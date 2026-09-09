# 08-CLEANUP-CHANGELOG.md — Repository Restructuring Audit Log

This document provides a comprehensive audit trail of all file moves, directory renamings, file merges, and file deletions executed during the repository restructuring.

---

## 1. Folder Structure & Renaming Overview

| Old Folder Path | New Folder Path | Purpose / Description |
|:---|:---|:---|
| Root Level (`00-stage-0-...`, `05-logistics...`) | `00-start-here/` | Consolidated initial onboarding, eligibility, and exam logistics |
| `01-gamified-assessment/` | `01-gamified-assessment/` | Kept at `01-` position; renamed fallback cognitive MCQ file |
| `01-aptitude/` | `02-aptitude-reasoning/` | Renumbered to `02-` to resolve `01-` folder collision |
| `02-technical-coding/cs-fundamentals/`, `pseudocode/` | `03-technical-assessment/` | Separated CS theory and pseudocode into dedicated `03-` assessment section |
| `02-technical-coding/coding-round/`, `dsa-practice/` | `04-coding-round/` | Dedicated hands-on coding languages (`languages/`) & DSA practice (`dsa-practice/`) |
| `03-communication/` | `05-communication-assessment/` | Renumbered to `05-` to align with exam sequence |
| `04-interview-prep/` | `06-interview-prep/` | Renumbered to `06-` |
| `05-mock-tests/`, `06-capstone-mock-day.md` | `07-mock-tests/` | Consolidated all 3 mock tests, answers, and capstone protocol under `07-` |
| Multiple scattered `-log.md` & tracker files | `08-progress-trackers/` | Consolidated all student progress tracking logs under `08-` |
| Maintainer specification files at root | `_meta/` | Isolated all non-learner maintainer files in `_meta/` |

---

## 2. Detailed File Moves & Renames

### `00-start-here/`
- **Moved**: `00-stage-0-eligibility-resume.md` (root) $\rightarrow$ `00-start-here/01-eligibility-and-resume.md`
- **Moved**: `05-logistics-checklist.md` (root) $\rightarrow$ `00-start-here/02-logistics-checklist.md`

### `01-gamified-assessment/`
- **Renamed**: `cognitive-mcq-classic.md` $\rightarrow$ `04-classic-cognitive-mcq-fallback.md`

### `02-aptitude-reasoning/`
- **Moved**: `01-aptitude/README.md` $\rightarrow$ `02-aptitude-reasoning/README.md`
- **Moved**: `01-aptitude/quantitative/*` $\rightarrow$ `02-aptitude-reasoning/quantitative/*`
- **Moved**: `01-aptitude/logical-reasoning/*` $\rightarrow$ `02-aptitude-reasoning/logical-reasoning/*`
- **Moved**: `01-aptitude/verbal/*` $\rightarrow$ `02-aptitude-reasoning/verbal/*`

### `03-technical-assessment/`
- **Moved**: `02-technical-coding/cs-fundamentals/*` $\rightarrow$ `03-technical-assessment/cs-fundamentals/*`
- **Moved**: `02-technical-coding/pseudocode/*` $\rightarrow$ `03-technical-assessment/pseudocode/*`
- **Created**: `03-technical-assessment/README.md`

### `04-coding-round/`
- **Moved**: `02-technical-coding/coding-round/*` $\rightarrow$ `04-coding-round/languages/*`
- **Moved**: `02-technical-coding/dsa-practice/01-arrays-strings.md`, `02-dp-graphs.md` $\rightarrow$ `04-coding-round/dsa-practice/*`
- **Created**: `04-coding-round/README.md`

### `05-communication-assessment/`
- **Moved**: `03-communication/*` $\rightarrow$ `05-communication-assessment/*`

### `06-interview-prep/`
- **Moved**: `04-interview-prep/*` $\rightarrow$ `06-interview-prep/*`

### `07-mock-tests/`
- **Moved**: `05-mock-tests/01-mock-test-1.md` $\rightarrow$ `07-mock-tests/01-mock-test-1.md`
- **Moved**: `05-mock-tests/01-mock-test-1-answers.md` $\rightarrow$ `07-mock-tests/01-mock-test-1-answers.md`
- **Moved**: `05-mock-tests/02-mock-test-2.md` $\rightarrow$ `07-mock-tests/02-mock-test-2.md`
- **Moved**: `05-mock-tests/02-mock-test-2-answers.md` $\rightarrow$ `07-mock-tests/02-mock-test-2-answers.md`
- **Moved**: `05-mock-tests/03-mock-test-3.md` $\rightarrow$ `07-mock-tests/03-mock-test-3.md`
- **Moved**: `05-mock-tests/03-mock-test-3-answers.md` $\rightarrow$ `07-mock-tests/03-mock-test-3-answers.md`
- **Moved**: `06-capstone-mock-day.md` (root) $\rightarrow$ `07-mock-tests/04-capstone-mock-day.md`

### `08-progress-trackers/`
- **Merged**: `01-aptitude/mock-test-logs.md` + `05-mock-tests/score-tracker.md` $\rightarrow$ `08-progress-trackers/01-aptitude-mock-score-tracker.md`
- **Moved**: `02-technical-coding/dsa-practice/solved-problems-log.md` $\rightarrow$ `08-progress-trackers/02-dsa-solved-problems-log.md`
- **Moved**: `03-communication/recorded-practice-log.md` $\rightarrow$ `08-progress-trackers/03-spoken-practice-log.md`
- **Moved**: `04-interview-prep/04-mock-interview-log.md` $\rightarrow$ `08-progress-trackers/04-mock-interview-log.md`

### `_meta/`
- **Moved**: `00-MASTER-PROMPT.md` (root) $\rightarrow$ `_meta/00-MASTER-PROMPT.md`
- **Moved**: `10-AUDIT.md` (root) $\rightarrow$ `_meta/10-AUDIT.md`
- **Moved**: `07-CLEANUP-AND-REORG-PLAN.md` (root) $\rightarrow$ `_meta/07-CLEANUP-AND-REORG-PLAN.md`
- **Moved**: `02-COVERAGE-CHECKLIST.md` (root) $\rightarrow$ `_meta/02-COVERAGE-CHECKLIST.md`
- **Moved**: `03-REQUIREMENTS.md` (root) $\rightarrow$ `_meta/03-REQUIREMENTS.md`
- **Moved**: `06-RESOURCE-LINKS.md` (root) $\rightarrow$ `_meta/06-RESOURCE-LINKS.md`
- **Moved**: `09-ROADMAP.md` (root) $\rightarrow$ `_meta/09-ROADMAP.md`
- **Moved**: `04-TEACHING-STANDARD.md` (root) $\rightarrow$ `_meta/04-TEACHING-STANDARD.md`
- **Moved**: `01-TOPICS-TO-COVER.md` (root) $\rightarrow$ `_meta/01-TOPICS-TO-COVER.md`
- **Moved**: `05-TRICKS-AND-SHORTCUTS.md` (root) $\rightarrow$ `_meta/05-TRICKS-AND-SHORTCUTS.md`
- **Created**: `_meta/README.md` (Explaining maintainer scope)

### Root Level
- **Created**: `ADDITIONAL-RESOURCES.md` (General practice platforms: IndiaBix, LeetCode, GfG, etc.)
- **Updated**: `README.md` (Full 00–08 TOC, disclaimers, 7-day sprint & 30-day plans)
- **Updated**: `CHEAT-SHEET.md` (Updated relative markdown links to match new folder paths)

---

## 3. Files & Directories Deleted (Deduplicated)

- **Deleted Root Files**:
  - `00-MASTER-PROMPT.md`
  - `00-stage-0-eligibility-resume.md`
  - `05-logistics-checklist.md`
  - `06-capstone-mock-day.md`
  - `10-AUDIT.md`
  - `07-CLEANUP-AND-REORG-PLAN.md`
  - `02-COVERAGE-CHECKLIST.md`
  - `03-REQUIREMENTS.md`
  - `06-RESOURCE-LINKS.md`
  - `09-ROADMAP.md`
  - `04-TEACHING-STANDARD.md`
  - `01-TOPICS-TO-COVER.md`
  - `05-TRICKS-AND-SHORTCUTS.md`
  - `resources.md` (Merged into `ADDITIONAL-RESOURCES.md` and `_meta/06-RESOURCE-LINKS.md`)
- **Deleted Redundant Tracking / Duplicate Files**:
  - `01-aptitude/mock-test-logs.md` (Merged)
  - `05-mock-tests/score-tracker.md` (Merged)
  - `03-communication/recorded-practice-log.md` (Renamed/moved to `08-progress-trackers/03-spoken-practice-log.md`)
  - `04-interview-prep/04-mock-interview-log.md` (Moved to `08-progress-trackers/04-mock-interview-log.md`)
  - `01-gamified-assessment/cognitive-mcq-classic.md` (Renamed)
- **Deleted Empty Directories**:
  - `01-aptitude/`
  - `02-technical-coding/`
  - `03-communication/`
  - `04-interview-prep/`
  - `05-mock-tests/`
