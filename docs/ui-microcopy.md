# UI Microcopy: Action Controls, CLI Flags & Error Recovery

Guide recovery immediately. Interface copy must direct users toward resolution while respecting serial assistive technology.

---

## 1. The Error State Triad (Apple Attribution Theory)

System failures trigger anxiety. Clear error copy preserves human agency by stating the objective condition and offering an unambiguous path forward.

### The 3-Step Triad:
1. **Objective Reality (Headline):** A calm noun phrase identifies the condition without system jargon ("Billing Problem", NOT "Error 402: Card Declined").
2. **Bounded Stakes (Body):** A single declarative sentence explains what is affected ("To keep backups active, update your payment details.").
3. **Restorative Agency (Buttons):** An active verb button executes the resolution, paired with a safe deferral (`[Update Payment Method]` and `[Not Now]`). Never display a lone "OK" button on a failure.

### Blame Redirection Rules
- Bad: "You entered an invalid password."
- Good: "The password does not match our records."
- Bad: "You failed to supply a valid work email."
- Good: "Enter a work email address (name@company.com) to continue."

### Ban on Faux-Empathy
- Avoid interjections: Never use "Oops!" or "Uh-oh!" during system errors.
- Avoid hollow apologies: Never say "Sorry for the inconvenience." State the remedy directly.

---

## 2. Accessibility Constraints (VoiceOver & Screen Readers)

### 2.1 Serial Audio Linearity
Audio is strictly linear. Screen reader users experience interface text as a sequential audio stream that cannot be skimmed diagonally.
- **Priority Order:** Place the primary noun or verb in the first three words.
- **Eliminate Trait Duplication:** Screen readers announce programmatic element traits like button or link. Writing "Submit Button" causes VoiceOver to read: "Submit Button, button". Label buttons with the naked action: `Submit`.

### 2.2 Dynamic Type Truncation Survival
Extreme zoom truncates strings. Critical meaning must survive even when high magnification factors clip the final two words of a sentence.

---

## 3. Localization Constraints

1. **Expansion Buffer:** Translations into German or Finnish expand by up to 50% in physical length. Keep English source strings under 18 words to prevent UI overflow.
2. **Literal Verbs:** Figurative expressions fail in translation. Use direct operational verbs ("choose", "start").

---

## 4. UI Exemplars

### Confirmation Dialog
- **Header:** Delete Project "Atlas"?
- **Body:** This action deletes all associated environments, API keys, and deployment logs.
- **Buttons:** `[Delete Project]` (Destructive red) · `[Cancel]`

### Field Validation
- Bad: "Invalid input format detected."
- Good: "Use letters and numbers only."

---

## 5. CLI Microcopy: Flag Descriptions & Terminal Diagnostics

Command line interfaces require concise copy. Format terminal messages for rapid operator comprehension and automated parsing.

### 5.1 Flag Descriptions & Help Strings
- **Help Text Ceiling:** Cap flag descriptions at 12 words. Lead with an active imperative verb ("Specify target configuration path").
- **Kebab-Case Naming:** Use lowercase kebab-case for long flags (`--output-dir`) paired with single-letter shortcuts (`-o`).

### 5.2 Diagnostic & Error Messages
- **Diagnostic Stream:** Emit human-facing warnings, progress states, and diagnostic tracebacks to standard error (`stderr`). Keep machine output streams (`stdout`) free of conversational status text.
- **Actionable Recovery:** When commands fail with non-zero exit codes, pair the failure condition with a concrete recovery command or flag ("Pass --force to overwrite").
