# Blog Post Plan: From Vibe Coding to Spec-Driven Development

## Metadata

- **Title**: "From Vibe Coding to Spec-Driven Development: My Journey with AI Coding Tools"
- **Date**: 2026-03-08
- **Categories**: [development, ai-tools, process]
- **Tags**: [spec-driven-development, ai-coding, github-spec-kit, kiro, opencode, workflow]
- **Excerpt**: Exploring the shift from vibe coding to spec-driven development using GitHub Spec Kit, AWS Kiro, and opencode—three tools that bring structure to AI-assisted coding.
- **Tone**: Personal, conversational, first-person
- **Audience**: Developers using AI coding tools who want better results
- **Estimated Length**: 1,500-2,000 words

---

## Hook & Context (Personal)

**Opening paragraph:**
- Reference your synthwave redesign experience with opencode
- The moment of realization: "This works, but..."
- What led you to explore spec-driven development

**Key points to cover:**
- You used opencode for the redesign
- It worked great for generating code
- But there were moments of friction: "works on my machine" issues, requirements that weren't clear
- The realization: the problem wasn't the tool, it was how you were communicating

---

## The Problem: Why Vibe Coding Hits a Wall

**Your own examples of AI "hallucinating" requirements:**
- A feature you asked for that got implemented completely differently than expected
- Missing edge cases the AI didn't ask about
- Code that looked great but didn't compile or integrate with existing codebase

**What happens when prompts are too vague:**
- AI fills in gaps with assumptions
- Assumptions don't match your actual requirements
- End up refactoring more than if you'd written it manually

**The "works on my machine" problem:**
- AI generates code that works in isolation
- Doesn't account for your specific tech stack, patterns, constraints
- You become the integrator, fixing what AI broke

**Transition:** "I needed a better way to communicate with AI. That's when I discovered spec-driven development."

---

## What is Spec-Driven Development? (Overview)

**Definition (in your own words):**
- Spec-driven development = treating your requirements as a contract
- The spec is the single source of truth
- Code is generated FROM the spec, not the other way around

**The 4-phase workflow (plain language):**
1. **Specify**: Define what you're building and why (user journeys, success criteria)
2. **Plan**: Choose your tech stack, architecture, constraints
3. **Tasks**: Break the plan into smaller, executable tasks
4. **Implement**: AI generates code based on the spec

**Visual idea:** Simple ASCII or description of flow:
```
Idea → Specify → Plan → Tasks → Implement → Verify ↔ Refine Spec
```

**How it differs from TDD:**
- TDD: Write tests first, then code
- SDD: Write specifications first, then generate code
- Specs are broader than tests—they define behavior, constraints, and context

**How it differs from traditional PRDs:**
- PRDs are static documents that get filed away
- SDD specs are living, executable artifacts
- They evolve with the project and drive implementation

**Benefits (your perspective):**
- Less rework: catch misunderstandings early
- Architectural consistency: AI follows your patterns
- Better collaboration: specs are readable by humans and AI
- Reduced cognitive load: you don't need to hold all requirements in your head

---

## Three Tools, Three Approaches

### GitHub Spec Kit

**What it is:**
- Open-source toolkit (71K+ GitHub stars)
- CLI-first with slash commands
- Works with Claude Code, Copilot, Cursor, Gemini CLI, and 20+ agents

**How it works:**
- `/specify` - Generate detailed spec from high-level description
- `/plan` - Create technical architecture
- `/tasks` - Break into executable tasks
- `/implement` - Generate code

**Best for:**
- Teams wanting structure without changing their workflow
- Developers who prefer CLI tools

**Your take (honest opinion):**
- "It's like giving AI guardrails"
- Good balance of flexibility and structure
- The slash commands make it feel intentional

**Link:** https://github.com/anomalyco/spec-kit

---

### AWS Kiro

**What it is:**
- Agentic AI IDE (public preview)
- Pronounced "kee-ro" (Japanese for "crossroads")
- Built on Code OSS with Claude Sonnet integration

**How it works:**
- Steering files in `.kiro/steering/`:
  - product.md - user journeys and requirements
  - tech.md - technical decisions
  - security-policies.md - security constraints
  - api-standards.md, testing-standards.md, structure.md
- Guided workflow: Requirements → Design → Task List → Coding

**Best for:**
- AWS-centric teams
- Developers who want more guided AI workflows

**Your take (honest opinion):**
- "Interesting but rigid"
- The steering files concept is compelling
- The pipeline can feel restrictive during iteration
- AWS model constraints may limit appeal

**Link:** https://kiro.ai

---

### opencode

**What it is:**
- Open-source AI coding agent (120K GitHub stars)
- Terminal, desktop app, and IDE extension
- Works with any model (Claude, GPT, Gemini, or local)

**How it works:**
- Agent-based, conversational
- Multi-session agents for parallel work
- LSP-enabled, understands your project structure

**Best for:**
- Flexible development workflows
- Developers who want control over their process

**Your take (your daily driver):**
- Used it for the synthwave redesign
- Strengths: flexibility, multi-model support, privacy-first
- Fits naturally into SDD workflows as the implementation engine

**Link:** https://opencode.ai

---

## Comparison Matrix

| Feature | GitHub Spec Kit | Kiro | opencode |
|---------|----------------|------|----------|
| Cost | Free (open source) | Free (preview) | Free (open source) |
| Platform | CLI | IDE (Code OSS) | Terminal, Desktop, IDE |
| Workflow style | Slash commands | Guided IDE | Agent-based |
| AI models | 20+ agents | Claude Sonnet | Any (75+ providers) |
| Learning curve | Medium | Low-Medium | Low |
| Flexibility | High | Low-Medium | High |
| Best for | Structured prompting | AWS teams | Exploratory + production |

---

## Side-by-Side Code Examples

### Example 1: User Authentication

**Vibe coding prompt:**
```
"Add user authentication"
```

**Spec-driven prompt:**
```markdown
"Implement JWT authentication in auth/middleware.ts:
- Validate Bearer tokens from Authorization header
- Return 401 on expired/missing tokens
- Use RS256 from existing public key in config/jwt.pem
- Include user_id and email in request.user
- Token expiry: 24 hours
- Follow existing auth patterns in codebase (see auth/*.ts)
- No external API calls; all validation local"
```

**The difference:**
- Vibe: AI guesses everything (stateless? stateful? OAuth? JWT? Sessions?)
- Spec: AI knows exactly what you want, follows your patterns, accounts for constraints

---

### Example 2: API Endpoint

**Vibe coding prompt:**
```
"Create a users endpoint"
```

**Spec-driven prompt:**
```markdown
"Create GET /api/users endpoint in routes/users.ts:
- Query params: page (default 1), limit (default 20, max 100)
- Returns: { users: [...], pagination: { page, limit, total, pages } }
- Auth: Requires valid JWT (use existing auth middleware)
- Error handling: Return 500 on DB errors, 401 on auth failure
- Use existing database connection from lib/db.ts
- Follow REST conventions used in routes/posts.ts
- Include rate limiting (100 req/min per user)"
```

---

### Example 3: Feature Flag (Real-world)

**What actually happened to you (personal example):**
- You asked AI: "Add dark mode"
- AI implemented it with CSS variables and localStorage
- But you wanted it to respect system preference by default
- Had to refactor after the fact

**Spec-driven version:**
```markdown
"Add dark mode toggle:
- Default: respect system preference (prefers-color-scheme)
- Toggle button in header (sun/moon icons)
- Persist choice to localStorage key 'theme-preference'
- Override system preference only when user explicitly toggles
- Use existing CSS variables in assets/css/main.scss
- Transition: 200ms ease for theme switch
- Include aria-label for accessibility"
```

---

## Honest Takeaways

### What surprised you about each tool:

**Spec Kit:**
- How much better the output is with structured prompts
- The slash commands feel natural after a few uses

**Kiro:**
- The steering files concept is actually useful
- But the rigid pipeline can kill momentum during iteration

**opencode:**
- It's already how you naturally work
- The multi-session feature is underrated

### Which fit your workflow best:

- opencode is your daily driver (flexibility wins)
- Spec Kit adds structure when you need it
- Kiro interesting but not a fit for your style

### The learning curve reality:

- It's not about learning new tools—it's about changing how you write prompts
- Start small: try one spec-driven prompt on a non-critical feature
- You'll see the difference immediately

### You don't need all three:

- Pick what fits your workflow
- The tool matters less than the mindset
- Spec-driven development is a practice, not a product

---

## The Shift

**Key insight:**
- "I'm not less of a developer—I'm writing better requirements"
- Your role shifts from "writing syntax" to "writing intent"
- AI is incredibly capable—it just needs to know what you actually want

**The future:**
- Vibe coding still has a place (exploration, prototypes)
- But for production code, specs are the professional choice
- The bottleneck isn't code generation—it's clear thinking

---

## Closing

**Call to action:**
- Try one tool this week on a non-critical feature
- Or just try writing a spec-driven prompt in your current tool
- Notice the difference in output quality

**Invitation:**
- Share your experience
- What worked, what didn't
- Your own tips for working with AI coding agents

---

## Resources to Link

- GitHub Spec Kit: https://github.com/anomalyco/spec-kit
- Kiro: https://kiro.ai
- opencode: https://opencode.ai
- Minimal Mistakes (theme): https://mmistakes.github.io/minimal-mistakes/
- Your synthwave redesign post (cross-link)

---

## Writing Tips

- Keep first-person voice throughout
- Include code blocks with syntax highlighting
- Use tables for comparisons (render well on the blog)
- Add personal anecdotes like the dark mode example
- End each section with your honest take
- Make it feel like sharing with a developer friend

---

## Future Follow-up Posts (Optional)

1. "Spec-Driven Development Deep Dive: A Real Project Example"
2. "Comparing AI Coding Agents: Which One Should You Use?"
3. "How I Use opencode for My Jekyll Workflow"
