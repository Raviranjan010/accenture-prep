# Project Deep Dive: Scrutin (Automated Code / Content Inspection Tool)

## 1. Structured Project Overview

- **Problem It Solves**: Automates static code analysis, vulnerability scanning, and code smell detection for student project repositories prior to submission.
- **My Role**: **Backend Developer** — Implemented static parser integration, AST (Abstract Syntax Tree) rule evaluation, and report generation pipeline.
- **Tech Stack**:
  - *Backend*: Python, AST module, ESLint/Flake8 CLI wrappers
  - *Frontend*: React.js with Monaco Editor integration
  - *Database*: PostgreSQL
  - *Job Processing*: Celery + Redis worker queues
- **One Hard Technical Problem I Solved**:
  - *Problem*: Long-running repository analysis tasks blocked main API threads, causing HTTP request timeouts.
  - *Solution*: Decoupled scanning pipeline into background worker tasks using Celery and Redis. Implemented WebSocket status progress bars (`0% -> 100%`) for the user UI.
- **What I'd Improve in v2.0**:
  - Add custom AI fix suggestions for identified security vulnerabilities using local LLM inference.

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "How did you handle large code repositories without exhausting server memory?"
- **Guidance on How to Answer**:
  - Streams file reads line-by-line rather than loading entire multi-megabyte files into RAM.
  - Enforced repository size limits (e.g., max 50MB) and ignored `node_modules` / `.git` directories.

### Q2: "Why did you choose Celery and Redis for job processing?"
- **Guidance on How to Answer**:
  - Static code analysis is I/O and CPU heavy; running it synchronously in HTTP request-response cycles would crash the server.
  - Celery allows asynchronous background processing and Redis acts as an ultra-fast message broker and result backend.

### Q3: "How would you prevent malicious code execution during analysis?"
- **Guidance on How to Answer**:
  - Static analysis reads code as plain text/AST without executing the code (`exec()` or `eval()` are never called).
  - For dynamic tests, execution takes place inside isolated, ephemeral Docker container sandboxes with network access disabled.
