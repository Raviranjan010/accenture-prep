import os

# 1. bhookly.md
bhookly_content = """# Project Deep Dive: Bhookly (Food Ordering Platform)

## 1. Structured Project Overview

- **Problem It Solves**: Eliminates physical queue congestion at university food courts by allowing students to order food online, track live preparation status, and receive automated digital pickup tokens.
- **My Role**: **Lead Full-Stack Developer** — Responsible for backend REST API architecture, database schema design, and live order status state management.
- **Tech Stack**: 
  - *Frontend*: React.js, Redux Toolkit, Tailwind CSS
  - *Backend*: Node.js, Express.js
  - *Database*: MongoDB (Mongoose ODM)
  - *Real-time Communication*: Socket.io (for live kitchen dashboard order updates)
- **One Hard Technical Problem I Solved**:
  - *Problem*: Simultaneous peak-hour orders caused double-booking of item quantities and web socket connection drops under high concurrency.
  - *Solution*: Implemented MongoDB atomic operations (`$inc` with conditional guards) for inventory reservation and introduced a Redis caching layer for active session management, reducing API latency from 1.2s to 180ms.
- **What I'd Improve in v2.0**:
  - Integrate a microservice architecture separating order processing from payment webhooks.
  - Implement Web Push Notifications via PWA to alert students when food is ready.

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "Why did you choose MongoDB over a SQL database like MySQL for an ordering system?"
- **Guidance on How to Answer**: 
  - Acknowledge that food ordering can be relational, but explain that menu items across different food vendors contained highly dynamic, deeply nested attributes (custom toppings, variants, dietary tags) that fit MongoDB's flexible JSON document model.
  - Emphasize how you handled transactional consistency using Mongoose sessions/ACID transactions for order payment updates.

### Q2: "How did you handle real-time status updates between the customer and the kitchen staff?"
- **Guidance on How to Answer**:
  - Explain the usage of **Socket.io** event emitters (`order_placed`, `order_status_updated`).
  - Mention fallbacks: If the WebSockets connection fails due to weak campus Wi-Fi, the client gracefully falls back to HTTP long-polling every 5 seconds.

### Q3: "How would you scale Bhookly if 10,000 students ordered at the exact same minute during lunch break?"
- **Guidance on How to Answer**:
  - **Load Balancing**: Place Node.js instances behind an NGINX reverse proxy.
  - **Message Queue**: Offload order creation to a BullMQ/RabbitMQ message queue to smooth out spike traffic.
  - **Database Read Scaling**: Implement MongoDB Read Replicas for menu browsing while directing writes to the Primary node.
"""

with open('04-interview-prep/project-deep-dives/bhookly.md', 'w', encoding='utf-8') as f:
    f.write(bhookly_content)

# 2. prepgenius.md
prepgenius_content = """# Project Deep Dive: PrepGenius (AI Mock Interview Assistant)

## 1. Structured Project Overview

- **Problem It Solves**: Provides automated, low-cost technical mock interviews for placement students with instant evaluation on technical correctness, speech clarity, and body language.
- **My Role**: **Full-Stack & AI Integration Engineer** — Designed LLM prompt engineering pipeline, audio processing service, and web dashboard.
- **Tech Stack**:
  - *Frontend*: React.js, Web Audio API, SpeechRecognition API
  - *Backend*: Python (FastAPI) / Node.js
  - *AI / APIs*: OpenAI GPT-4 API (Evaluation Engine), Whisper API (Speech-to-Text)
  - *Database*: PostgreSQL / Prisma ORM
- **One Hard Technical Problem I Solved**:
  - *Problem*: High API latency (4-6 seconds per answer evaluation) disrupted live interview conversation flow.
  - *Solution*: Implemented response streaming (SSE / Server-Sent Events) and chunked speech processing, allowing the UI to display evaluation criteria progressively as the model generated feedback.
- **What I'd Improve in v2.0**:
  - Add computer vision gaze tracking via MediaPipe to give feedback on eye contact and posture during video answers.

---

## 2. Top 3 Interviewer Follow-up Questions & How to Answer

### Q1: "How do you prevent the LLM from hallucinating when evaluating complex technical answers?"
- **Guidance on How to Answer**:
  - Explain your **Prompt Engineering & RAG (Retrieval-Augmented Generation)** approach: Provide the LLM with a strict canonical reference answer schema and explicit scoring rubrics (0–10 scale).
  - Constrain output formats using JSON Mode to enforce structured JSON parsing.

### Q2: "How did you store and process candidate speech recording efficiently?"
- **Guidance on How to Answer**:
  - Audio recorded in browser via MediaRecorder API converted to lightweight `.webm` format.
  - Uploaded directly to S3 bucket via presigned URLs (avoiding backend bottleneck), then passed to Whisper API for transcription.

### Q3: "What security measures did you take regarding OpenAI API key storage?"
- **Guidance on How to Answer**:
  - Never exposed API keys on the frontend client.
  - Kept keys strictly in server-side environment variables (`.env`), protected behind rate-limiting middleware (Express-rate-limit) to prevent quota abuse.
"""

with open('04-interview-prep/project-deep-dives/prepgenius.md', 'w', encoding='utf-8') as f:
    f.write(prepgenius_content)

# 3. scrutin.md
scrutin_content = """# Project Deep Dive: Scrutin (Automated Code / Content Inspection Tool)

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
"""

with open('04-interview-prep/project-deep-dives/scrutin.md', 'w', encoding='utf-8') as f:
    f.write(scrutin_content)

# 4. questions-to-ask-panelist.md
questions_content = """# Questions to Ask the Interviewer (Accenture Panelist)

Asking thoughtful, strategic questions at the end of your interview demonstrates curiosity, professional maturity, and genuine interest in joining Accenture.

---

## Category 1: Role & Daily Engineering Work

1. **"What does a typical day look like for a junior Software Engineer joining Accenture's technology practice?"**
   - *Why it's a great question*: Shows you are already visualizing yourself in the role and eager to understand day-to-day expectations.
2. **"Which modern tech stacks or cloud platforms (AWS, Azure, GCP) are currently seeing the highest client demand across your team's project pipeline?"**
   - *Why it's a great question*: Demonstrates tech awareness and desire to align your skills with market demand.
3. **"How are development teams typically structured at Accenture—are they agile squads with dedicated scrum masters and product owners?"**
   - *Why it's a great question*: Shows familiarity with corporate Agile methodologies and team dynamics.

---

## Category 2: Team Dynamics & Culture

4. **"What quality or habit differentiates a good fresh graduate hire from an exceptional one during their first 90 days at Accenture?"**
   - *Why it's a great question*: Signals high ambition, coachability, and a drive to excel right from day one.
5. **"How does Accenture foster continuous learning and skill upgrade for engineers when transitioning between client projects?"**
   - *Why it's a great question*: Highlights your commitment to long-term professional growth and self-improvement.

---

## Category 3: Growth & Innovation

6. **"With Accenture investing heavily in Generative AI and enterprise automation, how are entry-level engineers being trained to leverage these tools in client delivery?"**
   - *Why it's a great question*: Shows you follow company industry news and are forward-thinking about modern technology trends.
7. **"What has been your favorite project or technical milestone during your tenure with Accenture?"**
   - *Why it's a great question*: People love sharing personal success stories; it builds a warm human connection with the panelist.
8. **"What are the next steps in the evaluation process following today's round?"**
   - *Why it's a great question*: A professional, standard closing question showing eager interest in moving forward.
"""

with open('04-interview-prep/questions-to-ask-panelist.md', 'w', encoding='utf-8') as f:
    f.write(questions_content)

# 5. mock-interview-log.md
mock_log_content = """# Mock Interview Log

Use this log to record your full-length or sectional technical/HR mock interview sessions (conducted with peers, mentors, or self-recordings).

---

## Mock Interview Tracking Table

| Date | Question Asked | My Answer Summary | Self-Rating (1-5) | What to Improve |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-22 | "Tell me about a time you faced a major technical challenge." | Used STAR framework to explain Redis migration during Club Untangle hackathon. | ⭐⭐⭐⭐ (4/5) | Quantify initial latency (1.2s vs 180ms) earlier in the Action phase. |
| 2026-08-24 | "Why should we hire you for Accenture over other candidates?" | Mentioned B.Tech CS background, full-stack skills, and passion for technology. | ⭐⭐⭐ (3/5) | Sounded too generic; connect skills directly to Accenture's client delivery and AI culture. |
| YYYY-MM-DD | [Insert Question Asked] | [Summary of your spoken response] | ⭐⭐⭐⭐⭐ (_/5) | [Action item for next practice round] |
| YYYY-MM-DD | [Insert Question Asked] | [Summary of your spoken response] | ⭐⭐⭐⭐⭐ (_/5) | [Action item for next practice round] |
| YYYY-MM-DD | [Insert Question Asked] | [Summary of your spoken response] | ⭐⭐⭐⭐⭐ (_/5) | [Action item for next practice round] |
| YYYY-MM-DD | [Insert Question Asked] | [Summary of your spoken response] | ⭐⭐⭐⭐⭐ (_/5) | [Action item for next practice round] |
"""

with open('04-interview-prep/mock-interview-log.md', 'w', encoding='utf-8') as f:
    f.write(mock_log_content)

print("All 04-interview-prep files generated successfully.")
