#!/usr/bin/env python3
"""Build _resume/reference.docx: the pandoc style template for the résumé .docx.

Pandoc's --reference-doc supplies styles, fonts, and page setup for generated
documents but never its body text. This script derives that template from the
original Google Docs export so regenerated résumés keep the same look, while
stripping every trace of personal data — the file is committed to a public repo.

Removed: the body content, the embedded photo, and the mailto:/profile hyperlink
relationships. Kept: styles.xml (Title/Subtitle/Heading1-6), the embedded
Proxima Nova fonts, numbering, theme, and the page header.

Regenerate with:
    python3 _resume/make_reference_docx.py tmp/Resume.docx _resume/reference.docx
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

# The source template indents content 2.25in from the right, which wastes a
# quarter of every page. Normalize to a 1in margin (1440 twentieths of a point).
NORMALIZED_RIGHT_MARGIN = "1440"

DROP_PARTS = {"word/media/image2.jpg"}
DROP_REL_TYPES = ("hyperlink",)
DROP_REL_TARGETS = ("media/image2.jpg",)


def empty_document_xml(original: str) -> str:
    """Return document.xml with all body content removed but sectPr preserved."""
    section = re.search(r"<w:sectPr.*?</w:sectPr>", original, re.S)
    if not section:
        raise SystemExit("error: no <w:sectPr> found; unexpected .docx structure")

    sect_pr = section.group(0)
    sect_pr = re.sub(
        r'(<w:pgMar[^>]*?w:right=")[0-9]+(")',
        rf"\g<1>{NORMALIZED_RIGHT_MARGIN}\g<2>",
        sect_pr,
    )

    header = original[: original.index("<w:body>")]
    return f"{header}<w:body>{sect_pr}</w:body></w:document>"


def strip_rels(original: str) -> str:
    """Drop hyperlink and image relationships (they carry personal data)."""

    def keep(match: str) -> bool:
        if any(f"/{t}" in match and 'Type="' in match for t in DROP_REL_TYPES):
            type_attr = re.search(r'Type="[^"]*/([^/"]+)"', match)
            if type_attr and type_attr.group(1) in DROP_REL_TYPES:
                return False
        return not any(t in match for t in DROP_REL_TARGETS)

    return re.sub(
        r"<Relationship\b[^>]*/>",
        lambda m: m.group(0) if keep(m.group(0)) else "",
        original,
    )


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} <source.docx> <reference.docx>")

    source, target = Path(sys.argv[1]), Path(sys.argv[2])
    if not source.is_file():
        raise SystemExit(f"error: source not found: {source}")

    tmp_target = target.with_suffix(".docx.tmp")
    with zipfile.ZipFile(source) as src, zipfile.ZipFile(
        tmp_target, "w", zipfile.ZIP_DEFLATED
    ) as out:
        for item in src.infolist():
            if item.filename in DROP_PARTS:
                continue

            data = src.read(item.filename)
            if item.filename == "word/document.xml":
                data = empty_document_xml(data.decode("utf-8")).encode("utf-8")
            elif item.filename == "word/_rels/document.xml.rels":
                data = strip_rels(data.decode("utf-8")).encode("utf-8")

            out.writestr(item, data)

    # Refuse to ship a template that still contains personal data.
    with zipfile.ZipFile(tmp_target) as check:
        for name in check.namelist():
            if name.endswith((".xml", ".rels")):
                body = check.read(name).decode("utf-8", "replace").lower()
                for needle in ("gmail", "mailto", "linkedin.com"):
                    if needle in body:
                        tmp_target.unlink()
                        raise SystemExit(
                            f"error: '{needle}' still present in {name}; not written"
                        )

    shutil.move(str(tmp_target), str(target))
    kb = target.stat().st_size // 1024
    print(f"wrote {target} ({kb} KB) — styles and fonts kept, personal data stripped")


if __name__ == "__main__":
    main()
