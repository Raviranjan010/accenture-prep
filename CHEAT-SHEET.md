# Accenture Placement Final Revision Cheat-Sheet

A single quick-scan reference card for the day before your assessment and interview. Links point back to full topic guides for deeper re-study.

---

## 1. Quantitative Formulas

- **Percentages & Multipliers**: Net successive change $= a + b + \frac{ab}{100}\%$. Gain multiplier $= \times (1 + r)$, Loss multiplier $= \times (1 - r)$. Link: [percentages-profit-loss.md](01-aptitude/quantitative/percentages-profit-loss.md)
- **Profit, Loss & Discounts**: Profit/Loss $\%$ is calculated strictly on **Cost Price (CP)**; Discount $\%$ is calculated strictly on **Marked Price (MP)**. Link: [percentages-profit-loss.md](01-aptitude/quantitative/percentages-profit-loss.md)
- **Time, Speed & Distance**: $D = S \times T$. Convert $\text{km/h} \rightarrow \text{m/s}$ by multiplying by $\frac{5}{18}$. Link: [time-speed-distance.md](01-aptitude/quantitative/time-speed-distance.md)
- **Average Speed & Relative Speed**: Average Speed $= \frac{2xy}{x+y}$ (equal distances). Relative Speed: opposite directions $= S_1 + S_2$, same direction $= |S_1 - S_2|$. Link: [time-speed-distance.md](01-aptitude/quantitative/time-speed-distance.md)
- **Ratios & Averages**: Weighted Average $= \frac{n_1 a_1 + n_2 a_2}{n_1 + n_2}$. Rule of Alligation: $\frac{\text{Cheaper Qty}}{\text{Dearer Qty}} = \frac{D - M}{M - C}$. Link: [ratios-averages.md](01-aptitude/quantitative/ratios-averages.md)

---

## 2. Logical Reasoning #1 Tricks

- **Coding & Decoding**: Use **EJOTY** ($E=5, J=10, O=15, T=20, Y=25$) and **Opposite Letter Sum = 27** ($A1 + Z26 = 27$) for instant letter indexing. Link: [coding-decoding.md](01-aptitude/logical-reasoning/coding-decoding.md)
- **Blood Relations**: Use the **Self-Substitution Method** (read quotes from "my/his/her" outwards) and generation gap counts ($+2, +1, 0, -1$). Link: [blood-relations.md](01-aptitude/logical-reasoning/blood-relations.md)
- **Seating Arrangement**: Always start with **definite clues** first; draw 2 parallel case diagrams for ambiguous statements. Link: [seating-arrangement.md](01-aptitude/logical-reasoning/seating-arrangement.md)

---

## 3. Core CS Fundamentals

- **4 OOP Pillars**:
  - *Encapsulation*: Private data + public getters/setters.
  - *Abstraction*: Hiding complexity behind interfaces/abstract classes.
  - *Inheritance*: `extends` parent class for code reuse ("Is-A").
  - *Polymorphism*: Overloading (Compile-time) vs Overriding (Run-time). Link: [oop-concepts.md](02-technical-coding/cs-fundamentals/oop-concepts.md)
- **DBMS Normal Forms**:
  - *1NF*: Atomic values only (no repeating groups/arrays).
  - *2NF*: 1NF + No partial dependencies (depends on entire primary key).
  - *3NF*: 2NF + No transitive dependencies ($A \rightarrow B \rightarrow C$).
  - *BCNF*: Every determinant $X$ in $X \rightarrow Y$ must be a super key. Link: [dbms-normalization-joins.md](02-technical-coding/cs-fundamentals/dbms-normalization-joins.md)
- **OS MCQ High-Yields**:
  - *Process vs Thread*: Process has separate isolated memory space; Thread shares heap memory with parent process.
  - *Deadlock 4 Conditions*: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait (All 4 required).
  - *Round Robin*: Preemptive CPU scheduling using a fixed Time Quantum $q$. Link: [os-basics.md](02-technical-coding/cs-fundamentals/os-basics.md)
- **Networking MCQ High-Yields**:
  - *Ports*: HTTP (80), HTTPS (443), DNS (53), SSH (22).
  - *TCP vs UDP*: TCP is connection-oriented, reliable (3-Way Handshake: `SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`); UDP is fast, connectionless (Streaming/Gaming). Link: [networking-basics.md](02-technical-coding/cs-fundamentals/networking-basics.md)

---

## 4. Placement Grammar Top 3 Rules

- **Present Perfect vs Simple Past**: Simple Past for specific past time (*yesterday, in 2024*); Present Perfect for unspecified past time with current relevance (*have submitted*). Link: [grammar-vocab-notes.md](03-communication/grammar-vocab-notes.md)
- **Fixed Prepositions**: Say *"discuss the project"* (NOT "discuss about"); *"congratulate on"* (NOT "for"); *"comply with"*. Link: [grammar-vocab-notes.md](03-communication/grammar-vocab-notes.md)
- **Subject-Verb Agreement**: In *Either...or / Neither...nor*, the verb agrees strictly with the **closest subject**. Link: [grammar-vocab-notes.md](03-communication/grammar-vocab-notes.md)

---

## 5. STAR Behavioral Structure Reminder

- **STAR Method**: **Situation** (set context) $\rightarrow$ **Task** (your goal) $\rightarrow$ **Action** (specific steps YOU took under pressure) $\rightarrow$ **Result** (quantified outcome & learning). Links: [hackathon-win.md](04-interview-prep/star-answers/hackathon-win.md) | [teamwork.md](04-interview-prep/star-answers/teamwork.md) | [conflict-challenge.md](04-interview-prep/star-answers/conflict-challenge.md)
