# Contributing to AI Writing Systems

We welcome contributions that improve cognitive clarity, reduce conversational token waste, and refine agent communication standards.

---

## 1. Ground Rules for Contributions

All proposals and documentation changes must satisfy these three requirements:
- **No Invariant Dilution:** Core invariants (Minto BLUF, Controlled Syntax, Cadence Variance, Literal Precision, Ubiquitous Language) cannot be weakened.
- **Evidence-Based Rationale:** Cite cognitive ergonomics, working memory constraints, or empirical multi-agent benchmarks for any proposed rule changes.
- **Zero Linter Violations:** All markdown changes must pass `python3 scripts/check_writing.py` with zero errors and zero warnings.

---

## 2. Local Development & Verification

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chama-x/writing-systems.git
   cd writing-systems
   ```

2. **Run the standalone linter:**
   ```bash
   python3 scripts/check_writing.py AGENTS.md README.md skills/writing-systems/SKILL.md docs/*.md
   ```

3. **Verify CLI packaging:**
   ```bash
   node bin/cli.js info
   ```

---

## 3. Pull Request Review Protocol

This repository practices what it preaches. Review comments must use deterministic severity tags:
- **`[Blocker]`:** Halts the merge for architectural regressions, broken CLI syntax, or banned slop words.
- **`[Warning]`:** Flags readability hazards or non-standard entity synonyms without blocking the pull request.
- **`[Nit]`:** Suggests minor phrasing polish that the author may decline.
- **`[Question]`:** Inquires about design trade-offs without blocking the merge.
