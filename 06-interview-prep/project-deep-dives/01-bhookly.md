# Project Deep Dive: Bhookly / CraveQuad (Multi-Vendor Campus Food Delivery Platform)

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
