import os

os.makedirs('04-interview-prep/star-answers', exist_ok=True)
os.makedirs('04-interview-prep/project-deep-dives', exist_ok=True)

# 1. 04-interview-prep/README.md
readme_content = """# Interview Preparation Index & Final Prep Strategy

Welcome to the **Interview Preparation Module**. This section is designed to refine your behavioral STAR stories, technical project deep-dives, and panelist interactions for Accenture's technical and HR rounds.

## Recommended Preparation Timeline (T-minus 4 Days to Interview)

This module should be tackled **3 to 4 days before your scheduled interview**, after completing basic Aptitude and Technical CS review:

- **Day -4 (Behavioral STAR Mastery)**: Read all guides under `star-answers/`. Finalize your actual personal stories for `teamwork.md` and `conflict-challenge.md` using the provided STAR templates.
- **Day -3 (Project Deep-Dives)**: Fill out the technical details, architecture decisions, and hard problems solved for `bhookly.md`, `prepgenius.md`, and `scrutin.md`. Review the 3 follow-up questions per project.
- **Day -2 (Panelist Questions & Delivery)**: Memorize your top 3 favorite questions from `questions-to-ask-panelist.md`. Conduct 2 full mock interview recordings and log them in `mock-interview-log.md`.
- **Day -1 (Final Review & Polish)**: Re-read your project deep-dives and STAR stories. Ensure smooth, confident speech without over-rehearsing.

---

## Folder Structure & Checklist

### STAR Behavioral Stories
- [ ] [Hackathon Win STAR Answer](star-answers/hackathon-win.md) — 1st Place at Club Untangle University Hackathon story.
- [ ] [Teamwork STAR Answer](star-answers/teamwork.md) — Collaboration and team contribution framework.
- [ ] [Conflict & Challenge STAR Answer](star-answers/conflict-challenge.md) — Technical/team conflict resolution framework.

### Technical Project Deep-Dives
- [ ] [Project Deep-Dive: Bhookly](project-deep-dives/bhookly.md) — Real-time food ordering platform architecture & follow-ups.
- [ ] [Project Deep-Dive: PrepGenius](project-deep-dives/prepgenius.md) — AI mock interview system architecture & follow-ups.
- [ ] [Project Deep-Dive: Scrutin](project-deep-dives/scrutin.md) — Technical project breakdown & follow-ups.

### Interview Readiness
- [ ] [Questions to Ask Panelist](questions-to-ask-panelist.md) — 8 curated strategic questions categorized by Role, Team, and Growth.
- [ ] [Mock Interview Log](mock-interview-log.md) — Ready-to-use performance tracking table.
"""

with open('04-interview-prep/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

# 2. star-answers/hackathon-win.md
hackathon_content = """# STAR Story: Hackathon Victory (Club Untangle 1st Place)

## 1. What the Interviewer is Testing
When interviewers ask *"Tell me about a time you won a competition"* or *"Describe your biggest technical achievement under pressure"*, they are evaluating:
- **High-Pressure Execution**: Ability to deliver working software under strict deadlines.
- **Problem Solving & Innovation**: How you translate a raw problem statement into an effective MVP.
- **Leadership & Ownership**: Taking initiative to solve unexpected technical bottlenecks without panic.

---

## 2. The STAR Framework Breakdown
- **Situation**: Set the context—where were you, what was the competition, and what was the deadline?
- **Task**: Define your explicit responsibility and the goal your team set out to accomplish.
- **Action**: Explain the specific technical and tactical steps **YOU** took to build the solution.
- **Result**: Quantify the final outcome, award achieved, and key takeaways.

---

## 3. Fully Written Example Answer (Ravi's 1st Place Win)

> **[Situation]**
> "During my B.Tech at LPU, my team participated in the **Club Untangle University-Level Hackathon**, competing against 45+ senior developer teams to build a functional prototype within a strict **24-hour deadline**."
>
> **[Task]**
> "Our goal was to solve campus food court congestion during peak hours. As the **Lead Full-Stack Developer**, my task was to architect and build a real-time order processing API and an intuitive user interface that could handle concurrent token generation without database locks."
>
> **[Action]**
> "Twelve hours into the hackathon, we hit a major bottleneck: simultaneous order requests caused database lockups in our initial SQL implementation. Recognizing that we were losing time, I took ownership and migrated the order-queuing pipeline to an in-memory **Redis queue** integrated with **Node.js** webhooks. I worked through the night to implement optimistic concurrency control and built a lightweight React frontend dashboard for live stall status updates."
>
> **[Result]**
> "Our application processed over 200 simulated concurrent orders with a sub-300ms response time during the live jury demonstration. Out of 45 competing teams, we won **1st Place**, receiving a cash prize and recognition from university leadership. More importantly, this experience taught me how to stay calm under intense pressure and pivot system architecture rapidly when technical bottlenecks arise."
"""

with open('04-interview-prep/star-answers/hackathon-win.md', 'w', encoding='utf-8') as f:
    f.write(hackathon_content)

# 3. star-answers/teamwork.md
teamwork_content = """# STAR Story: Teamwork & Collaboration

## 1. What the Interviewer is Testing
When interviewers ask *"Describe a time you worked in a team"* or *"How do you handle team dynamics?"*, they are evaluating:
- **Collaboration & Adaptability**: How well you fit into agile engineering teams at Accenture.
- **Communication**: Ability to keep team members aligned, share knowledge, and support struggling peers.
- **Unselfish Focus**: Prioritizing overall project delivery above individual credit.

---

## 2. The STAR Framework Breakdown
- **Situation**: Context of the team project (college project, event, or internship task).
- **Task**: The shared objective and your specific assigned role within the team.
- **Action**: Concrete actions you took to collaborate, help teammates, or streamline workflow.
- **Result**: Project completion, team success, and team feedback.

---

## 3. Customizable Answer Template

> **[Situation]**
> "During our final year semester project, a team of **[3 / 4]** students was tasked with building **[Insert Project Name, e.g., Bhookly / PrepGenius]** within a **[4-week]** sprint."
>
> **[Task]**
> "My primary responsibility was **[Frontend / Backend / Database design]**, but our overall objective was to integrate all modules seamlessly before the mid-term review."
>
> **[Action]**
> "Two weeks before the deadline, one of our teammates struggling with **[API integration / state management]** fell behind schedule, which threatened to block the entire integration pipeline. Instead of assigning blame, I organized daily 20-minute pair-programming sessions after class. I helped them debug **[CORS / database schema]** issues and set up standardized Git branching rules so everyone could commit code without merge conflicts."
>
> **[Result]**
> "Thanks to our synchronized workflow, we integrated all modules **[3 days]** ahead of the deadline. Our team received an **[A+ grade / 95% evaluation score]** from the faculty panel, and my teammates praised the collaborative debugging sessions for keeping the project on schedule."
"""

with open('04-interview-prep/star-answers/teamwork.md', 'w', encoding='utf-8') as f:
    f.write(teamwork_content)

# 4. star-answers/conflict-challenge.md
conflict_content = """# STAR Story: Overcoming Conflict & Technical Challenges

## 1. What the Interviewer is Testing
When interviewers ask *"Tell me about a disagreement with a teammate"* or *"Describe a major technical challenge you faced"*, they are evaluating:
- **Emotional Intelligence & Maturity**: Disagreeing professionally based on data, not ego.
- **Problem Resolution**: How you bridge technical disagreements to reach consensus.
- **Resilience**: Staying solution-oriented when things go wrong.

---

## 2. The STAR Framework Breakdown
- **Situation**: Setting the technical or interpersonal conflict context.
- **Task**: The dilemma or decision that needed to be resolved.
- **Action**: Objective steps taken (benchmarking, discussions, trade-off analysis) to resolve the issue.
- **Result**: The final choice made, project outcome, and strengthened working relationship.

---

## 3. Customizable Answer Template

> **[Situation]**
> "While developing **[Insert Project Name, e.g., PrepGenius / Bhookly]**, my teammate and I had a strong disagreement regarding the database architecture. My teammate wanted to use **[MongoDB / NoSQL]** for quick prototyping, whereas I advocated for **[PostgreSQL / Relational DB]** to enforce strict data relationships."
>
> **[Task]**
> "As the project deadline was approaching, we needed to resolve this dispute quickly without hurting team morale or delaying sprint progress."
>
> **[Action]**
> "Rather than arguing hypothetically, I suggested a data-driven approach. I spent two hours building a small benchmark script simulating **[1,000 concurrent order writes / relational joins]** on both databases. We then sat down together, reviewed the benchmark logs objectively, and discussed our production requirements. Realizing that our application required **[frequent atomic transactions / flexible JSON schemas]**, we mutually agreed to use **[Selected DB]**."
>
> **[Result]**
> "This empirical approach resolved the conflict completely with zero hard feelings. We delivered the backend module **[2 days early]** with clean architecture, and it established a precedent in our team to always rely on benchmarks and objective data when making architectural decisions."
"""

with open('04-interview-prep/star-answers/conflict-challenge.md', 'w', encoding='utf-8') as f:
    f.write(conflict_content)

print("STAR files generated successfully.")
