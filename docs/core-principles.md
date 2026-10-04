# Core Principles: Cognitive Clarity & Linguistic Science

Digital readers scan technical text for immediate operational answers. This document outlines the working memory constraints and linguistic invariants that govern this writing system.

---

## 1. Minto BLUF (Bottom Line Up Front)

Human working memory decays within two seconds. Multi-clausal sentences flood this fragile buffer and force readers to drop their operational task goals.
- **Cognitive Decay:** Readers evict architectural goals when preambles delay critical conclusions.
- **BLUF Invariant:** Deliver the governing finding, trade-off, or operational action in the first 50 tokens.
- **Three Archetypes:** Apply Action BLUFs for procedures, Conditional BLUFs for bi-modal trade-offs, and Diagnostic BLUFs for investigations.
- **Information Foraging:** Front-load operative nouns and verbs to provide immediate information scent.

---

## 2. Controlled Syntax (ASD-STE100 Heuristic)

Aerospace engineers developed ASD-STE100 to eliminate ambiguity. Adapting these constraints to software documentation ensures that readers process technical descriptions without cognitive strain.

### The Production Rules:
1. **Sentence Word Ceilings:**  
   - Procedural instructions: Maximum 20 words per sentence.
   - Descriptive statements: Maximum 25 words per sentence.
2. **Voice Separation:**  
   - Procedural: Active imperative ("Inspect the manifold").
   - Descriptive: Active declarative ("The manifold regulates pressure").
3. **Noun Stack Cap:**  
   - Maximum 3 consecutive nouns. Convert "production database cluster failure rate" -> "failure rate of the production database cluster."
4. **Paragraph Ceiling:**  
   - Maximum 3 sentences per paragraph block.
5. **Two-Tier Enforcement:**  
   - Prompt directives enforce cognitive clarity, while background linters verify mechanical word counts.

---

## 3. Cadence Variance (Expository Prose)

Monotonous rhythm numbs the reader. Alternating punchy five-word assertions with twenty-word compound explanations maintains engagement and mirrors human thought.
- **Cadence Alternation:** In explanatory text, alternate punchy assertions (5–10 words) with compound mechanics (15–25 words).
- **Uniform Cadence Ban:** Avoid monotonous runs of four consecutive sentences of identical length.
- **Complete Propositions:** Every sentence must contain a subject and predicate. Ban artificial telegraphic fragments.
- **Structural Exemptions:** Checklists, runbooks, tables, and UI microcopy are exempt from cadence variance.

---

## 4. Literal Precision

Metaphors obscure system mechanics. Technical readers need direct statements of architectural reality to diagnose failures accurately under operational pressure.
- **Physical Grounding:** State physical, operational, and architectural truths directly.
- **Metaphor Elimination:** Substitute explicit system behavior for decorative idioms or figurative analogies.

---

## 5. Ubiquitous Language (Domain-Driven Design)

Synonyms fracture conceptual integrity. Using multiple labels for the same entity forces engineers to pause and evaluate false distinctions.
- **Canonical Terminology:** Assign exactly one term to each domain concept within a bounded context. Never alternate between synonyms.
- **Grammatical Cohesion:** Pronouns (`it`, `they`) remain valid for local cohesion once an entity is named.

