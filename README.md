# Writing Systems

**Make AI write clearly. Cut the fluff. Get to the point.**

[![CI](https://github.com/chamaththiwanka/writing-systems/actions/workflows/ci.yml/badge.svg)](https://github.com/chamaththiwanka/writing-systems/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success.svg)](#)

---

## The Problem

AI assistants (ChatGPT, Claude, Gemini, Copilot) pad their answers with filler words. They open with *"Certainly! In today's fast-paced world…"* before reaching the actual point. This wastes your time and burns tokens, which cost money.

**Writing Systems fixes this.** Drop a rules file into your project. AI reads it, then writes shorter and clearer answers.

---

## See the Difference

```text
┌── ❌ BEFORE: Typical AI response (312 tokens) ─────────────────────────────────┐
│ "Certainly! In today's fast-paced cloud landscape, it is increasingly crucial  │
│ to delve into our system architecture. While microservices offer a seamless    │
│ tapestry of modular components, they are not merely flexible, but also         │
│ introduce complex operational dynamics. After carefully examining our          │
│ ingestion pipeline, we have come to the realization that migrating to a        │
│ monolithic binary could foster significant performance improvements..."        │
└────────────────────────────────────────────────────────────────────────────────┘

┌── ✅ AFTER: With Writing Systems (84 tokens - 73% shorter) ───────────────────┐
│ Migrate event ingestion from microservices to a single Go daemon.             │
│                                                                                │
│ Microservices added 42ms of latency and three network failure points.         │
│ A single daemon delivers three improvements:                                  │
│ - Cost: Saves $18,000/month in AWS data transfer fees.                        │
│ - Speed: Cuts 99th-percentile latency from 58ms to 6ms.                       │
│ - Simplicity: Removes cross-service serialization; logs stay local.           │
└────────────────────────────────────────────────────────────────────────────────┘
```

Same information. 73% fewer words. The answer comes first.

---

## Get Started in One Command

Run this inside any project folder:

```bash
npx writing-systems init
```

This copies the writing rules into your project. No packages are installed permanently - you own the files, and you can edit them however you like.

> Think of it like a template. The command drops files into your project, then gets out of the way.

---

## What Gets Added to Your Project

| File | What It Does |
| :--- | :--- |
| `AGENTS.md` | The main rules file. AI tools read this and follow its writing instructions. |
| `docs/*.md` | Detailed guides for different writing situations (documentation, UI text, prompts, etc.). |
| `.vale/` | Optional config for [Vale](https://vale.sh), a prose-checking tool that can flag rule violations automatically. |
| `scripts/check_writing.py` | A small Python script that checks your writing against the rules. No installs needed beyond Python 3. |

---

## The 5 Writing Rules (Plain English)

These five rules are the core of the system. Every one exists to save the reader's time.

### 1. Lead with the Answer

> Don't warm up. Don't introduce yourself. Start with the conclusion, the decision, or the action.

**Bad:** *"After careful consideration of various factors…"*
**Good:** *"Use PostgreSQL. Here's why."*

### 2. Keep Sentences Short

> Instructions: 20 words max. Descriptions: 25 words max. If a sentence needs a deep breath to read aloud, split it.

### 3. Vary Your Rhythm

> Mix short punchy sentences with longer explanatory ones. Avoid four sentences in a row that all sound the same length - it puts readers to sleep.

### 4. Say What You Mean

> No vague phrases like *"a rich ecosystem of modular components."* State the actual system behavior. Readers need facts, not decoration.

### 5. One Name Per Thing

> Pick one term for each concept and stick with it. If you call it a "daemon" once, don't switch to "service" or "process" later in the same document.

<details>
<summary><strong>📘 What are the formal names for these rules?</strong></summary>

If you read academic papers or see these terms in the codebase, here's the mapping:

| Plain Name | Formal Name | Origin |
| :--- | :--- | :--- |
| Lead with the Answer | Minto BLUF (Bottom Line Up Front) | Barbara Minto's *The Pyramid Principle*, U.S. military communication doctrine |
| Keep Sentences Short | ASD-STE100 Controlled Syntax | Aerospace & Defence Industries Association of Europe - used in aircraft maintenance manuals |
| Vary Your Rhythm | Cadence Variance | Composition theory and readability research |
| Say What You Mean | Literal Precision | Technical writing best practices |
| One Name Per Thing | Ubiquitous Language | Eric Evans' *Domain-Driven Design* (2003) |

</details>

---

## Who Is This For?

### 🟢 Beginners - "I just want AI to write better"

1. Run `npx writing-systems init` in your project.
2. Open the `AGENTS.md` file it creates.
3. Paste that file's contents into your AI tool's system prompt (or place it at your project root - many AI coding tools read it automatically).
4. Done. Your AI writes shorter, clearer answers from now on.

### 🟡 Intermediate - "I want automated checks in my workflow"

Add the linter to your CI pipeline so pull requests get checked automatically:

```yaml
# .github/workflows/ci.yml
- name: Check Writing Quality
  uses: chama-x/writing-systems@v1
  with:
    path: 'docs/**/*.md'
```

Or run checks locally before pushing:

```bash
python3 scripts/check_writing.py docs/*.md
```

The script checks sentence length, detects filler words, and flags common problems. It needs only Python 3 - no extra packages.

### 🔴 Expert - "I want to customize the rules for my team"

The `docs/` folder contains specialized guides you can modify:

| Guide | Covers |
| :--- | :--- |
| [core-principles.md](docs/core-principles.md) | The cognitive science behind each rule - working memory limits, information foraging theory |
| [human-prose.md](docs/human-prose.md) | Technical documents: architecture decisions, RFCs, code reviews, specifications |
| [ui-microcopy.md](docs/ui-microcopy.md) | Button labels, error messages, CLI help text, form validation messages |
| [prompt-engineering.md](docs/prompt-engineering.md) | Writing system prompts for AI agents and assistants |
| [inter-agent-protocols.md](docs/inter-agent-protocols.md) | Structured JSON communication between AI agents in multi-agent systems |

Every rule in `AGENTS.md` traces back to a principle in `docs/core-principles.md`. Change the principle, and you change the rule.

---

## Project Structure

```text
writing-systems/
├── AGENTS.md               # The writing rules - AI tools read this file
├── bin/cli.js              # The "npx writing-systems init" scaffolder
├── docs/                   # Detailed guides for each writing context
│   ├── core-principles.md  # Why each rule exists (the science)
│   ├── human-prose.md      # Rules for technical documentation
│   ├── ui-microcopy.md     # Rules for UI text and error messages
│   ├── prompt-engineering.md   # Rules for AI system prompts
│   └── inter-agent-protocols.md # Rules for machine-to-machine messages
├── skills/                 # Portable skill file for AI coding agents
│   └── writing-systems/
│       └── SKILL.md        # Drop-in skill for tools that support agentskills.io
├── scripts/
│   └── check_writing.py    # Standalone linter - only needs Python 3
├── .vale/                  # Config for the Vale prose-checking tool
├── action.yml              # GitHub Action for automated CI checks
└── package.json            # npm package config (for npx distribution)
```

---

## Frequently Asked Questions

<details>
<summary><strong>Does this actually change how AI writes?</strong></summary>

Yes. AI language models follow the instructions in their system prompt. When you give them clear writing rules - short sentences, answer-first structure, no filler - they follow them. The before/after example at the top of this page is a real output comparison.

</details>

<details>
<summary><strong>What AI tools does this work with?</strong></summary>

Any tool that reads an `AGENTS.md` or `CLAUDE.md` file from your project root, or any tool where you can set a system prompt. This includes Claude Code, GitHub Copilot, Cursor, Windsurf, Google Antigravity, and others. You can also paste the rules into ChatGPT or Gemini's custom instructions.

</details>

<details>
<summary><strong>Do I need Node.js or Python?</strong></summary>

- **Node.js** is needed only for the one-time `npx writing-systems init` setup command. After that, you can delete Node if you want - the generated files are plain Markdown.
- **Python 3** is needed only if you want to run the automated linter (`check_writing.py`). The linter has zero dependencies beyond the Python standard library.
- **Neither** is required if you just copy the `AGENTS.md` file manually.

</details>

<details>
<summary><strong>Will this break my existing documentation?</strong></summary>

No. The `init` command only adds new files. It does not modify any of your existing files. You choose which rules to adopt and when to adopt them.

</details>

<details>
<summary><strong>Can I change the rules?</strong></summary>

Yes - that's the point. You own every file. Edit `AGENTS.md` to relax sentence limits, add domain-specific terms, or remove rules that don't fit your team. The `docs/core-principles.md` file explains why each rule exists, so you can make informed changes.

</details>

---

## Standards & Compatibility

This project follows two open standards:

- **[AAIF `AGENTS.md`](https://agents.md)** - A Linux Foundation specification that defines how AI agents discover project-level instructions. Place an `AGENTS.md` file at your repo root and compatible tools read it automatically.
- **[agentskills.io](https://agentskills.io)** - A specification for portable AI agent skills. The `skills/writing-systems/SKILL.md` file lets any compatible coding agent load these writing rules on demand.

---

## Contributing

Read the [Contribution Guide](CONTRIBUTING.md) before opening a pull request. The short version:

1. Don't weaken the core rules without evidence.
2. Run `python3 scripts/check_writing.py` and fix all warnings before submitting.
3. Tag your review comments with severity: `[Blocker]`, `[Warning]`, `[Nit]`, or `[Question]`.

---

## License

[MIT](LICENSE) - use it however you like, commercially or otherwise.
