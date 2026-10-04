# Machine State RPCs & Analytical Subagent Protocols

Machine coordination requires typed schemas and zero conversational tokens.

---

## 1. The Shannon Limit Principle

Natural language introduces entropy and parsing overhead between automated agents.
- **Zero Conversational Fluff:** Omit greetings, politeness tokens, and summaries.
- **Explicit State Mutations:** Report data modifications as deterministic diffs.
- **Schema Validation:** Validate automated state payloads against a strict JSON Schema.

### Operational Separation: State RPCs vs. Subagent Reports
1. **Automated State Mutations (RPCs):** Use the typed JSON Schema below. No natural language permitted.
2. **Analytical & Research Subagents:** Use Minto BLUF structured Markdown. Deliver findings concisely without conversational filler.

---

## 2. Inter-Agent Payload Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "InterAgentCoordinationPayload",
  "type": "object",
  "properties": {
    "task_id": { "type": "string" },
    "sender_agent": { "type": "string" },
    "action": {
      "type": "string",
      "enum": ["MUTATE_STATE", "QUERY_STATE", "DISPATCH_ERROR", "CONFIRM_COMPLETION"]
    },
    "target_entity": { "type": "string" },
    "state_diff": {
      "type": "object",
      "properties": {
        "previous_state": { "type": "object" },
        "mutation": { "type": "object" },
        "resulting_state": { "type": "object" }
      },
      "required": ["previous_state", "mutation", "resulting_state"]
    },
    "error_recovery": {
      "type": "object",
      "properties": {
        "is_fatal": { "type": "boolean" },
        "recovery_action": { "type": "string" }
      },
      "required": ["is_fatal", "recovery_action"]
    }
  },
  "required": ["task_id", "sender_agent", "action", "target_entity"],
  "allOf": [
    {
      "if": { "properties": { "action": { "const": "MUTATE_STATE" } } },
      "then": { "required": ["state_diff"] }
    },
    {
      "if": { "properties": { "action": { "const": "DISPATCH_ERROR" } } },
      "then": { "required": ["error_recovery"] }
    }
  ]
}
```

---

## 3. Analytical Subagent Markdown Reporting Schema

Analytical subagents return structured Markdown when tasks require code audits, research synthesis, or bug investigations.

### 3.1 Envelope Structure
Structure every analytical response according to this three-tier envelope:
1. **Executive BLUF:** Deliver the governing finding or verdict in the first 50 tokens.
2. **Empirical Findings:** Group observations with 2 to 4 word bold anchors. Include file paths and line ranges.
3. **Actionable Diffs:** Provide exact drop-in replacements or commands rather than open-ended recommendations.

### 3.2 Subagent Response Exemplar
```markdown
### BLUF: Database Migration Failed Due to Locked Schema Table
The PostgreSQL migration failed at 02:14 UTC because table billing_events held an active lock.

#### 1. Empirical Findings
- **Lock Contention:** Worker process 8421 held an open transaction on billing_events for 42 minutes.
- **Timeout Trigger:** Migration script timed out after 300 seconds at line 48 in migrations/004_add_index.sql.

#### 2. Actionable Fix
Terminate the blocking worker and retry migration:
```bash
SELECT pg_terminate_backend(8421);
./scripts/migrate.sh --retry
```
```

