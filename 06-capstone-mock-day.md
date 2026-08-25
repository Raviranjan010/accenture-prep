# Capstone Full-Length Mock Assessment & Interview Day

A complete simulated assessment experience combining all 4 tracks. Rehearse context-switching under timed conditions to mirror Accenture's live recruitment day.

---

## ⏱️ Section 1: Mixed Aptitude Assessment (15-Minute Time Limit)

**Instructions**: Solve these 10 questions covering Quantitative, Logical Reasoning, and Verbal Ability within 15 minutes.

1. **(Quant)** An item bought for ₹800 is sold at a 25% profit. What is the selling price?
2. **(Quant)** A train traveling at 72 km/h crosses a pole in 10 seconds. What is the length of the train in meters?
3. **(Quant)** Divide ₹900 between A and B in the ratio 4 : 5. What is B's share?
4. **(Logical)** If `SPRING` is coded as `TQSJOH`, how is `SUMMER` coded?
5. **(Logical)** Pointing to a woman, Rahul said, "She is the daughter of the only son of my grandfather." How is the woman related to Rahul?
6. **(Logical)** In an 8-person circular table facing center, if A is at seat 1, who sits directly opposite A?
7. **(Verbal)** Identify the grammatically correct sentence:
   - a) We discussed about the software architecture yesterday.
   - b) We discussed the software architecture yesterday.
   - c) We have discussed about the software architecture yesterday.
8. **(Verbal)** Reorder the sentences into a logical paragraph:
   - A. Consequently, renewable energy adoption has surged.
   - B. Global carbon emissions reached record levels last decade.
   - C. Governments responded by subsidizing solar and wind infrastructure.
9. **(Quant)** If the price of petrol increases by 20%, by what percentage must a driver reduce consumption so expenditure remains constant?
10. **(Logical)** If `CAT` = 24 and `DOG` = 26, what is `PIG`?

---

### Section 1 Answer Key & Explanations

1. **₹1,000** — $SP = 800 \times 1.25 = ₹1,000$.
2. **200 meters** — $72 \text{ km/h} \times \frac{5}{18} = 20 \text{ m/s}$. Length $= 20 \times 10 = 200 \text{ m}$.
3. **₹500** — Total parts $= 4 + 5 = 9$. Value per part $= 900 / 9 = 100$. B's share $= 5 \times 100 = ₹500$.
4. **TVNNFS** — Shift each letter $+1$ forward ($S \rightarrow T, U \rightarrow V, M \rightarrow N, M \rightarrow N, E \rightarrow F, R \rightarrow S$).
5. **Sister** — "Only son of my grandfather" $\rightarrow$ Rahul's father. "Daughter of Rahul's father" $\rightarrow$ Rahul's sister.
6. **Seat 5** — In 8-person circle facing center, seat opposite seat $1$ is $1 + (8/2) = 5$.
7. **b** — "Discuss" takes no preposition ("discussed the software architecture"); Simple Past is required with "yesterday".
8. **B - C - A** — B states problem (emissions) $\rightarrow$ C states government action (subsidies) $\rightarrow$ A states consequence (surge).
9. **16.67%** — Formula: $\frac{r}{100 + r} \times 100 = \frac{20}{120} \times 100 = \frac{1}{6} \times 100 = 16.67\%$.
10. **32** — Sum of positional values: $P(16) + I(9) + G(7) = 32$.

---

## 💻 Section 2: Technical CS & DSA Coding Test

### Part A: Core CS MCQs
1. **(DBMS)** Which normal form eliminates transitive dependencies?
2. **(Networking)** What protocol and port number are used for encrypted secure web traffic?

### Part B: Medium DSA Hands-on Coding Problem
**Problem Statement**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Assume exactly one solution exists and you may not use the same element twice. Optimize for $O(N)$ time complexity.

---

### Section 2 Answer Key & Explanations

#### Part A MCQs
1. **3NF (Third Normal Form)** — Eliminates transitive dependencies ($A \rightarrow B \rightarrow C$).
2. **HTTPS on Port 443** — Uses TLS/SSL encryption on TCP Port 443.

#### Part B Coding Solution
```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```
- **Time Complexity**: $O(N)$ single pass hash table lookup.
- **Space Complexity**: $O(N)$ auxiliary hash map storage.

---

## 🗣️ Section 3: Spoken Communication & Grammar Drill

### Task 1: Read-Aloud Spoken Practice
*Instructions: Read the following paragraph aloud into a recorder, focusing on clear technical pronunciation, natural pauses, and 130 WPM pacing.*

> "Accenture's digital transformation strategy enables global enterprises to modernize legacy infrastructures through cloud migration and artificial intelligence integration. By implementing microservices and automated CI/CD pipelines, engineering teams accelerate deployment cycles while maintaining strict data governance."

### Task 2: Grammar & Error Spotting
1. *Correct this sentence*: "Neither the project manager nor the software developers was present at the call."
2. *Fill in the blank*: "Ravi has been working on full-stack web applications __________ 2023."
3. *Identify the error*: "The lead engineer congratulated the team for completing the sprint on time."

---

### Section 3 Answer Key & Explanations
1. **"Neither the project manager nor the software developers WERE present at the call."** (Verb agrees with closest subject "software developers", which is plural).
2. **"since"** (Use "since" for specific starting points in time; "for" for duration).
3. Change "congratulated the team for" to **"congratulated the team ON completing..."** (Fixed preposition rule: *congratulate on*).

---

## 🎯 Section 4: Interview Round Simulation

*Instructions: Rehearse speaking your answers out loud. Evaluate your response against the provided criteria guidance.*

### Question 1 (Self-Introduction)
- **Prompt**: *"Good morning! Please introduce yourself."*
- **Evaluation Guidance for a Strong Response**:
  - Keep duration strictly between 60 and 90 seconds.
  - State name, degree (B.Tech CS at LPU), specialization (Full-Stack & AI-ML focus).
  - Highlight 1-2 major projects (*Bhookly*, *PrepGenius*) and real tech stack (Next.js, NestJS, React, Gemini).
  - Conclude with why Accenture aligns with your career goals.

### Question 2 (STAR Behavioral)
- **Prompt**: *"Tell me about a time you had a technical disagreement with a team member."*
- **Evaluation Guidance for a Strong Response**:
  - Follow **Situation $\rightarrow$ Task $\rightarrow$ Action $\rightarrow$ Result**.
  - Frame the conflict around technical trade-offs (e.g., database choice or architecture design), NOT personal friction.
  - Emphasize taking an objective, data-driven approach (e.g., writing a quick benchmark script to test performance).
  - End with a positive result and how it strengthened team decision-making.

### Question 3 (Project Deep-Dive)
- **Prompt**: *"How did you handle real-time code analysis feedback in your project Scrutin?"*
- **Evaluation Guidance for a Strong Response**:
  - State the real tech stack (React 19, Node.js/Express, Google Gemini API, CodeMirror, SSE).
  - Explain using Server-Sent Events (SSE) or HTTP stream response from Gemini to deliver real-time feedback without long polling latency.
  - Mention security middleware (Helmet, rate limiting) protecting the application.
