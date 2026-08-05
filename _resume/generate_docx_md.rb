#!/usr/bin/env ruby
# frozen_string_literal: true

# Renders _data/resume.yml as pandoc-flavored markdown on stdout, ready to be
# converted to .docx with _resume/reference.docx as the style template.
#
# Heading levels are chosen to match the styles in that template:
#   YAML title/subtitle -> Title / Subtitle
#   #                   -> Heading 1  (section names)
#   ##                  -> Heading 2  (company / school / certificate)
#
# Contact details come from tmp/resume.private.yml (gitignored) when present, so
# the editable document carries full contact info that the public site does not.
#
# Usage: ruby _resume/generate_docx_md.rb > tmp/resume-docx.md

require 'yaml'

ROOT = File.expand_path('..', __dir__)

resume = YAML.load_file(File.join(ROOT, '_data', 'resume.yml'))

private_path = File.join(ROOT, 'tmp', 'resume.private.yml')
if File.exist?(private_path)
  contact = YAML.load_file(private_path) || {}
else
  contact = {}
  warn "note: #{private_path} not found — generating without email/phone"
end

basics = resume.fetch('basics')
out = []

# Pandoc reads this metadata block and maps it onto the reference doc's
# Title/Subtitle styles.
out << '---'
out << "title: #{basics['name']}"
out << "subtitle: #{basics['label']}"
out << '---'
out << ''

# Contact block: one paragraph, hard-wrapped with trailing backslashes so each
# detail lands on its own line without becoming a separate paragraph.
contact_lines = [basics['location']]
contact_lines << contact['resume_email'] if contact['resume_email'].to_s != ''
contact_lines << contact['resume_phone'] if contact['resume_phone'].to_s != ''
Array(basics['profiles']).each { |profile| contact_lines << profile['url'] }
contact_lines << basics['availability'] if basics['availability'].to_s != ''
contact_lines.compact!

out << contact_lines.each_with_index.map { |line, i|
  i == contact_lines.size - 1 ? line : "#{line}\\"
}.join("\n")
out << ''

if resume['summary'].to_s != ''
  out << resume['summary'].strip.gsub(/\s*\n\s*/, ' ')
  out << ''
end

def section(out, title)
  out << "# #{title}"
  out << ''
end

section(out, 'SKILLS')
Array(resume['skills']).each do |group|
  out << "- **#{group['name']}:** #{Array(group['keywords']).join(', ')}"
end
out << ''

section(out, 'EXPERIENCE')
Array(resume['experience']).each do |job|
  role = job['role']
  role += " (#{job['engagement']})" if job['engagement'].to_s != ''
  where = [job['company'], job['location']].compact.reject(&:empty?).join(', ')

  out << "## #{where} — #{role}"
  out << ''
  out << "#{job['start']} - #{job['end']}"
  out << ''

  Array(job['highlights']).each { |highlight| out << "- #{highlight}" }
  out << '' unless Array(job['highlights']).empty?

  unless Array(job['tech']).empty?
    out << "*#{Array(job['tech']).join(' · ')}*"
    out << ''
  end
end

section(out, 'EDUCATION')
Array(resume['education']).each do |school|
  where = [school['institution'], school['location']].compact.reject(&:empty?).join(', ')
  years = school['start'] == school['end'] ? school['end'] : "#{school['start']} - #{school['end']}"

  out << "## #{where} — #{school['program']}"
  out << ''
  out << years
  out << ''

  Array(school['highlights']).each { |highlight| out << "- #{highlight}" }
  out << '' unless Array(school['highlights']).empty?
end

section(out, 'CERTIFICATIONS')
Array(resume['certifications']).each do |cert|
  heading = "#{cert['program']} — #{cert['issuer']}"
  heading += " (#{cert['status']})" if cert['status'].to_s != ''

  out << "## #{heading}"
  out << ''
  Array(cert['items']).each { |item| out << "- #{item}" }
  out << ''
end

# Collapse the runs of blank lines the section helpers leave behind.
puts out.join("\n").gsub(/\n{3,}/, "\n\n").strip
