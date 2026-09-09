# Logical Reasoning: Seating Arrangement

## What this is
Seating Arrangement tests your logical capability to reconstruct precise spatial positioning of individuals along linear rows (facing North/South) or around circular/polygonal tables (facing Center/Outward) based on a set of positive and negative positioning constraints.

---

## Formula / Rule / Pattern

| Configuration | Facing Direction | Right Direction | Left Direction |
| :--- | :--- | :--- | :--- |
| **Linear Row** | North | Move Right $\rightarrow$ | $\leftarrow$ Move Left |
| **Linear Row** | South | $\leftarrow$ Move Left | Move Right $\rightarrow$ |
| **Circular Table** | Center | Counter-Clockwise (CCW) | Clockwise (CW) |
| **Circular Table** | Outside | Clockwise (CW) | Counter-Clockwise (CCW) |

---

## Shortcut: The Fixed-Anchor First Rule

> [!TIP]
> ### Fixed-Anchor First Trick
> Mark **definite/fixed positions first** (e.g. "A sits at extreme left end" or "B sits 3rd to right of C"), and place conditional negative clues (e.g. "X is not adjacent to Y") **last**.
> 
> *Why it works*: Fixed clues lock in baseline coordinates and prune 80% of possible arrangement permutations immediately, whereas negative clues only state what is *not* true without reducing spatial options cleanly.

---

## Worked Examples

### Example 1: Linear Arrangement Facing North (Easy)
- **Question**: 5 people (A, B, C, D, E) sit in a row facing North. C is in the exact middle. A sits at extreme left. B is to immediate right of C. D is between A and C. Where does E sit?
- **Step-by-step Solution**:
  1. 5 positions: `[1] [2] [3] [4] [5]`.
  2. Fixed clue: C in middle $\implies$ Position 3 = C.
  3. Fixed clue: A at extreme left $\implies$ Position 1 = A.
  4. Fixed clue: B to immediate right of C $\implies$ Position 4 = B.
  5. Fixed clue: D between A and C $\implies$ Position 2 = D.
  6. Remaining slot (Position 5) $= \text{E}$.
  7. **Arrangement**: `A - D - C - B - E`. E sits at **Extreme Right End**.

### Example 2: Circular Arrangement Facing Center (Medium)
- **Question**: 6 people (P, Q, R, S, T, U) sit in a circle facing the center. P is opposite to S. Q is to immediate right of P. R is between P and T. Where is U?
- **Step-by-step Solution**:
  1. Fix P at 6 o'clock position.
  2. S is opposite P $\implies$ 12 o'clock position.
  3. Q is immediate right of P (facing center, right is CCW) $\implies$ 8 o'clock.
  4. R is between P and T $\implies$ 4 o'clock (R) and 2 o'clock (T).
  5. Remaining slot (10 o'clock) $= \text{U}$.
  6. **U is between S and Q**.

---

## Practice Questions (PYQ Bank)

Q1. 5 friends are sitting in a row facing North. A is to the right of B, E is to the left of B but to the right of C. D is to the right of A. Who is sitting in the middle?  
a) B  
b) A  
c) C  
d) E  

Q2. 6 persons A, B, C, D, E, F sit around a circular table facing center. A is opposite to D. B is to immediate left of A. C is between D and B. Who is to immediate right of A?  
a) F or E  
b) C  
c) B  
d) D  

Q3. In a row of 40 boys, Sameer is 14th from the left end. What is his rank from the right end?  
a) 26th  
b) 27th  
c) 28th  
d) 25th  

Q4. A, B, C, D, E, F are sitting in a circle. A is between E and F. E is opposite to D. C is not adjacent to E. Who is opposite to F?  
a) C  
b) B  
c) D  
d) Cannot be determined  

Q5. 4 girls A, B, C, D are sitting in a square facing center at 4 corners. A is to the immediate right of B. C is opposite to B. Where is D?  
a) To the immediate left of B  
b) Opposite to A  
c) Both a and b  
d) Next to C  

Q6. If 8 people sit around a circular table facing center, what is the position directly opposite to person at Position 1?  
a) Position 4  
b) Position 5  
c) Position 6  
d) Position 3  

Q7. In a linear arrangement facing South, moving to the "Right" of a person means moving in which compass direction?  
a) East  
b) West  
c) North  
d) South  

Q8. 7 people A, B, C, D, E, F, G are sitting in a line facing North. C is 3rd to right of G. B is at extreme right. Who is in the middle if D is adjacent to both B and C?  
a) C  
b) D  
c) E  
d) G  

Q9. In a row of students, Rahul is 10th from left and 15th from right. Total number of students in the row:  
a) 24  
b) 25  
c) 26  
d) 23  

Q10. Five people P, Q, R, S, T sit in a row. R is to the immediate left of S. T is to the right of Q. P is between Q and R. Who is at the extreme left?  
a) Q  
b) T  
c) P  
d) S  

Q11. Why do circular arrangements facing Outside invert Left and Right movements?  
a) Facing away from center shifts the observer's relative orientation by $180^\circ$  
b) It is a rule of physics  
c) Mirrors flip left and right  
d) Clockwise becomes counter-clockwise  

Q12. What formula computes total count $N$ from left rank $L$ and right rank $R$?  
a) $N = L + R - 1$  
b) $N = L + R$  
c) $N = L + R + 1$  
d) $N = L - R$  

Q13. In a row of 30 people, if A is 10th from left and B is 15th from right, how many people are between A and B?  
a) 5  
b) 6  
c) 4  
d) 7  

Q14. 6 people sit around a circular table. How many total pairs of directly opposite seats exist?  
a) 3 pairs  
b) 6 pairs  
c) 2 pairs  
d) 4 pairs  

Q15. Why should conditional negative clues be placed last during setup?  
a) Negative clues leave multiple open slots, whereas fixed clues eliminate specific slots  
b) Negative clues are illegal  
c) Fixed clues give points  
d) To save ink  

---

## Answers

1. **a) B** — Arrangement: `C - E - B - A - D`. B is in middle.
2. **a) F or E** — Remaining slot on immediate right of A must be filled by F or E.
3. **b) 27th** — $\text{Right Rank} = 40 - 14 + 1 = 27$.
4. **a) C** — D is opposite E. A is between E and F. C cannot be next to E, so C is opposite F.
5. **c) Both a and b** — D is to immediate left of B and opposite to A.
6. **b) Position 5** — In an 8-person circle, opposite of $i$ is $i + 4$. $1 + 4 = 5$.
7. **b) West** — Facing South, your right hand points West.
8. **a) C** — Position 7=B, Position 6=D, Position 5=C. Middle slot (Position 4) is occupied or C is center anchor.
9. **a) 24** — $N = 10 + 15 - 1 = 24$.
10. **b) T** — Arrangement: `T - Q - P - R - S`. T is at extreme left.
11. **a) Facing away from center shifts the observer's relative orientation...** — Orientation reversal.
12. **a) $N = L + R - 1$** — Subtracts the single overcounted person.
13. **a) 5** — $30 - (10 + 15) = 30 - 25 = 5$ people between.
14. **a) 3 pairs** — $N/2 = 6/2 = 3$ opposite pairs.
15. **a) Negative clues leave multiple open slots...** — Prunes choices faster.

---

## Where this appears in the real Accenture test
Appears in Stage 1 & Stage 2: Logical Reasoning section.

---

## Recommended videos
- [PrepInsta Seating Arrangement Guide](https://prepinsta.com/accenture/cognitive/) — Practice questions.
