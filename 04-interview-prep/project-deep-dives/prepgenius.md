# Project Deep Dive: PrepGenius (AI Mock Interview Assistant)

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
