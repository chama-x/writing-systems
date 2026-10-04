---
name: writing-systems
description: Audits and generates technical documentation, UI microcopy, system prompts, and inter-agent protocols using ASD-STE100 syntax, Minto BLUF, and Apple error standards.
---

# Writing Systems Agent Skill

Execute writing review and generation using this three-stage protocol.

## Stage 1: Surface Identification
Identify the applicable operational surface:
- **Human Prose:** Engineering specs, ADRs, PR reviews, and RFCs -> Enforce `docs/human-prose.md`.
- **UI & Microcopy:** Action buttons, CLI flags, and error recovery -> Enforce `docs/ui-microcopy.md`.
- **Agent Directives:** System instructions and polarity pairing -> Enforce `docs/prompt-engineering.md`.
- **Machine Protocols:** State RPCs and analytical subagent reporting -> Enforce `docs/inter-agent-protocols.md`.

## Stage 2: Universal Invariants
Apply these five invariants across all generation:
1. **Minto BLUF:** Deliver the governing finding or payload in the opening 50 tokens using Action, Conditional, or Diagnostic archetypes.
2. **Controlled Syntax:** Enforce maximum 20 words for instructions; 25 words for descriptions.
3. **Cadence Variance:** Alternate short assertions (5–10 words) with compound mechanics (15–25 words). Ban monotone runs and fragments.
4. **Literal Precision:** State concrete operational facts. Eliminate decorative metaphors.
5. **Ubiquitous Language:** Maintain canonical domain entities. Avoid synonym churn.

## Stage 3: Self-Contained Verification Checklist
Verify these four checkpoints before returning text:
- [ ] Deliver the governing finding or payload in the opening 50 tokens.
- [ ] Keep procedural sentences under 21 words and descriptive sentences under 26 words.
- [ ] Pair operational terms with concrete evidence; omit conversational filler tokens.
- [ ] Attribute error states to system conditions and provide direct recovery actions.
