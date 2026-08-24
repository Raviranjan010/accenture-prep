# Coding & Decoding — Complete Study Guide

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
