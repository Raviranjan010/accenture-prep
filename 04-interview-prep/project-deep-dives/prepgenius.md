# Project Deep Dive: PrepGenius (AI Mock Interview Platform)

## 1. Structured Project Overview

- **Problem It Solves**: AI-powered mock interview platform that reduces student preparation time by 35% for over 200+ users via smart question generation and adaptive workflows.
- **My Role**: [FILL IN: Describe your exact role, e.g., Lead Developer, Full-Stack Developer]
- **Tech Stack**:
  - *Frontend & Build*: React, TypeScript, Vite, Tailwind CSS
  - *Authentication*: Clerk
  - *Database & Storage*: Firebase Firestore
  - *AI Integration*: Google Gemini API
  - *Code Editor*: Monaco Editor
- **Key Features Verified**:
  - Resume & Job Description (JD) parsing for custom question targeting.
  - Adaptive interview question generation based on user performance.
  - Live coding workspace with time/space complexity evaluation.
  - System-design interactive whiteboard module.
  - Comprehensive architecture and scalability feedback reports.
- **One Hard Technical Problem I Solved**:
  - *Problem*: [FILL IN: Describe a real technical challenge faced during development]
  - *Solution*: [FILL IN: Describe the steps you took to resolve the issue]
  - *Metrics*: Reduced preparation time by 35% across 200+ active users.
- **What I'd Improve in v2.0**:
  - [FILL IN: Mention planned future enhancements]

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "How did you structure prompts for Google Gemini to deliver adaptive question generation and code feedback?"
- **Guidance on How to Answer**:
  - Explain how candidate inputs (resume details, target JD, previous answer scores) were passed in structured system prompts to Google Gemini.
  - Discuss how you constrained Gemini to return structured JSON payloads so the React UI could reliably render complexity feedback and follow-up questions.

### Q2: "Why did you choose Firebase Firestore and Clerk for this application?"
- **Guidance on How to Answer**:
  - Clerk provided instant, secure user authentication with multi-provider OAuth out of the box, reducing auth implementation overhead.
  - Firebase Firestore provided flexible NoSQL real-time document synchronization for storing user interview sessions, scoring histories, and resume metadata.

### Q3: "How does the live coding module with Monaco Editor evaluate time and space complexity?"
- **Guidance on How to Answer**:
  - The browser client captures code written in Monaco Editor and passes the code string along with test cases to the Google Gemini API for static/algorithmic analysis.
  - Explain how Gemini analyzes the asymptotic behavior ($O(N)$, $O(N \log N)$) and provides targeted refactoring suggestions directly back to the code editor.
