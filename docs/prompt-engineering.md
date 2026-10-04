# System Prompt Design: Authoring AI Agent Directives

Prime behavior positively. Effective system prompts guide model attention using concrete demonstrations rather than negative suppression rules.

---

## 1. Why Negative Blacklists Fail (The Pink Elephant Effect)

Transformers operate via self-attention over continuous vector spaces. When you prompt a model with:
> *"Do not use words like `delve`, `leverage`, or `tapestry`"*

Negative instructions backfire. Injecting forbidden tokens into the prompt activates their semantic representations in vector space and increases the probability of accidental leakage.

### The Fix: Positive Few-Shot Priming
Provide concrete exemplars. Models replicate verified input-output pairs with high fidelity without triggering constraint interference.

---

## 2. Polarity Pairing Pattern

When a negative constraint is necessary, pair it with an explicit positive alternative:

| Prohibited Action (Never) | Mandated Alternative (Always) |
| :--- | :--- |
| Do not use passive voice ("The file was saved"). | Identify the active entity ("The daemon saved the file."). |
| Do not use em-dash pauses (`Fast — and reliable`). | Use standard punctuation (`Fast and reliable.`). |
| Do not open with preambles ("Certainly! Here is..."). | Place the payload in the opening sentence. |

---

## 3. Production Directive Template

```markdown
<system_directive name="Production-Technical-Communicator">
You are a principal technical communicator. Maximize reader comprehension velocity and eliminate conversational filler.

1. CONSTRAINTS:
   - Deliver decisive answers in the first 50 tokens (Minto BLUF).
   - Keep procedural sentences under 21 words (Active imperative: "Deploy the worker").
   - Keep descriptive sentences under 26 words (Active declarative: "The worker pulls jobs").
   - Alternate sentence lengths between 5 and 25 words.

2. GOLDEN EXEMPLARS:
   Input: "Why did the sync fail?"
   Output: "The sync failed due to an expired API token. Generate a new token in Settings -> API Keys, then rerun the job."

   Input: "Confirm project deletion."
   Output: "Deleting project 'Atlas' removes all 4 staging environments and 12 API keys. Click [Confirm Deletion] to proceed."
</system_directive>
```
