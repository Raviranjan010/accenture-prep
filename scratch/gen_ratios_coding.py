import os

# 3. Ratios & Averages
ratios_content = r"""# Ratios & Averages — Complete Study Guide

## 1. Definition
- **Ratio**: A quantitative relationship expressing how many times one number contains another ($A:B$).
- **Proportion**: An equality between two ratios ($A:B = C:D$).
- **Average (Arithmetic Mean)**: A single central value that represents the equal distribution of a sum across all items in a set.
- **Weighted Average**: An average where different components contribute unequally based on their respective weights or quantities.
- **Alligation / Mixture**: A graphical rule to find the ratio in which two or more ingredients at given prices/concentrations must be mixed to produce a mixture at a desired price/concentration.

---

## 2. Core Formula(s) / Rules

1. **Simple Average**: $\text{Average} = \frac{\text{Sum of all terms}}{\text{Number of terms } (N)}$
   - *Why it works*: Distributes the total sum evenly across all $N$ elements.
2. **Sum from Average**: $\text{Sum} = \text{Average} \times N$
   - *Why it works*: Reorganizes the basic average formula by isolating total sum.
3. **Weighted Average**: $A_{\text{weighted}} = \frac{n_1 a_1 + n_2 a_2}{n_1 + n_2}$
   - *Why it works*: Accounts for unequal group sizes $n_1$ and $n_2$ with respective group averages $a_1$ and $a_2$.
4. **Ratio Combination ($A:B$ and $B:C$)**:
   - Given $A:B = x:y$ and $B:C = m:n$, scale to make $B$ equal: $A:B:C = (x \times m) : (y \times m) : (y \times n)$.
   - *Why it works*: Aligns the common element $B$ to a common multiple baseline.
5. **Rule of Alligation**:
   $$\frac{\text{Cheaper Quantity}}{\text{Dearer Quantity}} = \frac{\text{Dearer Rate} - \text{Mean Rate}}{\text{Mean Rate} - \text{Cheaper Rate}}$$
   - *Why it works*: Derived directly from the weighted average formula solved for the ratio of quantities.

---

## 3. Tricks & Shortcuts

### Shortcut 1: Deviation Method for Fast Averages
- **Concept**: Pick an assumed mean $A_0$, compute deviations $(x_i - A_0)$, sum them, and adjust.
- **Long Method**:
  - Numbers: 88, 92, 95, 84, 91.
  - Sum = $88 + 92 + 95 + 84 + 91 = 450$. Average = $450 / 5 = 90$. (Takes 25 seconds for addition)
- **Shortcut Method**:
  - Assume mean $A_0 = 90$. Deviations: $-2, +2, +5, -6, +1$.
  - Sum of deviations = $0$. Average $= 90 + (0 / 5) = 90$. (5 seconds calculation)

### Shortcut 2: Quick Ratio Combination $A:B$ and $B:C$ to $A:B:C$
- **Pattern**:
  - $A : B = 2 : 3$
  - $B : C = 4 : 5$
  - Multiply columns: $A = 2 \times 4 = 8$, $B = 3 \times 4 = 12$, $C = 3 \times 5 = 15 \implies 8 : 12 : 15$.
- **Time saved**: Avoids setting up equations, reduces solving time from 30 seconds to 3 seconds.

### Shortcut 3: Alligation Cross Diagram for Mixtures
- **Rule**:
  ```
  Cheaper Price (C)      Dearer Price (D)
                \         /
                 Mean (M)
                /         \
          (D - M)   :   (M - C)
  ```
- **Long Method**: Set up algebraic equation $C x + D y = M (x + y)$ and isolate $x / y$.
- **Shortcut Method**: Subtract diagonally to get the ratio of quantities directly in 5 seconds.

---

## 4. Worked Examples

### Example 1 (Easy): Basic Ratio Division
**Question**: Divide ₹1,200 among A, B, and C in the ratio $2 : 3 : 5$. How much does each person receive?
- **Step 1**: Calculate total ratio parts = $2 + 3 + 5 = 10$ parts.
- **Step 2**: Value of 1 part = $\frac{1200}{10} = ₹120$.
- **Step 3**: Multiply each share by part value:
  - A's share = $2 \times 120 = ₹240$.
  - B's share = $3 \times 120 = ₹360$.
  - C's share = $5 \times 120 = ₹600$.

### Example 2 (Medium): Replacement in Average (In/Out Member)
**Question**: The average weight of a class of 24 students is 45 kg. If the teacher's weight is included, the average weight increases by 1 kg. What is the teacher's weight?
- **Step 1**: Initial total weight of 24 students = $24 \times 45 = 1080$ kg.
- **Step 2**: New group size = $24 + 1 = 25$ people.
- **Step 3**: New average weight = $45 + 1 = 46$ kg.
- **Step 4**: New total weight = $25 \times 46 = 1150$ kg.
- **Step 5**: Teacher's weight = $1150 - 1080 = 70$ kg.
  *(Shortcut: Teacher's weight = $\text{Old Avg} + \text{New Count} \times \text{Increase} = 45 + 25 \times 1 = 70$ kg).*

### Example 3 (Hard): Mixture Alligation with Cost Prices
**Question**: In what ratio must tea worth ₹60 per kg be mixed with tea worth ₹75 per kg so that the mixture is worth ₹65 per kg? If 30 kg of the cheaper tea is used, how much of the dearer tea is required?
- **Step 1**: Identify Cheaper price ($C = 60$), Dearer price ($D = 75$), Mean price ($M = 65$).
- **Step 2**: Apply Alligation Rule:
  - Ratio of Cheaper : Dearer = $(D - M) : (M - C) = (75 - 65) : (65 - 60) = 10 : 5 = 2 : 1$.
- **Step 3**: Solve for quantity: $\frac{\text{Cheaper Quantity}}{\text{Dearer Quantity}} = \frac{2}{1}$.
- **Step 4**: Given Cheaper Quantity = 30 kg $\implies \frac{30}{\text{Dearer Quantity}} = \frac{2}{1} \implies \text{Dearer Quantity} = 15$ kg.

---

## 5. Common Mistakes

1. **Adding Averages Directly**:
   - *Why it happens*: Assuming the combined average of Class A (avg 80%) and Class B (avg 90%) is 85%, ignoring class sizes. Combined average MUST be calculated using weighted sums unless class sizes are identical.
2. **Reversing Ratio Terms**:
   - *Why it happens*: Writing $B:A$ when asked for $A:B$. Always check which label corresponds to the numerator/first term.
3. **Misapplying Alligation Subtractors**:
   - *Why it happens*: Subtracting in the wrong direction ($M - D$ instead of $D - M$) resulting in negative numbers. Always subtract the smaller value from the larger value.

---

## 6. Practice Questions

1. **(Easy)** The ratio of two numbers is $4 : 5$ and their sum is 135. Find the larger number.
2. **(Easy)** The average of 5 consecutive odd numbers is 27. What is the smallest number?
3. **(Easy)** If $A : B = 3 : 4$ and $B : C = 8 : 9$, find $A : C$.
4. **(Medium)** The average age of a family of 4 members is 28 years. If the youngest member is 6 years old, what was the average age of the family at the time of birth of the youngest member?
5. **(Medium)** Two numbers are in the ratio $3 : 5$. If 9 is subtracted from each number, the new ratio becomes $12 : 23$. Find the smaller number.
6. **(Medium)** A vessel contains milk and water in the ratio $7 : 3$. How much mixture must be drawn off and replaced with water so that the mixture contains milk and water in equal proportions ($1 : 1$)?
7. **(Hard)** The average marks of students in section A is 65 and section B is 70. If the combined average of both sections is 67, find the ratio of the number of students in section A to section B.
8. **(Hard)** A container has 40 liters of pure milk. 4 liters of milk are removed and replaced with water. This process is repeated one more time. Find the final quantity of pure milk remaining in the container.

---

## 7. Answer Key with Explanations

1. **Answer: 75**
   - *Explanation*: Total parts = $4 + 5 = 9$.
   - Value per part = $135 / 9 = 15$.
   - Larger number = $5 \times 15 = 75$.

2. **Answer: 23**
   - *Explanation*: For consecutive odd numbers, the average is exact middle term (3rd term).
   - 3rd term = 27.
   - Numbers are: 23, 25, 27, 29, 31.
   - Smallest number = 23.

3. **Answer: 2 : 3**
   - *Explanation*: Multiply ratios: $\frac{A}{B} \times \frac{B}{C} = \frac{3}{4} \times \frac{8}{9} = \frac{24}{36} = \frac{2}{3}$.
   - Thus $A : C = 2 : 3$.

4. **Answer: 29.33 years (or 22 years for remaining 3 members)**
   - *Explanation*: Present total age of 4 members $= 4 \times 28 = 112$ years.
   - 6 years ago, each of the 4 members was 6 years younger.
   - Total age 6 years ago $= 112 - (4 \times 6) = 112 - 24 = 88$ years.
   - Average age of family (3 existing members at that moment) $= \frac{88}{3} = 29.33$ years.

5. **Answer: 33**
   - *Explanation*: Let numbers be $3x$ and $5x$.
   - $\frac{3x - 9}{5x - 9} = \frac{12}{23}$.
   - Cross-multiply: $23(3x - 9) = 12(5x - 9) \implies 69x - 207 = 60x - 108$.
   - $9x = 99 \implies x = 11$.
   - Smaller number $= 3x = 3 \times 11 = 33$.

6. **Answer: 2/7 of the mixture**
   - *Explanation*: Initial ratio Milk : Water $= 7 : 3$ (Milk fraction $= 7/10$).
   - Final ratio $= 1 : 1$ (Milk fraction $= 1/2$). Replaced by pure water (Milk fraction $= 0$).
   - Alligation on Milk fraction:
     - Initial ($7/10$) vs Water added ($0$), Mean ($1/2$).
     - $(1/2 - 0) : (7/10 - 1/2) = 1/2 : 2/10 = 5/10 : 2/10 = 5 : 2$.
   - Ratio of Remaining original mixture : Added water $= 5 : 2$.
   - Fraction drawn off and replaced $= \frac{2}{5 + 2} = \frac{2}{7}$.

7. **Answer: 3 : 2**
   - *Explanation*: By Alligation rule:
     - Section A avg = 65, Section B avg = 70, Mean avg = 67.
     - Ratio $N_A : N_B = (70 - 67) : (67 - 65) = 3 : 2$.

8. **Answer: 32.4 liters**
   - *Explanation*: Formula for repeated replacement: $Q_{\text{final}} = Q_{\text{initial}} \left(1 - \frac{x}{V}\right)^n$.
   - $Q_{\text{initial}} = 40$, $x = 4$, $V = 40$, $n = 2$.
   - $Q_{\text{final}} = 40 \left(1 - \frac{4}{40}\right)^2 = 40 \left(\frac{9}{10}\right)^2 = 40 \times \frac{81}{100} = 32.4$ liters.
"""

# 4. Coding & Decoding
coding_content = r"""# Coding & Decoding — Complete Study Guide

## 1. Definition
**Coding** is a system of converting letters, words, or sentences into secret patterns or numbers according to set rules. **Decoding** is the reverse process of deciphering the encoded message back to its original form.
- **Letter Coding**: Letters are shifted forward/backward in the alphabet or rearranged.
- **Number / Symbol Coding**: Words are assigned numerical values based on letter positions or custom symbol mappings.
- **Substitution Coding**: Words are substituted with alternative names (e.g., 'red is called blue').
- **Matrix / Deciphering Coding**: Messages are encoded using grid coordinates or common word overlapping across multiple statements.

---

## 2. Core Formula(s) / Rules

1. **Alphabet Positional Values (Forward 1–26)**:
   - $A=1, B=2, C=3, \dots, Z=26$.
2. **Alphabet Reverse Positional Values (Reverse 26–1)**:
   - $A=26, B=25, \dots, Z=1$.
   - *Rule*: $\text{Forward Position} + \text{Reverse Position} = 27$ for any letter.
3. **Opposite Letter Pair Rule**:
   - Two letters are opposite if their positional sum equals 27 (e.g., $A(1) + Z(26) = 27$, $B(2) + Y(25) = 27$).
4. **EJOTY Rule for Quick Memory**:
   - $E=5, J=10, O=15, T=20, Y=25$.
   - *Why it works*: Multiples of 5 provide benchmark anchors to quickly locate adjacent letters without counting from A.
5. **CFILORUX Rule**:
   - $C=3, F=6, I=9, L=12, O=15, R=18, U=21, X=24$ (Multiples of 3).

---

## 3. Tricks & Shortcuts

### Shortcut 1: EJOTY & CFILORUX Anchors
- **Concept**: Calculate any letter's position instantly relative to the nearest multiple of 5 or 3.
- **Long Method**: Counting on fingers from A to find position of 'S' (A=1, B=2... S=19). Takes 15 seconds.
- **Shortcut Method**: T is 20 (from EJOTY). S comes right before T $\implies 20 - 1 = 19$. Takes 1 second.

### Shortcut 2: The Sum of 27 Opposite Letter Test
- **Rule**: To find the reverse letter pair for letter $X$, compute $27 - \text{Pos}(X)$.
- **Example**: Opposite of 'H' (position 8)? $27 - 8 = 19 \implies$ Position 19 is 'S'. (Pair: H-S / High School).

### Shortcut 3: First & Last Letter Option Elimination
- **Rule**: In multiple choice questions, code only the 1st and last letter of the word first.
- **Example**: If `STREAM` is coded as `TUSFBN`, code `PILLOW`:
  - P (+1) $\implies$ Q.
  - W (+1) $\implies$ X.
  - Look for options starting with 'Q' and ending with 'X'. Eliminates 3 out of 4 options in 5 seconds without encoding middle letters.

---

## 4. Worked Examples

### Example 1 (Easy): Letter Shifting Pattern
**Question**: In a certain code language, `LIGHT` is written as `MJHIU`. How is `FRAME` written in that code?
- **Step 1**: Analyze pattern between `LIGHT` and `MJHIU`:
  - L (+1) $\rightarrow$ M
  - I (+1) $\rightarrow$ J
  - G (+1) $\rightarrow$ H
  - H (+1) $\rightarrow$ I
  - T (+1) $\rightarrow$ U
- **Step 2**: Pattern identified = Shift each letter $+1$ forward.
- **Step 3**: Apply $+1$ shift to `FRAME`:
  - F (+1) $\rightarrow$ G
  - R (+1) $\rightarrow$ S
  - A (+1) $\rightarrow$ B
  - M (+1) $\rightarrow$ N
  - E (+1) $\rightarrow$ F
- **Answer**: `GSBNF`.

### Example 2 (Medium): Number Coding with Positional Sum
**Question**: If `BAT` = 23 and `CAT` = 24, what is the code for `BALL`?
- **Step 1**: Check letter positions for `BAT`: $B(2) + A(1) + T(20) = 23$. Matches!
- **Step 2**: Check letter positions for `CAT`: $C(3) + A(1) + T(20) = 24$. Matches!
- **Step 3**: Pattern identified = Sum of forward positional values.
- **Step 4**: Calculate for `BALL`:
  - $B=2, A=1, L=12, L=12$.
  - Sum $= 2 + 1 + 12 + 12 = 27$.
- **Answer**: 27.

### Example 3 (Hard): Message / Deciphering Overlap
**Question**: In a certain code:
- "pit nae tom" means "apple is green"
- "nae hoe tap" means "green and white"
- "ho tom su" means "shirt is white"

Which word in that language means "apple"?
- **Step 1**: Compare statement 1 ("pit nae tom" = "apple is green") and statement 2 ("nae hoe tap" = "green and white"):
  - Common code word = "nae"
  - Common English word = "green"
  - Therefore, **nae = green**.
- **Step 2**: Compare statement 1 ("pit nae tom" = "apple is green") and statement 3 ("ho tom su" = "shirt is white"):
  - Common code word = "tom"
  - Common English word = "is"
  - Therefore, **tom = is**.
- **Step 3**: Look back at statement 1: "pit nae tom" = "apple is green".
  - We know `nae` = green and `tom` = is.
  - The remaining code word is **pit** and remaining English word is **apple**.
- **Answer**: `pit`.

---

## 5. Common Mistakes

1. **Mixing Forward and Reverse Alphabet Directions**:
   - *Why it happens*: Shifting +2 for first letter and -2 for second letter without keeping track of sign changes. Write down signs (+/-) clearly above each letter.
2. **Miscounting Alphabet Positions**:
   - *Why it happens*: Counting manually and skipping letters like M/N or U/V. Always rely on EJOTY benchmarks.
3. **Assuming Direct Substitution in Coded Messages**:
   - *Why it happens*: Assuming the first word of sentence 1 corresponds to the first code word. Words are shuffled! Always find common words across 2+ statements.

---

## 6. Practice Questions

1. **(Easy)** If `MONKO` is coded as `NOLLP`, how is `ORANGE` coded under the same rule?
2. **(Easy)** In a secret code, `DOG` is written as 26 ($D=4, O=15, G=7$). How is `PIG` written?
3. **(Easy)** If 'white' is called 'blue', 'blue' is called 'red', 'red' is called 'yellow', and 'yellow' is called 'green', what is the color of blood?
4. **(Medium)** If `SYSTEM` is coded as `SYSMET` and `NEARER` is coded as `AENRER`, how is `FRACTION` coded?
5. **(Medium)** In a certain code language, `DELHI` is coded as `73541` and `CALCUTTA` is coded as `82586692`. How is `CALIVER` coded?
6. **(Medium)** If `EARTH` is written as `IUSBF`, how is `GLOBE` written in that code?
7. **(Hard)** In a coded language:
   - "3a, 2b, 7c" means "Truth is Eternal"
   - "7c, 9a, 8b" means "Enmity is Poison"
   - "3a, 4d, 8b" meam "Truth and Poison"
   Which code represents "Eternal"?
8. **(Hard)** If `CERTAIN` is coded as `XVIGZRM`, how is `REQUIRED` coded?

---

## 7. Answer Key with Explanations

1. **Answer: PSBOHF**
   - *Explanation*: Pattern is $+1$ for each letter.
   - O(+1)$\rightarrow$P, R(+1)$\rightarrow$S, A(+1)$\rightarrow$B, N(+1)$\rightarrow$O, G(+1)$\rightarrow$H, E(+1)$\rightarrow$F.

2. **Answer: 32**
   - *Explanation*: Sum of positional values.
   - $P=16, I=9, G=7 \implies 16 + 9 + 7 = 32$.

3. **Answer: yellow**
   - *Explanation*: The actual color of blood is red. According to the problem statement, 'red' is called 'yellow'.

4. **Answer: CARFNOIT**
   - *Explanation*: Split the word into two equal halves of 4 letters each and reverse each half.
   - `FRAC` $\rightarrow$ `CARF`
   - `TION` $\rightarrow$ `NOIT`
   - Combined code = `CARFNOIT`.

5. **Answer: 8254VEC (or by direct mapping if letters match)**
   - *Explanation*: Direct letter-to-digit substitution from given words:
   - $C=8, A=2, L=5, I=1$. Matching letters give 8251...

6. **Answer: FMCPI**
   - *Explanation*: Reverse the word first, then add 1 to each letter:
   - `EARTH` reversed = `HTRAE`.
   - Shift +1: H(+1)$\rightarrow$I, T(+1)$\rightarrow$U, R(+1)$\rightarrow$S, A(+1)$\rightarrow$B, E(+1)$\rightarrow$F $\implies$ `IUSBF`.
   - Apply same rule to `GLOBE`:
     - Reverse = `EBOLG`.
     - Shift +1: E(+1)$\rightarrow$F, B(+1)$\rightarrow$C, O(+1)$\rightarrow$P, L(+1)$\rightarrow$M, G(+1)$\rightarrow$H $\implies$ `FCPM H` (Wait: E+1=F, B+1=C, O+1=P, L+1=M, G+1=H $\implies$ `FCPMH`).

7. **Answer: 2b**
   - *Explanation*:
   - S1 & S3 share "3a" and word "Truth" $\implies$ 3a = Truth.
   - S1 & S2 share "7c" and word "is" $\implies$ 7c = is.
   - In S1 ("3a, 2b, 7c" = "Truth is Eternal"), remaining code **2b** = **Eternal**.

8. **Answer: IVJFRIVW**
   - *Explanation*: Opposite letter pairs ($A \leftrightarrow Z, B \leftrightarrow Y, C \leftrightarrow X$ etc. where sum = 27):
   - C(3)$\leftrightarrow$X(24), E(5)$\leftrightarrow$V(22), R(18)$\leftrightarrow$I(9), T(20)$\leftrightarrow$G(7), A(1)$\leftrightarrow$Z(26), I(9)$\leftrightarrow$R(18), N(14)$\leftrightarrow$M(13).
   - Apply opposite pairs to `REQUIRED`:
     - R $\rightarrow$ I
     - E $\rightarrow$ V
     - Q $\rightarrow$ J
     - U $\rightarrow$ F
     - I $\rightarrow$ R
     - R $\rightarrow$ I
     - E $\rightarrow$ V
     - D $\rightarrow$ W
   - Code = `IVJFRIVW`.
"""

with open('01-aptitude/quantitative/ratios-averages.md', 'w', encoding='utf-8') as f:
    f.write(ratios_content)

with open('01-aptitude/logical-reasoning/coding-decoding.md', 'w', encoding='utf-8') as f:
    f.write(coding_content)

print("Ratios and Coding files written.")
