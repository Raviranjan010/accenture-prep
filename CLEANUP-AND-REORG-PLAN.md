# CLEANUP-AND-REORG-PLAN.md

This is the exact restructuring to apply to the current repo. Follow the
mapping table below precisely — merge content when two old files map to one
new file, don't just copy-paste-duplicate.

## Target folder structure (final, learner-facing)

```
README.md                     — single entry point: what this repo is, full TOC, 2026 pattern note, 7-day & 30-day plans
CHEAT-SHEET.md                — master one-page shortcut/formula sheet (quick pre-exam scan)
ADDITIONAL-RESOURCES.md       — external practice platforms (IndiaBix, LeetCode, GfG, etc.)

00-start-here/
  01-eligibility-and-resume.md
  02-logistics-checklist.md

01-gamified-assessment/
  memory-maze.md
  path-finder.md
  quick-fire-math.md
  classic-cognitive-mcq-fallback.md      (renamed from cognitive-mcq-classic.md)

02-aptitude-reasoning/
  README.md
  quantitative/  (percentages-profit-loss, ratios-averages, time-speed-distance, data-interpretation)
  logical-reasoning/  (coding-decoding, blood-relations, seating-arrangement, abstract-visual-reasoning)
  verbal/  (reading-comprehension, para-jumbles)

03-technical-assessment/
  README.md
  cs-fundamentals/  (oop-concepts, dbms-normalization-joins, os-basics, networking-basics, cloud-security-basics, ms-office-basics)
  pseudocode/  (pseudocode-loop-recursion, pseudocode-array-string-flowchart)

04-coding-round/
  README.md
  dsa-practice/  (arrays-strings, dp-graphs)   [solved-problems-log.md MOVED OUT — see 08]
  languages/  (c-coding, cpp-coding, java-coding, python-coding, javascript-coding, sql-queries)

05-communication-assessment/
  README.md
  versant-drills/  (01-reading through 06-spontaneous-speech)
  grammar-vocab-notes.md
  self-intro-script.md
  project-summary-script.md
  [recorded-practice-log.md MOVED OUT — see 08]

06-interview-prep/
  README.md
  technical-interview-guide.md
  hr-managerial-guide.md
  group-discussion-guide.md
  questions-to-ask-panelist.md
  star-answers/  (teamwork, conflict-challenge, hackathon-win)
  project-deep-dives/  (bhookly, prepgenius, scrutin)
  [mock-interview-log.md MOVED OUT — see 08]

07-mock-tests/
  mock-test-1.md + mock-test-1-answers.md
  mock-test-2.md + mock-test-2-answers.md
  mock-test-3.md + mock-test-3-answers.md
  capstone-mock-day.md   (moved from root 06-capstone-mock-day.md)

08-progress-trackers/
  aptitude-mock-score-tracker.md   (MERGE 01-aptitude/mock-test-logs.md + 05-mock-tests/score-tracker.md — one table, dedupe rows)
  dsa-solved-problems-log.md       (moved from 02-technical-coding/dsa-practice/solved-problems-log.md)
  spoken-practice-log.md           (moved from 03-communication/recorded-practice-log.md)
  mock-interview-log.md            (moved from 04-interview-prep/mock-interview-log.md)

_meta/                             (maintainer-only files, NOT part of the learner nav — add a one-line README.md inside saying so)
  AUDIT.md
  COVERAGE-CHECKLIST.md
  REQUIREMENTS.md
  TOPICS-TO-COVER.md
  TRICKS-AND-SHORTCUTS.md
  RESOURCE-LINKS.md
  TEACHING-STANDARD.md
  00-MASTER-PROMPT.md              (v1, keep as build history)
  00-MASTER-PROMPT-V2.md           (this cleanup pass, once run)
```

## Explicit merge instructions

- **`resources.md` + `RESOURCE-LINKS.md`** → split by audience:
  - General external practice platforms (IndiaBix, LeetCode, GfG, InterviewBit, PrepInsta, etc.) → new root file `ADDITIONAL-RESOURCES.md`.
  - Accenture-specific YouTube videos/playlists used inline in topic files → stays as `_meta/RESOURCE-LINKS.md` (source-of-truth list, not learner-facing on its own since the links are already embedded in each topic file's "Recommended videos" section).
  - Delete the old `resources.md` after merging — do not leave both.

- **`01-aptitude/mock-test-logs.md` + `05-mock-tests/score-tracker.md`** → one file, `08-progress-trackers/aptitude-mock-score-tracker.md`. Combine all existing rows from both (don't lose the sample rows), keep one table schema, keep blank template rows at the bottom.

- **`06-capstone-mock-day.md`** (currently sitting alone at repo root) → move into `07-mock-tests/capstone-mock-day.md` since it's conceptually a mock test, not a standalone top-level stage.

- **`05-logistics-checklist.md`** (root) → move into `00-start-here/02-logistics-checklist.md`.

## README.md rewrite requirements

The root `README.md` must be rewritten (not just have links added) to:
1. Open with the honest disclaimer (no repo guarantees 100% marks; patterns vary by drive).
2. Give the full folder TOC in the exact order above — this order IS the recommended study sequence, so number folders `00 → 08` and tell the reader to move through them in order.
3. Include both a 7-Day Sprint plan and a 30-Day Full Prep plan as tables, referencing the new folder paths.
4. Link `CHEAT-SHEET.md` and `ADDITIONAL-RESOURCES.md` prominently near the top as "quick access" items usable at any stage.
5. Note that `_meta/` is for maintainers/repo builders only and can be ignored by someone just studying.

## Verification pass (do this after reorganizing, before finishing)

- Re-open every file in `02-aptitude-reasoning/`, `03-technical-assessment/`, `04-coding-round/`, `05-communication-assessment/` and confirm each still follows the full template from `_meta/REQUIREMENTS.md` (explanation → formula/shortcut → worked examples → PYQ bank → answers → "where it appears" → recommended videos). Flag any file missing a section instead of silently leaving it incomplete.
- Confirm no broken relative links after the folder moves (any internal markdown links referencing old paths must be updated to new paths).
- Confirm `_meta/COVERAGE-CHECKLIST.md` is updated to reflect the new file paths and still shows ✅/❌ per syllabus item from `_meta/TOPICS-TO-COVER.md`.
