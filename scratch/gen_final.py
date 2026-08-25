import os

# 1. 05-logistics-checklist.md
logistics_content = """# Accenture Assessment & Interview Logistics Checklist

A comprehensive pre-test and pre-interview operational checklist based on Accenture's official hiring platform guidelines (Mettl / CoCubes / HirePro platforms). Complete all checks to prevent system disqualification or technical interruptions during the live assessment.

---

## 📅 Day Before the Assessment / Interview

### System & Hardware Specifications
- [ ] **Operating System**: Windows 10/11 (64-bit) or macOS 10.15+ (Linux/Ubuntu is NOT supported).
- [ ] **RAM & Processor**: Minimum 4 GB RAM (8 GB recommended) with Dual-Core 2.0 GHz or higher processor.
- [ ] **Primary Browser**: Google Chrome (v110+ updated to latest version) or MS Edge. Clear browser cache and cookies.
- [ ] **Secure Exam Browser (SEB)**: Download and complete test-run installation of the platform's proprietary lock-down browser if required by the test email link.
- [ ] **Webcam & Microphone Check**: Functional HD webcam (720p+) and built-in or wired microphone. Test audio/video clarity at [webcammictest.com](https://webcammictest.com/).

### Network & Environment Setup
- [ ] **Internet Bandwidth**: Stable broadband/fiber connection with minimum **2 Mbps continuous speed** (5 Mbps+ recommended). Have a mobile hotspot ready as an instant backup.
- [ ] **Browser Settings**: Enable Pop-ups and Redirects for the assessment domain; allow Camera & Microphone permissions.
- [ ] **Antivirus & Firewall**: Temporarily disable third-party antivirus auto-scans or web shields (e.g., Avast, McAfee, Kaspersky) that block WebRTC connections.
- [ ] **Power Backup**: Laptop fully charged to 100% and connected to a uninterrupted power outlet/UPS.

### Identity & Documentation
- [ ] **Government Photo ID**: Physical original **PAN Card** (or e-PAN with clear photo) or Aadhaar Card placed on desk.
- [ ] **Admit Card / Registration Email**: Printed or digital copy of official Accenture registration confirmation containing Candidate ID.

---

## ⏰ 30 Minutes Before the Assessment / Interview

### Environment & Privacy Setup
- [ ] **Quiet Private Room**: Isolated room with door closed. Ensure zero background noise, TV sounds, or family members walking past.
- [ ] **Lighting Setup**: Primary light source positioned in front of your face (facing a window or desk lamp). Avoid strong backlighting that turns your video into a silhouette.
- [ ] **Desk Clearance**: Remove all extraneous books, unauthorized second monitors, papers, smartwatch, and headphones (unless wired headset is explicitly permitted).
- [ ] **Phone & Notifications**: Set mobile phone to **Silent / Do Not Disturb** mode and place it out of arm's reach (only usable for hotspot emergency).

### Technical Warm-Up
- [ ] **Close Background Apps**: Force-close Discord, Telegram, WhatsApp Web, Slack, Zoom, TeamViewer, AnyDesk, and IDE background watchers.
- [ ] **System Diagnostics**: Run the automated platform hardware test link provided in your Accenture invitation email.
- [ ] **Login & Verification**: Log into the test portal 15 minutes before start time; keep your photo ID ready for webcam verification scanning.
"""

with open('05-logistics-checklist.md', 'w', encoding='utf-8') as f:
    f.write(logistics_content)

# 2. resources.md
resources_content = """# Curated Free Preparation Resources

A handpicked, categorized directory of top-tier, reputable free platforms and websites for placement preparation, specific to the Accenture recruitment pattern.

---

## 1. Quantitative & Logical Aptitude

- **[IndiaBix](https://www.indiabix.com/)** — *Best for*: Topic-wise fundamental practice questions with step-by-step solutions for Quantitative, Logical, and Verbal ability.
- **[PrepInsta](https://prepinsta.com/accenture/)** — *Best for*: Accenture-specific previous year question papers, exam pattern breakdowns, and sectional time limits.
- **[Face Prep](https://www.faceprep.in/accenture/)** — *Best for*: High-yield aptitude shortcut tutorials and placement diagnostic mock tests.
- **[Sanfoundry](https://www.sanfoundry.com/)** — *Best for*: Harder MCQs on computer science fundamentals and quantitative reasoning.

---

## 2. Technical Coding & Computer Science

- **[LeetCode](https://leetcode.com/)** — *Best for*: Practicing Easy-to-Medium array, string, and dynamic programming problems (Filter by tags: Array, Two Pointers, String).
- **[GeeksforGeeks](https://www.geeksforgeeks.org/)** — *Best for*: Comprehensive tutorials on Data Structures, Algorithms, OOPs concepts, DBMS joins, OS, and Computer Networks.
- **[InterviewBit](https://www.interviewbit.com/)** — *Best for*: Timed coding practice with memory and time complexity hints tailored for tech placement drives.
- **[SQLZoo](https://sqlzoo.net/)** — *Best for*: Interactive, browser-based SQL query practice covering joins, aggregations, and subqueries.

---

## 3. Communication & Verbal Ability

- **[British Council LearnEnglish](https://learnenglish.britishcouncil.org/)** — *Best for*: Grammar rules, preposition usage exercises, and listening comprehension drills.
- **[Grammarly Blog](https://www.grammarly.com/blog/)** — *Best for*: Quick reference guides on subtle subject-verb agreement rules and common vocabulary confusions.
- **[Versant Practice Tests on YouTube](https://www.youtube.com/)** — *Best for*: Listening to sample automated voice audio snippets to prepare for sentence repetition and passage retelling.

---

## 4. Mock Interviews & Behavioral Prep

- **[Pramp / Exponent](https://www.pramp.com/)** — *Best for*: Free peer-to-peer live mock technical and behavioral interviews.
- **[Big Interview Blog](https://biginterview.com/blog/)** — *Best for*: In-depth STAR framework guides and behavioral question breakdown templates.
- **[Glassdoor Accenture Interview Reviews](https://www.glassdoor.co.in/)** — *Best for*: Reading recent candidate interview experiences, HR questions, and interview panel feedback for Accenture India.
"""

with open('resources.md', 'w', encoding='utf-8') as f:
    f.write(resources_content)

# 3. Top-Level README.md
toplevel_readme = """# Accenture Placement Preparation Repository

Welcome to the comprehensive, self-contained **Accenture Placement Preparation Master Repository**. This repository is engineered specifically for B.Tech Computer Science candidates (tailored for **Ravi Ranjan**, B.Tech CS at LPU specializing in Full-Stack Web Development & AI-ML) preparing for the upcoming Accenture campus recruitment drive.

---

## 🎯 Purpose of This Repository

Accenture's campus recruitment process consists of rigorous automated assessments and multi-stage technical/HR interviews:
1. **Cognitive & Technical Assessment**: Aptitude (Quant, Logical, Verbal), CS Fundamentals (Pseudocode, DBMS, OS, Networking).
2. **Coding Assessment**: 2 Hands-on Data Structures & Algorithm problems.
3. **Communication Assessment**: Automated spoken English, listening, and sentence repetition evaluation (Versant style).
4. **Technical & HR Interview**: Project deep-dives, behavioral STAR questions, and core CS fundamentals.

This repository provides structured, zero-placeholder study content, shortcuts, practice questions, script templates, and tracking logs across all 4 preparation tracks.

---

## 📌 The 4-Track Structure Explained

The repository is organized into 4 core preparation tracks plus operational logistics and resources:

```
accenture-prep/
├── 01-aptitude/           → Track 1: Quantitative, Logical Reasoning, and Verbal Ability
├── 02-technical-coding/   → Track 2: CS Fundamentals (OOPs, DBMS, OS, CN) & DSA Practice
├── 03-communication/      → Track 3: Grammar, Versant Practice, Self-Intro & Project Scripts
├── 04-interview-prep/     → Track 4: STAR Behavioral Answers, Project Deep-Dives & Panelist Qs
├── 05-logistics-checklist.md → Technical hardware, SEB browser, PAN card & room environment setup
└── resources.md          → Categorized free preparation websites & practice links
```

---

## 🗓️ Suggested Master Timeline (4-Week Prep Plan)

Follow this structured 4-week timeline to systematically cover all tracks before your placement drive:

### Week 1: Aptitude & Core Calculation Speed (Track 1)
- **Goal**: Master all 8 quantitative, logical, and verbal topics under `01-aptitude/`.
- **Daily Budget**: 90 minutes (45m concept & shortcuts, 45m practice questions).
- **Milestone**: Log first 2 mock tests in `01-aptitude/mock-test-logs.md`.

### Week 2: Technical CS Fundamentals & Core DSA (Track 2)
- **Goal**: Revise OOPs, DBMS normalization/joins, OS basics, Networking, and solve array/string DSA problems under `02-technical-coding/`.
- **Daily Budget**: 120 minutes (60m CS fundamentals review, 60m coding practice).
- **Milestone**: Record solved problems in `02-technical-coding/dsa-practice/solved-problems-log.md`.

### Week 3: Communication Assessment & Spoken Scripts (Track 3)
- **Goal**: Practice spoken English daily, memorize grammar rules, and record self-intro & project summary pitches under `03-communication/`.
- **Daily Budget**: 30 minutes (15m self-recording, 15m grammar notes).
- **Milestone**: Log practice sessions in `03-communication/recorded-practice-log.md`.

### Week 4: Interview Deep-Dives & Mock Rounds (Track 4 & Logistics)
- **Goal**: Finalize STAR stories for hackathon win/teamwork/conflict, prepare project deep-dives for *Bhookly*, *PrepGenius*, and *Scrutin* under `04-interview-prep/`, and perform system checks in `05-logistics-checklist.md`.
- **Daily Budget**: 90 minutes (45m project deep-dive review, 45m live mock interviews).
- **Milestone**: Complete system diagnostic run 24h before test day.

---

## 🔗 Master Module Directory & Checklist

- [ ] **Track 1**: [01-Aptitude Module Index](01-aptitude/README.md)
- [ ] **Track 2**: [02-Technical Coding Module Index](02-technical-coding/README.md)
- [ ] **Track 3**: [03-Communication Module Index](03-communication/README.md)
- [ ] **Track 4**: [04-Interview Prep Module Index](04-interview-prep/README.md)
- [ ] **Logistics**: [05-Logistics Checklist](05-logistics-checklist.md)
- [ ] **Resources**: [Free Preparation Resources Directory](resources.md)
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(toplevel_readme)

print("Generated 05-logistics-checklist.md, resources.md, and top-level README.md successfully.")
