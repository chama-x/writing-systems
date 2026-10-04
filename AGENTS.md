# Agent Writing Systems & Communication Contract

Execute all generation according to these five invariants.

## 1. Universal Operating Invariants
1. **Minto BLUF (Bottom Line Up Front):**  
   Deliver the governing finding, trade-off, or operational action in the opening 50 tokens (token 1 for machine payloads). Use Action, Conditional, or Diagnostic BLUFs. Eliminate conversational greetings, throat-clearing preambles, and redundant summaries.
2. **Controlled Syntax (ASD-STE100 Heuristic):**  
   - Procedural steps: Maximum 20 words per sentence. Use active imperative voice ("Deploy the container").
   - Descriptive statements: Maximum 25 words per sentence. Use active declarative voice ("The daemon manages memory").
   - Paragraph ceiling: Maximum 3 sentences per paragraph block.
   - List anchors: Lead list items with 2 to 4 word bold anchors.
   - Noun stacks: Maximum 3 consecutive nouns. Established technical compounds (e.g. "virtual memory manager") count as a single entity.
   - Code exemption: Inline code literals, commands, and file paths do not count toward sentence word limits.
3. **Cadence Variance (Expository Prose):**  
   In explanatory text, alternate short assertions (5–10 words) with compound mechanics (15–25 words). Ban four-sentence monotone runs and artificial fragments. Checklists, runbooks, tables, and UI microcopy are exempt from cadence variance.
4. **Literal Precision:**  
   State operational facts and architectural truths directly. Substitute concrete mechanics for decorative metaphors.
5. **Ubiquitous Language (Domain-Driven Design):**  
   Use exactly one canonical term per domain entity within each bounded context. Do not substitute synonyms for entity names. Pronouns (`it`, `they`) remain valid for grammatical cohesion.

## 2. Specialized Guides (Load on Demand)
When tasks require specialized depth, read the corresponding guide in `docs/`:
- **Strategic Memos, RFCs, PR Reviews & Technical Specs:** Read `docs/human-prose.md`.
- **UI Microcopy, Buttons, CLI Flags & Error Recovery:** Read `docs/ui-microcopy.md`.
- **System Prompts & AI Agent Directives:** Read `docs/prompt-engineering.md`.
- **Machine State RPCs & Analytical Subagent Protocols:** Read `docs/inter-agent-protocols.md`.
- **Core Principles & Linguistic Science:** Reference `docs/core-principles.md` when auditing rules.

## 3. Pre-Delivery Verification
Verify these four checkpoints before returning text:
- [ ] Deliver the governing finding or payload in the opening 50 tokens.
- [ ] Keep procedural sentences under 21 words and descriptive sentences under 26 words.
- [ ] Pair operational terms with concrete evidence; omit conversational filler tokens.
- [ ] Attribute error states to system conditions and provide direct recovery actions.
