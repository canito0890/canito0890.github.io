---
title: "From Vibe Coding to Spec-Driven Development: My Journey with AI Coding Tools"
date: 2026-03-08
categories: [development, ai-tools, process]
tags: [spec-driven-development, ai-coding, github-spec-kit, kiro, opencode, workflow]
excerpt: "Exploring the shift from vibe coding to spec-driven development using GitHub Spec Kit, AWS Kiro, and opencode—three tools that bring structure to AI-assisted coding."
toc: true
toc_label: "What We'll Cover"
toc_icon: "list-ul"
header:
  overlay_color: "#0f0f1e"
  overlay_filter: "0.5"
---

## Introduction

A few weeks ago, I wrapped up the synthwave redesign of this site using opencode. The results were solid—the AI generated clean, working CSS, handled the Jekyll templating without a hitch, and the whole thing came together faster than I expected.

But there were moments of friction.

Like when I asked for "a nice hover effect on the cards" and got something that looked great in isolation but broke the existing layout. Or when the AI implemented dark mode with localStorage persistence, but didn't account for my system preference detection. Twice I found myself refactoring code that would've been right the first time if I'd just... been more specific.

That's when it clicked: **the problem wasn't the tool. It was how I was communicating.**

## The Problem: Why Vibe Coding Hits a Wall

Let me give you a real example. Early in my AI coding journey, I asked Claude something simple:

```
Add user authentication
```

What did I get? A full OAuth2 implementation with Google and GitHub login. Except I wanted JWT tokens for a simple API. The AI made assumptions—reasonable ones, but wrong for my use case. I spent more time tearing it out than I would've spent writing it from scratch.

That's the thing about vague prompts: **AI fills in gaps with assumptions, and assumptions don't match your actual requirements.**

The "works on my machine" problem is real too. AI generates code that works beautifully in its own context—fresh project, no dependencies, ideal conditions. Then you drop it into your existing codebase and suddenly:

- Variable names conflict with your patterns
- It uses a library you don't have installed
- It doesn't respect your error handling approach
- The imports are wrong

You become the integrator, fixing what AI broke. And that defeats the whole point.

I needed a better way to communicate. That's when I discovered spec-driven development.

## What is Spec-Driven Development?

Spec-driven development (SDD) is about treating your requirements as a contract. The spec is the single source of truth. Code gets generated *from* the spec, not the other way around.

It's a four-phase workflow:

1. **Specify** — Define what you're building and why (user journeys, success criteria)
2. **Plan** — Choose your tech stack, architecture, constraints
3. **Tasks** — Break the plan into smaller, executable tasks
4. **Implement** — AI generates code based on the spec

```
Idea → Specify → Plan → Tasks → Implement → Verify ↔ Refine Spec
```

This isn't TDD (test-driven development). TDD has you write tests first, then code. SDD is broader—specs define behavior, constraints, and context before any code exists.

It's also different from traditional PRDs (product requirement documents). PRDs are static files that get filed away. SDD specs are living artifacts that evolve with the project and actively drive implementation.

**The benefits I've noticed:**

- **Less rework** — Catch misunderstandings before writing code
- **Architectural consistency** — AI follows your patterns, not its own
- **Better collaboration** — Specs are readable by humans and AI alike
- **Reduced cognitive load** — You don't need to hold every requirement in your head

## Three Tools, Three Approaches

### GitHub Spec Kit

[GitHub Spec Kit](https://github.com/anomalyco/spec-kit) is an open-source toolkit with 71K+ GitHub stars. It's CLI-first with slash commands and works with Claude Code, Copilot, Cursor, Gemini CLI, and 20+ other agents.

**How it works:**

- `/specify` — Generate detailed spec from high-level description
- `/plan` — Create technical architecture
- `/tasks` — Break into executable tasks
- `/implement` — Generate code

It's like giving AI guardrails. You get good balance of flexibility and structure—the slash commands make it feel intentional rather than like you're just chatting. Best for teams wanting structure without changing their workflow.

### AWS Kiro

[Kiro](https://kiro.ai) is an agentic AI IDE in public preview, built on Code OSS with Claude Sonnet integration. Pronounced "kee-ro" (Japanese for "crossroads").

The steering files concept is interesting. You create files in `.kiro/steering/`:

- `product.md` — User journeys and requirements
- `tech.md` — Technical decisions
- `security-policies.md` — Security constraints
- `api-standards.md`, `testing-standards.md`, `structure.md`

Then it guides you through: Requirements → Design → Task List → Coding.

My honest take? It's interesting but rigid. The steering files concept is genuinely useful, but the pipeline can feel restrictive when you want to iterate quickly. Also, being AWS-centric might limit appeal for some teams.

### opencode

[opencode](https://opencode.ai) is my daily driver—an open-source AI coding agent with 120K GitHub stars. It works in the terminal, desktop app, or IDE extension, and supports any model (Claude, GPT, Gemini, or local).

It's agent-based and conversational, with multi-session agents for parallel work and LSP-enabled understanding of your project structure. The flexibility is what sells me on it—it's already how I naturally work, and it fits naturally into SDD workflows as the implementation engine.

### Comparison Matrix

| Feature | GitHub Spec Kit | Kiro | opencode |
|---------|----------------|------|----------|
| Cost source) | Free | Free (open (preview) | Free (open source) |
| Platform | CLI | IDE (Code OSS) | Terminal, Desktop, IDE |
| Workflow style | Slash commands | Guided IDE | Agent-based |
| AI models | 20+ agents | Claude Sonnet | Any (75+ providers) |
| Learning curve | Medium | Low-Medium | Low |
| Flexibility | High | Low-Medium | High |
| Best for | Structured prompting | AWS teams | Exploratory + production |

## Side-by-Side Examples

### Example 1: User Authentication

**Vibe coding prompt:**
```
Add user authentication
```

**Spec-driven prompt:**
```markdown
Implement JWT authentication in auth/middleware.ts:
- Validate Bearer tokens from Authorization header
- Return 401 on expired/missing tokens
- Use RS256 from existing public key in config/jwt.pem
- Include user_id and email in request.user
- Token expiry: 24 hours
- Follow existing auth patterns in codebase (see auth/*.ts)
- No external API calls; all validation local
```

The difference? Vibe: AI guesses everything (stateless? stateful? OAuth? JWT? Sessions?). Spec: AI knows exactly what you want, follows your patterns, accounts for your constraints.

### Example 2: API Endpoint

**Vibe coding prompt:**
```
Create a users endpoint
```

**Spec-driven prompt:**
```markdown
Create GET /api/users endpoint in routes/users.ts:
- Query params: page (default 1), limit (default 20, max 100)
- Returns: { users: [...], pagination: { page, limit, total, pages } }
- Auth: Requires valid JWT (use existing auth middleware)
- Error handling: Return 500 on DB errors, 401 on auth failure
- Use existing database connection from lib/db.ts
- Follow REST conventions used in routes/posts.ts
- Include rate limiting (100 req/min per user)
```

### Example 3: The Dark Mode Fiasco

This one hit close to home. I asked AI to "add dark mode." It implemented it with CSS variables and localStorage—looked great, worked perfectly.

Except I wanted it to respect system preference by default, with a toggle to override. The AI assumed manual control was the primary approach. I had to refactor the whole thing after the fact.

**Spec-driven version:**
```markdown
Add dark mode toggle:
- Default: respect system preference (prefers-color-scheme)
- Toggle button in header (sun/moon icons)
- Persist choice to localStorage key 'theme-preference'
- Override system preference only when user explicitly toggles
- Use existing CSS variables in assets/css/main.scss
- Transition: 200ms ease for theme switch
- Include aria-label for accessibility
```

One extra paragraph in the prompt, and the AI nailed it.

## Honest Takeaways

**What surprised me:**

- **Spec Kit** — How much better the output is with structured prompts. The slash commands feel natural after a few uses.
- **Kiro** — Steering files are actually useful, but the rigid pipeline kills momentum during iteration.
- **opencode** — It's already how I naturally work. The multi-session feature is underrated.

**Which fits my workflow best:**

- opencode is my daily driver—flexibility wins
- Spec Kit adds structure when I need it
- Kiro interesting but not a fit for my style

**The learning curve reality:**

It's not about learning new tools—it's about changing how you write prompts. Start small: try one spec-driven prompt on a non-critical feature. You'll see the difference immediately.

**You don't need all three:**

Pick what fits your workflow. The tool matters less than the mindset. Spec-driven development is a practice, not a product.

## The Shift

Here's the key insight: **I'm not less of a developer—I'm writing better requirements.**

My role shifted from "writing syntax" to "writing intent." AI is incredibly capable—it just needs to know what you actually want.

Vibe coding still has a place (exploration, prototypes, quick experiments). But for production code, specs are the professional choice. The bottleneck isn't code generation—it's clear thinking.

## Closing

If you're using AI coding tools, try this: this week, on a non-critical feature, write a spec-driven prompt instead of a vibe prompt. Be specific about constraints, patterns, and expected behavior.

Notice the difference in output quality.

And if you want to explore further, check out:

- [GitHub Spec Kit](https://github.com/anomalyco/spec-kit)
- [Kiro](https://kiro.ai)
- [opencode](https://opencode.ai)

This site was redesigned with opencode—[check out that process here](/posts/synthwave-redesign-deep-dive/) if you're curious.

Got thoughts? Found this helpful? [Open an issue](https://github.com/canito0890/canito0890.github.io/issues) or [hit me up on GitHub](https://github.com/canito0890).

---

*Brewing up better specs, one prompt at a time.*
