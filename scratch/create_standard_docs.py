import os

# 1. ROADMAP.md
roadmap_content = """# Accenture Placement Preparation — Beginner's Learning Roadmap

Welcome to the **Accenture Placement Preparation Master Roadmap**. Whether you are starting with zero programming background or brushing up before campus recruitment, this guide outlines the exact learning order, prerequisites, difficulty progression, practice tracking, and week-by-week milestones across all 4 preparation tracks.

---

## 🧭 Where to Start

If you are unsure where to begin:
1. **Self-Diagnostic Assessment**: Start with **[01-Aptitude Module](01-aptitude/README.md)**. Quantitative reasoning and logical patterns build general analytical speed needed for all subsequent technical and non-technical rounds.
2. **Setup Readiness**: Skim **[05-logistics-checklist.md](05-logistics-checklist.md)** early to ensure your laptop, browser (Chrome 110+ / Secure Exam Browser), webcam, and environment meet Accenture's technical guidelines.

---

## 🛤️ Learning Order Across All 4 Tracks

Follow this sequential 4-track progression:

```
┌──────────────────────────────────────────────────────────┐
│ Track 1: Aptitude & Calculation Foundation               │
│ (Percentages -> TSD -> Ratios -> Logical -> Verbal)      │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Track 2: Technical CS Fundamentals & DSA Practice        │
│ (OOPs -> DBMS -> OS -> Networks -> Arrays/Strings -> DP) │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Track 3: Spoken Communication & Grammar Notes            │
│ (Grammar Rules -> Self-Intro -> Project Summary Pitch)   │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Track 4: Behavioral STAR & Project Deep-Dives            │
│ (STAR Stories -> Project Deep-Dives -> Panelist Qs)      │
└──────────────────────────────────────────────────────────┘
```

---

## 🔑 Prerequisites Per Track & Topic

To avoid getting stuck, adhere strictly to these topic prerequisites:

### Track 1: Aptitude (`01-aptitude/`)
- **Prerequisites**: Basic arithmetic (addition, multiplication, basic fractions).
- **Topic Order**:
  1. `quantitative/percentages-profit-loss.md` (Must come first—percentages are the base for ratios and data interpretation).
  2. `quantitative/ratios-averages.md` (Requires percentage concepts).
  3. `quantitative/time-speed-distance.md` (Requires ratio proportional reasoning).
  4. `logical-reasoning/coding-decoding.md` (Independent).
  5. `logical-reasoning/blood-relations.md` (Independent).
  6. `logical-reasoning/seating-arrangement.md` (Requires basic logical elimination).
  7. `verbal/reading-comprehension.md` & `verbal/para-jumbles.md` (Independent).

### Track 2: Technical & Coding (`02-technical-coding/`)
- **Prerequisites**:
  - `cs-fundamentals/oop-concepts.md`: Assumes **no prior programming knowledge**. Starts from absolute zero (variables, functions, objects).
  - `cs-fundamentals/dbms-normalization-joins.md`, `os-basics.md`, `networking-basics.md`: Assume completion of basic OOP/programming concepts.
  - `dsa-practice/arrays-strings.md`: **Prerequisite**: Basic OOP concepts (`oop-concepts.md`) and memory basics.
  - `dsa-practice/dp-graphs.md`: **Prerequisite**: Must complete `arrays-strings.md` first (requires comfort with loops, recursion, array indexing, and hashing).

### Track 3: Communication (`03-communication/`)
- **Prerequisites**: Basic English vocabulary.
- **Topic Order**: Start with `grammar-vocab-notes.md`, then practice `self-intro-script.md` and `project-summary-script.md`.

### Track 4: Interview Prep (`04-interview-prep/`)
- **Prerequisites**: Must complete Track 2 (`02-technical-coding/`) and Track 3 (`03-communication/`) to articulate technical architectural trade-offs confidently.

---

## 📈 Difficulty Progression Within Folders

Every topic and concept file in this repository strictly progresses through 3 levels:

1. **Foundational (Level 1 - Easy)**: Plain-language definitions, direct formula applications, basic 1-step examples.
2. **Intermediate (Level 2 - Medium)**: Combined rules, multi-step problem solving, moderate time pressure strategies.
3. **Advanced (Level 3 - Hard)**: Edge cases, complex real-world trade-offs, high-concurrency scenarios, and tricky placement questions.

---

## 📊 How to Use Practice Logs

This repository includes 4 dedicated tracking logs. Never skip logging after a study session:

1. **[01-aptitude/mock-test-logs.md](01-aptitude/mock-test-logs.md)**: Log date, test score, time taken, weak areas, and action fixes after every full or sectional aptitude mock.
2. **[02-technical-coding/dsa-practice/solved-problems-log.md](02-technical-coding/dsa-practice/solved-problems-log.md)**: Log every DSA problem solved on LeetCode/GFG along with time & space complexity.
3. **[03-communication/recorded-practice-log.md](03-communication/recorded-practice-log.md)**: Log audio/video self-recordings, noting filler words, pacing (WPM), and vocal clarity.
4. **[04-interview-prep/mock-interview-log.md](04-interview-prep/mock-interview-log.md)**: Record mock technical/HR interview responses and peer feedback.

---

## 🗓️ Week-by-Week Progress Self-Check

- [ ] **Week 1: Quantitative & Logical Aptitude**
  - Completed all 8 topic files under `01-aptitude/`.
  - Logged at least 2 mock tests in `mock-test-logs.md` with >75% accuracy.
- [ ] **Week 2: CS Core & Array/String Coding**
  - Revised OOPs, DBMS, OS, and Networking under `02-technical-coding/cs-fundamentals/`.
  - Solved 10+ Array/String coding problems and logged them in `solved-problems-log.md`.
- [ ] **Week 3: Advanced DSA & Communication Fluency**
  - Mastered DP & Graph basics (`dp-graphs.md`).
  - Recorded 5+ self-intro and project summary pitches in `recorded-practice-log.md`.
- [ ] **Week 4: STAR Stories, Project Deep-Dives & Logistics**
  - Finalized STAR answers and customized project deep-dives (`04-interview-prep/`).
  - Verified system readiness against `05-logistics-checklist.md`.

---

## 🔗 Quick Links to Section READMEs

- 📑 **[Track 1: 01-Aptitude README](01-aptitude/README.md)**
- 💻 **[Track 2: 02-Technical Coding README](02-technical-coding/README.md)**
- 🗣️ **[Track 3: 03-Communication README](03-communication/README.md)**
- 🎯 **[Track 4: 04-Interview Prep README](04-interview-prep/README.md)**
"""

with open('ROADMAP.md', 'w', encoding='utf-8') as f:
    f.write(roadmap_content)

# 2. TEACHING-STANDARD.md
teaching_standard_content = """# Repository Teaching Standard & Section Structure

To guarantee that every candidate—regardless of prior knowledge—can achieve complete mastery, every concept file in this repository MUST strictly follow the **14-Step Teaching Framework** detailed below.

---

## 📋 The 14 Mandatory Sections

Every concept guide must be organized using these exact 14 headers in sequential order:

### 1. What is it?
- A plain-language explanation of the concept written for an absolute beginner with zero background knowledge. Avoid dense jargon; use clear everyday analogies.

### 2. Why does it matter?
- Explanation of why this concept is critical for placement exams (e.g., Accenture assessment weightage) and real-world software engineering practice.

### 3. When to use it?
- Clear decision criteria, trigger keywords, and scenario indicators specifying exactly when this formula, rule, pattern, or data structure should be applied.

### 4. How it works
- The mechanical, step-by-step underlying process or execution flow (how the math compounds, how memory is allocated, or how data flows).

### 5. Key rules or syntax
- Complete mathematical formulas, code syntax, or logical axioms needed. Every formula MUST include a one-line explanation of *WHY* it works.

### 6. Simple example
- A basic, low-complexity example (Level 1 - Easy) demonstrating the direct application of the concept.

### 7. Detailed example
- A fully worked intermediate/advanced problem showing **every single intermediate step** without skipping math steps or code logic.

### 8. Practical use case
- A real-world production software engineering or industry scenario where this concept is actively implemented (e.g., database indexing, caching, rate limiting).

### 9. Common mistakes
- 2 to 3 specific errors candidates make on placement tests regarding this topic, explaining *why* they happen and how to avoid them.

### 10. Tips & tricks
- At least 3 exam-speed shortcuts, mental shortcuts, or time-saving strategies, featuring a direct **Shortcut vs. Long Method** comparison showing obvious time saved.

### 11. Practice exercises
- A minimum of 8 practice questions or coding problems ordered strictly in increasing difficulty (Easy $\rightarrow$ Medium $\rightarrow$ Hard).

### 12. Q&A with explanations
- Full, un-truncated step-by-step answer key and logical explanations for all 8 practice exercises.

### 13. Quick revision
- A bulleted, 60-second cheat-sheet summary containing core formulas, key syntax, and critical reminders for rapid pre-exam review.

### 14. Connection to next topic
- A logical bridging paragraph explaining how the current topic connects to and prepares the candidate for the next topic in the learning roadmap.
"""

with open('TEACHING-STANDARD.md', 'w', encoding='utf-8') as f:
    f.write(teaching_standard_content)

print("ROADMAP.md and TEACHING-STANDARD.md created successfully.")
