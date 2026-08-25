import os

# 1. bhookly.md
bhookly_content = """# Project Deep Dive: Bhookly / CraveQuad (Multi-Vendor Campus Food Delivery Platform)

## 1. Structured Project Overview

- **Problem It Solves**: Multi-vendor campus food delivery platform designed to streamline food ordering, vendor management, and campus deliveries.
- **My Role**: [FILL IN: Describe your exact role and responsibilities, e.g., Lead Developer, Full-Stack Developer, Backend API Developer]
- **Tech Stack**:
  - *Architecture*: pnpm Monorepo
  - *Frontend*: Next.js 14
  - *Backend API*: NestJS
  - *Database & ORM*: PostgreSQL with Prisma ORM
- **One Hard Technical Problem I Solved**:
  - *Problem*: [FILL IN: Describe a real technical challenge or bottleneck you faced]
  - *Solution*: [FILL IN: Explain how you solved it and the technical trade-offs involved]
  - *Metrics*: [FILL IN: State any actual performance metrics, if available]
- **What I'd Improve in v2.0**:
  - [FILL IN: Mention features or architectural improvements you would make next]

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "Why did you choose NestJS with Next.js 14 in a pnpm monorepo for Bhookly?"
- **Guidance on How to Answer**:
  - Highlight that NestJS provides an enterprise-grade modular architecture (Controllers, Services, Modules) with built-in TypeScript support, perfect for complex backend domain logic like multi-vendor ordering.
  - Explain that Next.js 14 offers Server-Side Rendering (SSR) and Server Components for optimal performance, while a pnpm monorepo enables seamless code sharing (e.g., shared TypeScript types and DTOs) between frontend and backend.

### Q2: "How did Prisma ORM and PostgreSQL help handle data relationships across multiple campus vendors?"
- **Guidance on How to Answer**:
  - Explain how PostgreSQL provides strong relational integrity and ACID compliance, essential for handling transactions and order statuses across multiple vendors.
  - Mention that Prisma ORM provides type-safe database queries, auto-generated migrations, and clean relational mappings (`Vendor` -> `MenuItem` -> `Order`).

### Q3: "How would you handle high concurrent order placement during campus lunch rushes?"
- **Guidance on How to Answer**:
  - Discuss database transaction isolation levels in PostgreSQL to handle inventory updates safely.
  - Explain scaling options in NestJS (horizontal scaling of statelessly deployed microservices) and database connection pooling (e.g., via Prisma Accelerate or PgBouncer).
"""

with open('04-interview-prep/project-deep-dives/bhookly.md', 'w', encoding='utf-8') as f:
    f.write(bhookly_content)

# 2. prepgenius.md
prepgenius_content = """# Project Deep Dive: PrepGenius (AI Mock Interview Platform)

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
"""

with open('04-interview-prep/project-deep-dives/prepgenius.md', 'w', encoding='utf-8') as f:
    f.write(prepgenius_content)

# 3. scrutin.md
scrutin_content = """# Project Deep Dive: Scrutin (AI-Assisted Code Review Platform)

## 1. Structured Project Overview

- **Problem It Solves**: AI-assisted code review platform that analyzes code quality, detects bugs, evaluates performance, and scans for security vulnerabilities with real-time streaming reviews and shareable reports.
- **My Role**: [FILL IN: Describe your exact role, e.g., Backend Developer, Full-Stack Lead]
- **Tech Stack**:
  - *Frontend*: React 19, Vite, CodeMirror
  - *Backend*: Node.js, Express.js
  - *AI Model*: Google Gemini API
  - *Authentication*: GitHub OAuth via Passport.js
  - *Security & Middleware*: Helmet, Rate Limiting, OWASP Top 10 security scanning modules
  - *Deployment*: Railway (Backend) & Vercel (Frontend)
- **Key Features Verified**:
  - Real-time streaming code reviews.
  - Automated OWASP Top 10 security vulnerability detection.
  - Shareable code inspection reports.
- **One Hard Technical Problem I Solved**:
  - *Problem*: [FILL IN: Describe a real technical challenge faced during development]
  - *Solution*: [FILL IN: Describe how you resolved it]
- **What I'd Improve in v2.0**:
  - [FILL IN: Mention planned future features]

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "How did you implement real-time streaming code reviews with Google Gemini and Node.js?"
- **Guidance on How to Answer**:
  - Explain how the Node.js Express backend leveraged stream responses from the Google Gemini API, forwarding chunks to the React 19 frontend via Server-Sent Events (SSE) or chunked HTTP transfer encoding.
  - Discuss how this minimized perceived latency for long code reviews, allowing users to read feedback incrementally as CodeMirror highlighted issues.

### Q2: "How do you scan for OWASP Top 10 security vulnerabilities and ensure the analysis platform itself is secure?"
- **Guidance on How to Answer**:
  - Highlight security middleware like **Helmet** for HTTP header security and **express-rate-limit** to protect against abuse/DDoS.
  - Explain how specialized prompt rules and pattern scanners check submitted code for classic OWASP threats (SQL Injection, XSS, insecure dependencies, unhandled exceptions).

### Q3: "How does GitHub OAuth via Passport.js work in your authentication flow?"
- **Guidance on How to Answer**:
  - Walk through the OAuth 2.0 flow: User clicks 'Login with GitHub' -> redirected to GitHub consent page -> callback endpoint receives auth code -> Passport exchanges code for access token -> session JWT issued to frontend.
"""

with open('04-interview-prep/project-deep-dives/scrutin.md', 'w', encoding='utf-8') as f:
    f.write(scrutin_content)

# 4. hackathon-win.md
hackathon_content = """# STAR Story: Hackathon Victory (Club Untangle 1st Place)

## 1. What the Interviewer is Testing
When interviewers ask *"Tell me about a time you won a competition"* or *"Describe your biggest achievement under pressure"*, they are evaluating:
- **High-Pressure Execution**: Ability to deliver a functional MVP under strict time constraints.
- **Problem Solving & Adaptability**: How you navigate unexpected challenges during development.
- **Team Leadership & Initiative**: Taking ownership when critical issues arise.

---

## 2. The STAR Framework Breakdown
- **Situation**: Define the event context (university hackathon by Club Untangle).
- **Task**: Define your explicit role and team objective.
- **Action**: Specific technical and organizational steps YOU took to solve obstacles.
- **Result**: Final outcome (1st place victory) and learnings.

---

## 3. Written STAR Answer Template (Ravi's 1st Place Win)

> **[Situation]**
> "During my B.Tech at LPU, my team participated in a university-level hackathon organized by **Club Untangle**, competing [FILL IN: number of competing teams, if you want to state one] to build a functional software prototype within a strict deadline."
>
> **[Task]**
> "My role was [FILL IN: Lead Full-Stack Developer / Backend Developer / Team Lead]. Our goal was to design and deploy a working MVP for [FILL IN: brief description of problem statement]."
>
> **[Action]**
> "[FILL IN: Describe the specific technical challenge or bottleneck that occurred during the hackathon—e.g., an architectural issue, integration bug, or performance bottleneck. Explain the exact steps YOU took to diagnose, fix, or pivot the solution under pressure]."
>
> **[Result]**
> "Our team won **1st Place** in the Club Untangle hackathon. [FILL IN: Add any specific outcome, jury feedback, or key takeaways, e.g., prize won, project recognition]. This experience reinforced my ability to stay composed under pressure, debug effectively, and deliver results within tight deadlines."
"""

with open('04-interview-prep/star-answers/hackathon-win.md', 'w', encoding='utf-8') as f:
    f.write(hackathon_content)

print("All 4 verified files updated successfully.")
