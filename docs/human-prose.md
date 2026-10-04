# Human-Facing Prose: Strategic Memos, RFCs, PR Reviews & Technical Specs

Decisions must be immediate. Engineering documents must communicate decisive architectural choices within seconds of landing on a page.

---

## 1. Macro-Architecture: Every Page is Page One (EPPO)

Engineers rarely read documents cover to cover. Readers arrive through deep links, targeted search queries, or urgent production error traces.
- **EPPO Invariant (Mark Baker):** Every section must function as an autonomous modular unit. Provide sufficient local context so the text succeeds in isolation.
- **Progressive Disclosure:**
  - **Tier 1 (Glance):** Title, Minto BLUF summary, and visual comparison table.
  - **Tier 2 (Core):** Structured sections with layer-cake bold anchors.
  - **Tier 3 (Deep):** Footnotes, raw schema appendices, and reference links.

---

## 2. Minto BLUF Hierarchy

Lead with the verdict. Place the governing architectural decision or financial trade-off in the opening fifty tokens.

### 2.1 The Three BLUF Archetypes
Select the archetype matching your operational context:
- **Action BLUF (Procedures & Decisions):** State the direct architectural choice or operational remediation immediately.  
  *Exemplar:* Migrate event ingestion from microservices to a single Go daemon on bare metal.
- **Conditional BLUF (Engineering Trade-offs):** State the decision criteria across workload boundaries.  
  *Exemplar:* Adopt Kafka if event throughput exceeds 50,000 msg/sec; adopt PostgreSQL LISTEN/NOTIFY for simple single-node architectures.
- **Diagnostic BLUF (Audits & Root Cause):** State the primary failure mechanism and affected scope directly.  
  *Exemplar:* Ingestion latency spiked to 450ms due to unindexed foreign key lookups on billing_events.

### 2.2 Communication Registers
Engineering prose alternates between two interaction registers:
- **Operational Register (Runbooks, Incidents, PRs):** Use active imperative voice. Prioritize execution velocity and concise data diffs.
- **Collaborative Register (RFCs, ADRs, Strategic Memos):** Use active declarative voice. Provide collegial trade-off analysis while preserving the ban on AI slop words.

### 2.3 Before & After Transformation

#### BAD (Standard AI Preamble and Delayed Point)
```text
"Certainly! In today's fast-paced cloud landscape, it is increasingly crucial to delve into our system architecture. While microservices offer a seamless tapestry of modular components, they are not merely flexible, but also introduce complex operational dynamics. After carefully examining our ingestion pipeline, we have come to the realization that migrating to a monolithic binary could foster significant performance improvements..."
```

#### GOOD (Minto BLUF + Controlled Syntax)
> **Migrate event ingestion from microservices to a single Go daemon on bare metal.**  
>
> Microservices added 42ms of latency and introduced three network failure points. Consolidating to a monolithic daemon delivers three measurable results:
> - **Cost:** Reduces AWS egress expenses by $18,000 each month.
> - **Latency:** Lowers 99th-percentile ingestion latency from 58ms to 6ms.
> - **Operations:** Removes cross-service protobuf serialization and simplifies debugging to local logs.

---

## 3. Formatting Invariants

1. **Layer-Cake Scanning:** Lead every list item with a bold anchor defining the mechanism.
2. **Topological Escalation:** When three or more entities interact across time, provide a comparison table or Mermaid diagram instead of prose.
3. **Paragraph Limit:** Cap paragraph blocks at three sentences.

---

## 4. Pull Request & Code Review Protocols

Classify review urgency deterministically. Ambiguous review comments stall pull requests and force engineering teams into unnecessary synchronous meetings.

### 4.1 Severity Classification Tags
- **[Blocker]:** Halts the merge. Identifies architectural flaws, data corruption hazards, security vulnerabilities, or broken API contracts.
- **[Warning]:** Flags high-risk patterns. Identifies missing test coverage, performance hazards, or imminent maintainability debt without halting merges.
- **[Nit]:** Suggests minor polish. Identifies naming choices, syntax cleanups, or micro-optimizations that the author may decline.
- **[Question]:** Seeks architectural context. Requests rationale for non-obvious design choices without blocking the pull request.

### 4.2 Review Comment Structure
Lead every review comment with its severity tag and a concrete recommendation:
1. **Severity Tag:** Declare urgency on token 1 (`[Blocker]`, `[Warning]`, `[Nit]`, `[Question]`).
2. **Operational Rationale:** State the failure condition or risk within 25 words.
3. **Actionable Diff:** Supply an explicit code replacement rather than conversational guidance.
