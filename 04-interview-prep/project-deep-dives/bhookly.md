# Project Deep Dive: Bhookly (Food Ordering Platform)

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
