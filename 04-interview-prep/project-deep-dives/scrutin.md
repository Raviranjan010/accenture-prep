# Project Deep Dive: Scrutin (AI-Assisted Code Review Platform)

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
