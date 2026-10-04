#!/usr/bin/env python3
"""
Standalone Writing Systems Linter (Zero External Dependencies).
Validates Markdown files against:
1. Sentence word ceilings (warns > 25 words).
2. Canonical 13-token AI slop word registry in prose (code blocks and backticks excluded).
3. Cadence variance in expository prose (lists and tables excluded).
"""

import sys
import re
from pathlib import Path

# Canonical 13-token registry + em-dash
BANNED_SLOP = [
    r"\bdelve\b",
    r"\bdelve into\b",
    r"\bleverage\b",
    r"\brobust\b",
    r"\bseamless\b",
    r"\bseamlessly\b",
    r"\btapestry\b",
    r"\bbeacon\b",
    r"\bpivotal\b",
    r"\bcrucial\b",
    r"\btestament\b",
    r"\blandscape\b",
    r"\bthis matters because\b",
    r"—"  # Em-dash pause
]

def clean_inline_prose(text: str) -> str:
    """Removes inline code and markdown link URLs to prevent false positives."""
    # Remove inline backticked code
    text = re.sub(r"`[^`]*?`", "", text)
    # Remove markdown link URLs: [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    return text

def split_into_sentences(text: str):
    """Splits a block of text into sentences, protecting common abbreviations."""
    # Protect abbreviations from splitting
    text = re.sub(r"\be\.g\.", "eg_token", text)
    text = re.sub(r"\bi\.e\.", "ie_token", text)
    raw_sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    clean_sentences = []
    for s in raw_sentences:
        s_clean = s.replace("eg_token", "e.g.").replace("ie_token", "i.e.").strip()
        words = s_clean.split()
        if len(words) >= 3:
            clean_sentences.append((s_clean, len(words)))
    return clean_sentences

def check_file(filepath: Path):
    print(f"\n[AUDITING] {filepath}")
    lines = filepath.read_text(encoding="utf-8").splitlines()
    errors = 0
    warnings = 0

    # 1. Slop Check & Block Parsing
    in_code_block = False
    
    # Store blocks: (block_type, start_line_num, text)
    # block_type is either 'expository' or 'list_item'
    blocks = []
    current_block_type = None
    current_block_lines = []
    current_block_start = 1

    def flush_block():
        nonlocal current_block_type, current_block_lines, current_block_start
        if current_block_lines:
            block_text = " ".join(current_block_lines).strip()
            if block_text:
                blocks.append((current_block_type, current_block_start, block_text))
            current_block_lines = []
        current_block_type = None

    # Skip YAML frontmatter at start of file
    start_idx = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start_idx = i + 1
                break

    for idx, line in enumerate(lines[start_idx:], start=start_idx + 1):
        stripped = line.strip()

        # Handle fenced code blocks
        if stripped.startswith("```"):
            flush_block()
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Check for banned slop on non-code lines
        cleaned_line = clean_inline_prose(line)
        for pattern in BANNED_SLOP:
            for match in re.finditer(pattern, cleaned_line, re.IGNORECASE):
                print(f"  ❌ ERROR (Line {idx}): Banned AI pattern detected -> '{match.group(0)}'")
                errors += 1

        # Skip headers, table rows, and horizontal rules
        if not stripped or stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("---"):
            flush_block()
            continue

        # Check for list items or blockquotes
        is_list = bool(re.match(r"^[-*+>]\s+", stripped) or re.match(r"^\d+\.\s+", stripped))
        if is_list:
            flush_block()
            current_block_type = "list_item"
            current_block_start = idx
            # Strip list marker
            content = re.sub(r"^[-*+>]\s+", "", stripped)
            content = re.sub(r"^\d+\.\s+", "", content)
            current_block_lines.append(content)
        else:
            # Continuation of list item or regular expository paragraph
            if current_block_type == "list_item" and (line.startswith("  ") or line.startswith("\t")):
                current_block_lines.append(stripped)
            else:
                if current_block_type != "expository":
                    flush_block()
                    current_block_type = "expository"
                    current_block_start = idx
                current_block_lines.append(stripped)

    flush_block()

    # 2. Sentence Length & Structure Verification
    all_sentence_lengths = []
    expository_data = []  # list of (s_text, word_count, start_line)

    for block_type, start_line, text in blocks:
        clean_text = clean_inline_prose(text)
        sentences = split_into_sentences(clean_text)
        for s_text, word_count in sentences:
            all_sentence_lengths.append(word_count)
            if block_type == "expository":
                expository_data.append((s_text, word_count, start_line))

            if word_count > 25:
                snippet = s_text[:60] + "..." if len(s_text) > 60 else s_text
                print(f"  ⚠️  WARNING (Line ~{start_line}): Sentence exceeds 25 words ({word_count} words): '{snippet}'")
                warnings += 1

    # 3. Cadence & Rhythm Verification (Expository Prose Only)
    if len(expository_data) >= 4:
        lengths = [w for _, w, _ in expository_data]
        avg_len = sum(lengths) / len(lengths)
        variance = sum((l - avg_len) ** 2 for l in lengths) / len(lengths)
        std_dev = variance ** 0.5
        print(f"  📊 METRICS: Expository Sentences: {len(lengths)} | Avg: {avg_len:.1f}w | StdDev: {std_dev:.1f}")

        # Detect monotone runs: 4 or more consecutive sentences within +/- 2 words of each other
        monotone_found = False
        for i in range(len(lengths) - 3):
            window = lengths[i:i+4]
            if max(window) - min(window) <= 2:
                line_no = expository_data[i][2]
                print(f"  ⚠️  WARNING (Line ~{line_no}): Monotone rhythm detected ({window} words in consecutive sentences). Introduce cadence variance.")
                warnings += 1
                monotone_found = True
                break
    else:
        print(f"  📊 METRICS: Total Sentences: {len(all_sentence_lengths)} | Expository: {len(expository_data)} (Exempt from cadence check, < 4 expository sentences)")

    return errors, warnings

def main():
    if len(sys.argv) < 2:
        target_dir = Path("docs")
        files = list(target_dir.glob("*.md")) if target_dir.exists() else []
    else:
        files = [Path(p) for p in sys.argv[1:]]

    if not files:
        print("No markdown files found to check.")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0
    for f in files:
        if f.is_file() and f.suffix == ".md":
            err, warn = check_file(f)
            total_errors += err
            total_warnings += warn

    print("\n" + "=" * 50)
    print(f"AUDIT COMPLETE: {total_errors} errors, {total_warnings} warnings.")
    if total_errors > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
