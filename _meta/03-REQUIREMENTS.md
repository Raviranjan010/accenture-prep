# 03-REQUIREMENTS.md — Quality & Structure Bar

## Repo-wide rules
- Keep the top-level folder numbering convention (`00-` through `08-`).
- One concept = one file. Don't cram 10 topics into a single giant markdown file — it becomes unusable as a revision tool.
- Every file is self-contained: someone should be able to open just that file the night before the exam and get full value without hunting elsewhere.
- No topic file may be "concept only" — every single one needs worked examples + a PYQ bank + answer key. A formula sheet with zero practice questions is incomplete and should be flagged, not left as-is.
- Plain English first, jargon second. Assume the reader is revising at 11 PM and tired — no dense unexplained jargon dumps.

## Per-topic file skeleton (mandatory)
```
# Topic Name

## What this is
[1 paragraph, plain English]

## Formula / Rule / Pattern
[boxed/table]

## Shortcut
[the trick + WHY it works]

## Worked Examples
1. Easy — ...
2. Medium — ...
3. Hard — ...

## Practice Questions (PYQs)
Q1 ... Q25

## Answers
[at the end, or in topic-answers.md]

## Where this appears in the real Accenture test
[one line]

## Recommended videos
- [Title](url) — why watch this one
```

## Depth requirements
- Aptitude/reasoning/DI/abstract-reasoning topics: minimum 15 PYQs each.
- Pseudocode: minimum 20 problems with full trace tables shown.
- Coding round: minimum 10 problems per language, spanning easy/medium, with brute-force + optimized solution where relevant.
- Communication assessment: each of the 6 sections gets its own drill file with at least 10 practice items (sentences/scripts/stories as applicable).
- Gamified round: each game type gets a technique file + at least 5 practice scenarios described in text (since actual games can't run in markdown, describe the scenario and the optimal decision process).

## Things that must NOT happen
- Do not invent Accenture-specific "leaked" questions and present them as officially confirmed — label anything sourced from prep sites/forums as "commonly reported practice question," not "official question."
- Do not claim a fixed cutoff percentage — Accenture doesn't publish one, and it varies by drive. State this explicitly wherever cutoffs are discussed.
- Do not duplicate content that already exists well in the repo — extend it instead of rewriting from scratch, unless the existing version is factually outdated.
