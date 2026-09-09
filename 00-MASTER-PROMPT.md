# MASTER PROMPT — Paste this into Antigravity IDE

> Attach `REQUIREMENTS.md`, `TOPICS-TO-COVER.md`, `RESOURCE-LINKS.md`, and
> `TRICKS-AND-SHORTCUTS.md` (all in this folder) to the IDE's context along with
> this prompt, then run it against the existing `accenture-prep` repo.

---

You are acting as a senior placement-prep content architect and technical writer.
Your job is to upgrade my existing repository, **`accenture-prep`**, into a complete,
self-contained, master-level preparation resource for the **Accenture 2026 hiring
process** (ASE / Advanced ASE tracks, on-campus and off-campus).

I am giving you four reference files in this same folder — treat them as your
source of truth and follow them exactly:

1. `REQUIREMENTS.md` — the structural/quality bar every file you create must meet.
2. `TOPICS-TO-COVER.md` — the full syllabus, section by section, that the repo must cover with nothing missing.
3. `RESOURCE-LINKS.md` — curated YouTube videos, playlists, and practice-tool links to embed in the right topic files.
4. `TRICKS-AND-SHORTCUTS.md` — the shortcut/technique content that must appear inline in the relevant topic files, not just linked externally.

## Your task

1. **Audit first.** Read the existing repo structure fully. Produce a short gap
   report (as `AUDIT.md`) listing: what already exists, what's incomplete, and
   what's completely missing, mapped against `TOPICS-TO-COVER.md`. Do this before
   writing new content so nothing gets duplicated.

2. **Fill every gap** identified in the audit and in `TOPICS-TO-COVER.md`. For each
   topic/subtopic that's missing or thin, create a properly named markdown file
   inside the correct existing folder (or a new folder if the topic doesn't have
   a home yet — follow the existing repo's naming convention, e.g. `NN-kebab-case/`).

3. **Every topic file must contain, in this order:**
   - A one-paragraph plain-English explanation of the concept (no jargon dumps).
   - The formula/rule/pattern, boxed or highlighted, with a **shortcut/trick**
     pulled from `TRICKS-AND-SHORTCUTS.md` (or one you derive in the same spirit
     if not listed there) — explain *why* the shortcut works, not just the steps.
   - 3–5 **worked examples**, fully solved step by step, ordered easy → hard.
   - A **PYQ (Previous Year / Practice Question) bank** of at least 15–25
     questions per topic, each with a final answer key (answers in a separate
     collapsible/appendix section or a matching `-answers.md` file, not inline
     right after the question, so it can be used as a real timed test).
   - A **"Where this shows up in the real test"** one-liner (e.g. "Appears in the
     Quick-Fire Math game" or "Tested via the pseudocode trace-table section").
   - A **Recommended videos** section at the bottom with the specific links from
     `RESOURCE-LINKS.md` that match this topic, each with a one-line note on what
     to watch it for.

4. **Cover the full pipeline end-to-end**, not just the written test. That means
   folders/files for: Gamified Assessment, Technical Assessment (CS fundamentals
   + pseudocode + networking/cloud/security + MS Office), Coding Round (per
   language: C/C++/Java/Python/SQL/JS), Communication Assessment (all 6 sections
   individually drilled), and the HR/Managerial interview + Group Discussion round.

5. **Add a master index.** Update the root `README.md` with a full table of
   contents linking every file, a suggested day-by-day study plan (assume the
   user has anywhere from 7 to 30 days — build both a "7-Day Sprint" and a
   "30-Day Full Prep" plan as separate tables), and a section-wise scoring/cutoff
   note (with the explicit caveat that Accenture doesn't publish official
   cutoffs and patterns vary by drive).

6. **Add a mock-test generator folder** (`05-mock-tests/`) with at least 3 full
   timed mock papers assembled from the PYQ banks (mix of sections, matching the
   real time limits), plus an answer key file for each, plus a blank score-tracking
   template (markdown table: date, mock #, section, score, time taken, mistakes to review).

7. **Never claim any file "guarantees" a 100% score or guaranteed selection.**
   In the root README, include an honest disclaimer: real performance also
   depends on practice volume/speed, actual test-day pattern (which can vary by
   drive/date), and interview delivery — this repo is a preparation aid, not a guarantee.

8. **Formatting standards:** consistent markdown headers (`##` for topic name,
   `###` for subsections), tables for formula sheets, fenced code blocks for
   pseudocode/coding examples, and a consistent PYQ format:
   ```
   Q1. [question text]
   a) ... b) ... c) ... d) ...
   ```
   with answers collected at the bottom of the file or in a paired `-answers.md`.

9. **Do not fabricate links.** Only use URLs given in `RESOURCE-LINKS.md`. If you
   believe a topic needs a video and none is listed, add a `TODO: find video for
   [topic]` note instead of inventing a URL.

10. **Final deliverable:** a fully updated repo, plus a top-level
    `COVERAGE-CHECKLIST.md` that lists every syllabus item from
    `TOPICS-TO-COVER.md` with a ✅/❌ next to it, so completeness can be verified
    at a glance.

Work through this systematically, folder by folder, and don't stop until every
item in `TOPICS-TO-COVER.md` is either ✅ covered or explicitly flagged as a TODO
with a reason (e.g. "needs a real recorded audio sample, can't be markdown-only").
