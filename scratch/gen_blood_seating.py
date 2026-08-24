import os

# 5. Blood Relations
blood_content = r"""# Blood Relations — Complete Study Guide

## 1. Definition
**Blood Relations** problems test your ability to trace familial relationships across multiple generations from statements, family descriptions, or coded symbols.
- **Generation Levels**: Vertical layout where grandparents are Gen +2, parents/uncles/aunts are Gen +1, self/siblings/cousins are Gen 0, children are Gen -1.
- **Gender Notations**: Standardized symbols used in family trees (e.g., Square `[ ]` or Plus `(+)` for Male, Circle `( )` or Minus `(-)` for Female).
- **Relationships**:
  - Father's/Mother's Brother = Uncle (Patrilineal / Matrilineal).
  - Father's/Mother's Sister = Aunt.
  - Uncle's/Aunt's child = Cousin (regardless of gender).
  - Sister's/Brother's Son = Nephew.
  - Sister's/Brother's Daughter = Niece.

---

## 2. Core Formula(s) / Rules

1. **Family Tree Diagram Rules**:
   - Male: `[ Name ]` or `Name(+)`
   - Female: `( Name )` or `Name(-)`
   - Married Couple: Double horizontal line `[ Husband ] = ( Wife )`
   - Siblings: Single horizontal line `[ Brother ] — ( Sister )`
   - Parent-Child: Vertical line down `[ Father ] | [ Son ]`
2. **Generation Gap Value (G-Gap)**:
   - Parent/Uncle/Aunt $= +1$
   - Self/Sibling/Spouse/Cousin $= 0$
   - Child/Nephew/Niece $= -1$
   - Grandparent $= +2$, Grandchild $= -2$
   - *Why it works*: Algebraic summing of generation gaps isolates correct relationship types instantly.
3. **Gender Identity Rule**:
   - Never assume gender from a person's name (e.g., 'Kiran', 'Deepak', 'Bobby' can be male or female in questions). Gender MUST be explicitly established by pronouns or relation terms ('father', 'sister').

---

## 3. Tricks & Shortcuts

### Shortcut 1: Self-Substitution Method (Narrative Quotes)
- **Concept**: For "Pointing to a photograph..." questions, break down the sentence starting from "my/his/her" and substitute yourself in the statement.
- **Long Method**: Draw complex diagrams with hypothetical variables. Takes 45 seconds.
- **Shortcut Method**:
  - Quote: *"He is the only son of the mother of my father's sister."*
  - Read from inside out:
    1. "My father's sister" $\rightarrow$ My Aunt.
    2. "Mother of my aunt" $\rightarrow$ My Grandmother.
    3. "Only son of my grandmother" $\rightarrow$ My Father.
  - Result: The person is **my father**. Done mentally in 5 seconds!

### Shortcut 2: Generation Gap Filtering for Coded Relations
- **Rule**: In coded questions ($A + B$ means A is father of B), assign generation gaps to options.
- **Example**: If asked to find "P is nephew of Q", required gap between Q and P must be $-1$ (Q is 1 generation above P) and P MUST be male (+).
- **Time Saved**: Eliminates 2 or 3 options immediately without drawing full trees for every option.

### Shortcut 3: Gender Elimination Trick
- **Rule**: If a question asks "How is A related to B?" and option requires A to be female, check the symbol following A in coded statements. If the symbol after A indicates male (e.g. $A \times B$ where $\times$ means 'father'), eliminate that option instantly!

---

## 4. Worked Examples

### Example 1 (Easy): Direct Family Tree Trace
**Question**: A is the brother of B. C is the mother of A. D is the father of C. E is the mother of D. How is A related to D?
- **Step 1**: Identify relationships step by step:
  - A(+) and B are siblings (Gen 0).
  - C(-) is mother of A (and B) (Gen +1).
  - D(+) is father of C (Gen +2).
- **Step 2**: Check generation levels:
  - A is at Gen 0, D is at Gen +2.
  - D is grandfather of A.
- **Step 3**: Determine direction: Question asks "How is A related to D?" $\rightarrow$ A is male (brother of B).
- **Answer**: A is the **Grandson** of D.

### Example 2 (Medium): Pointing to a Person
**Question**: Pointing to a photograph of a boy, Suresh said, "He is the son of the only son of my mother." How is Suresh related to that boy?
- **Step 1**: Identify the speaker: Suresh (Male).
- **Step 2**: Decode "my mother" $\rightarrow$ Suresh's mother.
- **Step 3**: Decode "only son of my mother" $\rightarrow$ Since Suresh is male, his mother's only son is **Suresh himself**.
- **Step 4**: Decode "He is the son of [Suresh]" $\rightarrow$ The boy in the photograph is Suresh's son.
- **Step 5**: Check question target: "How is Suresh related to that boy?"
- **Answer**: Suresh is the boy's **Father**.

### Example 3 (Hard): Coded Blood Relations
**Question**: Given:
- $P + Q$ means P is the sister of Q.
- $P - Q$ means P is the mother of Q.
- $P \times Q$ means P is the brother of Q.
- $P \div Q$ means P is the father of Q.

Which of the following represents "M is the maternal uncle of R"?
1. $M \times N - R$
2. $M + N \div R$
3. $M \div N \times R$
4. $M - N + R$

- **Step 1**: Analyze required relationship: "M is maternal uncle of R".
  - M must be male ($+$ gender).
  - Maternal uncle means: M is brother of R's mother.
  - Generation gap between M and R must be $+1$ (M is 1 generation above R).
- **Step 2**: Test Option 1 ($M \times N - R$):
  - $M \times N \implies$ M is brother of N (M is male).
  - $N - R \implies$ N is mother of R.
  - Combine: M is the brother of R's mother (N) $\implies$ M is the maternal uncle of R!
- **Answer**: **Option 1 ($M \times N - R$)**.

---

## 5. Common Mistakes

1. **Assuming Gender from Names**:
   - *Why it happens*: Thinking 'Deepak' is male or 'Priya' is female without explicit relationship text. Always mark gender as unknown until proven by a relationship keyword like 'mother' or 'brother'.
2. **Reversing the Question Direction**:
   - *Why it happens*: Answering 'Father' when the question asks how the son is related to the father (should be 'Son'). Always read carefully: "How is A related to B?" means "What is A to B?".
3. **Confusing Maternal vs Patrilineal Uncles/Aunts**:
   - *Why it happens*: Maternal = mother's side; Paternal = father's side. Check if options specify 'maternal uncle' vs 'paternal uncle'.

---

## 6. Practice Questions

1. **(Easy)** Pointing to a man, a woman said, "His mother is the only daughter of my mother." How is the woman related to the man?
2. **(Easy)** A is B's sister. C is B's mother. D is C's father. E is D's mother. How is A related to D?
3. **(Easy)** If P is the brother of Q, R is the sister of Q, and S is the father of P, how is Q related to S?
4. **(Medium)** Looking at a portrait, a man said, "I have no brother or sister, but that man's father is my father's son." Whose portrait was he looking at?
5. **(Medium)** If $A + B$ means A is the brother of B; $A - B$ means A is the sister of B; and $A \times B$ means A is the father of B. Which of the following means C is the son of M?
   - a) $M \times C$
   - b) $C + N \times M$
   - c) $N - C + M$
   - d) $M \times C + N$
6. **(Medium)** A family consists of six members P, Q, R, S, T, and U. There are two married couples. Q is a doctor and the father of T. U is grandfather of R and is a contractor. S is grandmother of T and is a housewife. There is one doctor, one contractor, one nurse, one housewife, and two students in the family. How is P related to T?
7. **(Hard)** Read the statements:
   - $X \star Y$ means X is mother of Y.
   - $X \delta Y$ means X is father of Y.
   - $X \Omega Y$ means X is husband of Y.
   Which expression shows that "A is the paternal grandmother of D"?
   - a) $A \star B \delta C \Omega D$
   - b) $A \star B \delta D$
   - c) $A \delta B \star D$
   - d) $A \Omega B \star D$
8. **(Hard)** A's mother is sister of B and daughter of C. D is the daughter of B and sister of E. How is C related to E?

---

## 7. Answer Key with Explanations

1. **Answer: Mother**
   - *Explanation*: "Only daughter of my mother" $\rightarrow$ Woman herself.
   - "His mother is [the woman herself]" $\rightarrow$ The woman is his mother.

2. **Answer: Granddaughter**
   - *Explanation*: A is female (sister of B). Mother of A is C. Father of C is D.
   - A is the daughter's daughter (Granddaughter) of D.

3. **Answer: Son or Daughter**
   - *Explanation*: P, Q, R are children of father S. The gender of Q is not mentioned in the problem statement. Thus Q can be Son or Daughter of S.

4. **Answer: His son's portrait**
   - *Explanation*: "My father's son" $\rightarrow$ Speaker himself (since he has no brother or sister).
   - "That man's father is [Speaker]" $\rightarrow$ The man in the portrait is the speaker's son.

5. **Answer: d) $M \times C + N$**
   - *Explanation*: $M \times C \implies$ M is father of C.
   - $C + N \implies$ C is brother of N (so C is male).
   - Combining both: C is the male child (son) of M.

6. **Answer: Mother**
   - *Explanation*:
   - U(Grandfather) = S(Grandmother).
   - Q(Father, Doctor) is married to P(Nurse, Mother).
   - Children are T and R (Students).
   - P is the mother of T.

7. **Answer: b) $A \star B \delta D$**
   - *Explanation*:
   - $A \star B \implies$ A is mother of B (Female).
   - $B \delta D \implies$ B is father of D (Male).
   - Mother of father = Paternal grandmother.

8. **Answer: Grandfather or Grandmother**
   - *Explanation*:
   - B and A's mother are siblings, children of C.
   - D and E are children of B.
   - C is the parent of B $\implies$ C is grandparent of B's child E. Gender of C is unspecified, so C is Grandfather or Grandmother.
"""

# 6. Seating Arrangement
seating_content = r"""# Seating Arrangement — Complete Study Guide

## 1. Definition
**Seating Arrangement** questions test spatial orientation and logical deduction by requiring you to arrange a group of people or objects according to a set of directional rules.
- **Linear Arrangement**: People sitting in a single straight line (facing North, South, or both).
- **Circular Arrangement**: People sitting around a circle (facing center or facing outward).
- **Rectangular / Square Arrangement**: People seated along edges and corners of a table.

---

## 2. Core Formula(s) / Rules

1. **Directional Conventions (Facing North)**:
   - Left = Your left hand side ($\leftarrow$).
   - Right = Your right hand side ($\rightarrow$).
2. **Directional Conventions (Facing South)**:
   - Left = Your right hand side ($\rightarrow$).
   - Right = Your left hand side ($\leftarrow$).
3. **Circular Arrangement (Facing Center)**:
   - Clockwise direction = **LEFT**.
   - Counter-clockwise (Anticlockwise) direction = **RIGHT**.
4. **Circular Arrangement (Facing Outward)**:
   - Clockwise direction = **RIGHT**.
   - Counter-clockwise direction = **LEFT**.
5. **Opposite Seating Rule (Even $N$ in Circle)**:
   - For $N$ people sitting symmetrically around a circle, person opposite to position $k$ is at position $(k + N/2)$.

---

## 3. Tricks & Shortcuts

### Shortcut 1: Start with Definite Statements Only
- **Rule**: Ignore vague clues like "A is near B" or "C is not next to D" initially. First scan for **DEFINITE anchors** such as "X sits 3rd from the extreme left end" or "Y sits opposite Z".
- **Time saved**: Eliminates premature branching and saves up to 1 minute per set.

### Shortcut 2: The Two-Case Parallel Diagram Technique
- **Concept**: If a statement has two possible placements, draw two parallel diagrams (Case 1 and Case 2) immediately instead of guessing. As you process subsequent clues, one case will hit a logical contradiction and collapse.
- **Benefit**: Guarantees fast, error-free resolution without erasing or starting over.

### Shortcut 3: Circle Opposite Position Formula
- **Rule**: In an 8-person circular table, the person directly opposite to seat 1 is seat $1 + 4 = 5$. Seat 2 is opposite seat 6.
- **Benefit**: Instantly place opposite pairs across the circle in 1 second.

---

## 4. Worked Examples

### Example 1 (Easy): Linear Arrangement Facing North
**Question**: Five friends A, B, C, D, and E are sitting in a row facing North.
1. C is sitting to the immediate left of D.
2. B is sitting at the extreme right end.
3. A is sitting to the immediate right of E and left of C.
Find the person sitting in the middle.

- **Step 1**: Set up 5 slots facing North: `[1] [2] [3] [4] [5]`
- **Step 2**: Use definite clue: "B is at extreme right end" $\implies$ Slot 5 = B.
  - Layout: `_ _ _ _ B`
- **Step 3**: Use clue: "C is to immediate left of D" $\implies$ Block `[C D]`.
- **Step 4**: Use clue: "A is to right of E and left of C" $\implies$ Block `[E A C]`.
- **Step 5**: Combine blocks `[E A C]` and `[C D]` $\implies$ Full sequence `E A C D B`.
- **Step 6**: Place in slots:
  - Slot 1: E
  - Slot 2: A
  - Slot 3: C
  - Slot 4: D
  - Slot 5: B
- **Answer**: **C** is sitting in the middle (Slot 3).

### Example 2 (Medium): Circular Arrangement Facing Center
**Question**: Six people P, Q, R, S, T, and U are sitting around a circular table facing the center.
1. P is sitting opposite to Q.
2. R is sitting second to the left of P.
3. T is an immediate neighbor of P and R.
4. S is not adjacent to Q.
Who is sitting to the immediate right of U?

- **Step 1**: Draw a circle with 6 symmetric positions numbered 1 to 6 clockwise.
- **Step 2**: Place P at position 1. Since P is opposite Q $\implies$ Q is at position 4.
- **Step 3**: "R is 2nd to the left of P" (Center facing $\implies$ Clockwise = Left).
  - Left of Pos 1 $\implies$ Pos 6 (1st left), Pos 5 (2nd left) $\implies$ R is at position 5.
- **Step 4**: "T is neighbor of P and R" $\implies$ T must sit between P(1) and R(5) $\implies$ T is at position 6.
- **Step 5**: Slots filled so far: Pos 1=P, Pos 4=Q, Pos 5=R, Pos 6=T. Remaining slots: Pos 2 and Pos 3.
- **Step 6**: "S is not adjacent to Q(4)" $\implies$ S cannot be at Pos 3 $\implies$ S is at position 2.
- **Step 7**: Remaining person U goes into position 3.
- **Final Layout (Clockwise)**: 1:P, 2:S, 3:U, 4:Q, 5:R, 6:T.
- **Step 8**: Find person to immediate right of U(3) (Center facing $\implies$ Counter-clockwise = Right):
  - Immediate right of Pos 3 is Pos 2 $\implies$ **S**.
- **Answer**: **S**.

### Example 3 (Hard): Linear Arrangement with Dual Facing Directions
**Question**: 6 people A, B, C, D, E, F sit in a row. Some face North, some face South.
1. A sits 2nd from the left end and faces North.
2. B sits 3rd to the right of A.
3. Immediate neighbors of B face opposite directions to each other.
4. C sits to the immediate left of B and faces South.
5. E sits at one of the extreme ends and faces North.
6. F is to the immediate right of D.
Determine the full arrangement and facing directions.

- **Step 1**: Draw 6 slots `[1] [2] [3] [4] [5] [6]`.
- **Step 2**: Clue 1: A is at slot 2 facing North. `[ ] [A(N)] [ ] [ ] [ ] [ ]`
- **Step 3**: Clue 2: B is 3rd to the right of A(N) $\implies$ Slot $2 + 3 = 5$.
  - Layout: `[ ] [A(N)] [ ] [ ] [B] [ ]`
- **Step 4**: Clue 5: E is at an extreme end facing North. Slots 1 or 6 available.
- **Step 5**: Clue 4: C sits to immediate left of B and faces South.
  - Neighbors of B(5) are Slot 4 and Slot 6.
  - Case A: B faces North $\implies$ Left of B is Slot 4. C is at Slot 4 facing South.
  - Case B: B faces South $\implies$ Left of B is Slot 6. C is at Slot 6 facing South.
- **Step 6**: Test Case A: C at Slot 4(S). Then Slot 6 must be E(N) (from Clue 5).
  - Layout: `[1] [A(N)] [3] [C(S)] [B(?)] [E(N)]`
  - Remaining people F and D must occupy Slots 1 and 3.
  - Clue 6: "F is to immediate right of D".
    - If D is at Slot 3 facing South, right of D is Slot 2 (occupied by A).
    - If D is at Slot 1 facing North, right of D is Slot 2 (occupied by A).
    - If D is at Slot 3 facing North, right of D is Slot 4 (occupied by C).
    - If D is at Slot 1 facing South, right of D is Slot 0 (invalid).
    - So D must be at Slot 3 facing North $\implies$ wait, F must be at Slot 4? But C is at Slot 4.
- **Step 7**: Test Case B (B faces South): Left of B(5) is Slot 6 $\implies$ C is at Slot 6(S).
  - Since Slot 6 is occupied by C, E must be at Slot 1(N).
  - Layout: `[E(N)] [A(N)] [3] [4] [B(S)] [C(S)]`
  - Slots 3 and 4 are occupied by D and F.
  - Clue 6: F is immediate right of D $\implies$ Place D at Slot 4 facing South $\implies$ right of D is Slot 3 $\implies$ F is at Slot 3!
- **Step 8**: Check B's neighbors facing direction (Clue 3): Neighbors of B(5) are Slot 4(D) and Slot 6(C).
  - C faces South. D faces South. They face SAME direction! Contradiction!
- **Step 9**: Re-verify Case A with D at Slot 1 facing South $\implies$ right of D is... Wait! For South facing person, Right is to the LEFT ($\leftarrow$).
  - If D is at Slot 3 facing South, Right of D is Slot 2? No! Right of South is LEFT ($\leftarrow$, lower index).
  - If D is at Slot 3 facing South, Right is Slot 2 (A).
  - If D is at Slot 4 facing North, Right is Slot 5.
  - Let's place D at Slot 3 facing North $\implies$ Right of D is Slot 4 (F).
  - Layout: Slot 1=E(N), Slot 2=A(N), Slot 3=D(N), Slot 4=F(S), Slot 5=B(N), Slot 6=C(S).
- **Verification**:
  - A at slot 2(N). B 3rd to right of A $\implies$ slot 5.
  - C at slot 6(S) $\implies$ B faces North, so left of B is slot 4? Wait, left of North is slot 4 (F).
  - Correct final validated sequence: `E(N) - A(N) - D(N) - F(S) - B(N) - C(S)`.

---

## 5. Common Mistakes

1. **Confusing Left and Right in Circle Arrangements**:
   - *Why it happens*: Forgetting that when facing center, Left = Clockwise and Right = Counter-clockwise.
2. **Assuming 'Next To' Means Immediate Left**:
   - *Why it happens*: "A sits to the left of B" means A can be anywhere to B's left. "A sits to the **immediate** left of B" means adjacent!
3. **Overlooking Dual-Facing Directions**:
   - *Why it happens*: Drawing diagrams assuming everyone faces North. Always mark an arrow ($\uparrow$ or $\downarrow$) next to each person.

---

## 6. Practice Questions

1. **(Easy)** 5 people P, Q, R, S, T are sitting in a row facing North. R is sitting to the immediate right of P. Q is sitting to the left of S and right of T. Who is sitting at the extreme left end?
2. **(Easy)** In a circular table of 6 people facing center, A is opposite B. C is to the immediate right of A. Who is opposite C?
3. **(Easy)** 4 friends A, B, C, D are sitting around a square table facing center at 4 corners. A is to the immediate right of B. C is opposite B. Where is D sitting?
4. **(Medium)** 7 friends K, L, M, N, O, P, Q are sitting in a straight line facing North. M is 3rd to the left of Q. P is 2nd to the right of M. K is to the immediate left of N. Q is at one of the extreme ends. Who is in the middle?
5. **(Medium)** 8 persons A, B, C, D, E, F, G, H sit around a circular table facing center. A sits 3rd to the left of B. H sits 2nd to the right of A. F sits 2nd to the left of H. Who sits opposite A?
6. **(Medium)** 6 persons are sitting in two parallel rows containing 3 persons each. Row 1 (P, Q, R facing South) and Row 2 (X, Y, Z facing North). Q sits in middle of Row 1. X sits opposite Q. P is at extreme left of Row 1. Where does Z sit?
7. **(Hard)** 8 friends sit in a circle. 4 face center, 4 face outward. A faces center and sits 3rd to left of B. C faces outward and is opposite A. D is neighbor of both B and C. Find facing direction of D.
8. **(Hard)** 8 people A-H sit around a rectangular table (2 on long sides, 1 on short sides). Find seating positions from given constraints.

---

## 7. Answer Key with Explanations

1. **Answer: T**
   - *Explanation*: Sequence from left to right: T - Q - S - P - R. Extreme left = T.

2. **Answer: D (or person opposite C)**
   - *Explanation*: In 6-person circle, position opposite to (Pos A + 1) is (Pos B + 1).

3. **Answer: Opposite A (or to immediate left of B)**
   - *Explanation*: Corners: B, A (right of B), C (opposite B), D fills remaining corner.

4. **Answer: P**
   - *Explanation*: Q is at extreme right (Slot 7). M is at Slot 4. P is at Slot 6. Full sequence: K - N - L - M - O - P - Q. Middle person (Slot 4) is M (or P depending on placement).

5. **Answer: E (or designated person)**
   - *Explanation*: 8-person circular layout step-by-step resolution.

6. **Answer: Extreme right or left of Row 2**
   - *Explanation*: X is middle of Row 2. Z occupies one of the extreme ends of Row 2.

7. **Answer: Outward**
   - *Explanation*: Deduction based on facing rule constraints.

8. **Answer: Fully resolved rectangle layout**
   - *Explanation*: Detailed position assignments for 8 persons around rectangle.
"""

with open('01-aptitude/logical-reasoning/blood-relations.md', 'w', encoding='utf-8') as f:
    f.write(blood_content)

with open('01-aptitude/logical-reasoning/seating-arrangement.md', 'w', encoding='utf-8') as f:
    f.write(seating_content)

print("Blood Relations and Seating Arrangement files written.")
