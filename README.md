# AI Writing Systems & Cognitive Communication

[![CI](https://github.com/chama-x/writing-systems/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/writing-systems/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Standard: AAIF AGENTS.md](https://img.shields.io/badge/Standard-AAIF%20AGENTS.md-emerald.svg)](https://agents.md)
[![Specification: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io-purple.svg)](https://agentskills.io)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-success.svg)](#)
[![Token Savings](https://img.shields.io/badge/Context%20Savings--60%25-orange.svg)](#)

An open-source specification and zero-dependency linter that eliminates conversational AI slop, enforces Minto BLUF, and structures deterministic multi-agent communication. Grounded in aerospace maintenance syntax (ASD-STE100) and Apple attribution theory.

---

## Quickstart: The One-Command Scaffolder

Scaffold the vendor-neutral contract, Vale prose styles, and standalone linter directly into any project root:

```bash
npx writing-systems init
```

*Like `shadcn/ui`, you own the code. No permanent runtime dependencies added.*

---

## Proof of Life: The Before & After Contrast

```text
┌── [BEFORE] DEFAULT CONVERSATIONAL AI SLOP (312 Tokens) ──────────────────────────┐
│ "Certainly! In today's fast-paced cloud landscape, it is increasingly crucial to │
│ delve into our system architecture. While microservices offer a seamless         │
│ tapestry of modular components, they are not merely flexible, but also           │
│ introduce complex operational dynamics. After carefully examining our           │
│ ingestion pipeline, we have come to the realization that migrating to a          │
│ monolithic binary could foster significant performance improvements..."          │
└──────────────────────────────────────────────────────────────────────────────────┘

┌── [AFTER] WRITING SYSTEMS MINTO BLUF (84 Tokens, -73% Waste) ────────────────────┐
│ Migrate event ingestion from microservices to a single Go daemon on bare metal.  │
│                                                                                  │
│ Microservices added 42ms of latency and introduced three network failure points. │
│ Consolidating to a monolithic daemon delivers three measurable results:          │
│ - Cost: Reduces AWS egress expenses by $18,000 each month.                       │
│ - Latency: Lowers 99th-percentile ingestion latency from 58ms to 6ms.            │
│ - Operations: Removes cross-service protobuf serialization and simplifies logs.  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## The 5 Universal Operating Invariants

| Invariant | Target Standard | What to Do | What to Ban |
| :--- | :--- | :--- | :--- |
| **1. Minto BLUF** | First 50 tokens | Apply Action, Conditional, or Diagnostic BLUFs | Greetings, preambles, throat-clearing |
| **2. Controlled Syntax** | Max 20w (proc) / 25w (desc) | Active voice; <= 3 noun stacks | Passive nominalizations, run-on clauses |
| **3. Cadence Variance** | Alternate 5w and 25w | Alternate punchy assertions with compound mechanics | Monotone runs (>= 4 same length) and fragments |
| **4. Literal Precision** | Operational facts | State concrete system mechanics directly | Decorative metaphors, conversational filler |
| **5. Ubiquitous Language** | Canonical entity naming | Single canonical term per domain concept | Casual entity synonym swapping |

---

## The 4 Operational Surfaces

1. **[Human-Facing Prose](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/docs/human-prose.md):** Architecture decision records, RFCs, PR reviews, and technical specs. Covers Operational and Collaborative registers.
2. **[UI & Forms Design](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/docs/ui-microcopy.md):** Microcopy, action buttons, CLI flag help strings, Apple error triad, and accessibility.
3. **[Agent Directives](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/docs/prompt-engineering.md):** Production system prompts, polarity pairing, and behavioral guardrails.
4. **[Machine State Protocols](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/docs/inter-agent-protocols.md):** Typed JSON schemas, deterministic state diffs, and analytical subagent reporting envelopes.

---

## Automated CI/CD Integration

Add automated prose and syntax linting to your repository workflow with two lines:

```yaml
- name: Verify Writing Systems
  uses: chama-x/writing-systems@v1
  with:
    path: 'docs/**/*.md'
```

Or run the zero-dependency Python validator locally:

```bash
python3 scripts/check_writing.py docs/*.md
```

---

## Repository Structure

```text
writing-systems/
├── AGENTS.md                    # Universal AI agent contract (AAIF / Linux Foundation)
├── CLAUDE.md                    # Claude Code pointer (@AGENTS.md)
├── action.yml                   # Composite GitHub Action for CI pipelines
├── bin/cli.js                   # Zero-dependency npx scaffolder
├── docs/                        # Authoritative topic guides
│   ├── core-principles.md       # Cognitive science, BLUF, and syntax bounds
│   ├── human-prose.md           # Technical documentation, RFCs, and PR reviews
│   ├── ui-microcopy.md          # UI text, CLI flags, and error recovery
│   ├── prompt-engineering.md    # System prompts and polarity pairing
│   ├── inter-agent-protocols.md # Machine state RPCs and analytical subagents
│   └── viral-case-studies.md    # 2026 distribution benchmarks & research
├── skills/                      # Portable agent skill (agentskills.io spec)
│   └── writing-systems/
│       └── SKILL.md             # On-demand tool skill for coding agents
├── .vale/                       # Vale prose linter configuration
├── scripts/                     # Standalone Python linter (zero dependencies)
└── LAUNCH_KIT.md                # Turnkey viral launch posts (HN, X, Reddit)
```

---

## License & Community

- **License:** Licensed under the [MIT License](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/LICENSE).
- **Contributing:** Read our [Contribution Guide](file:///Users/chamaththiwanka/Desktop/0/Projects/writing-systems/CONTRIBUTING.md) to propose invariant modifications.
- **Specification:** Adheres to Linux Foundation AAIF `AGENTS.md` and `agentskills.io`.
