# Logical Reasoning: Coding-Decoding

## What this is
Coding-Decoding tests your ability to decipher hidden rules, alphabetical shift patterns, reverse letter positions, and numerical symbol substitutions used to encrypt words into code strings. In Accenture assessments, multi-letter shift patterns, matrix coding, and reverse alphabetical positions are tested.

---

## Formula / Rule / Pattern

| Pattern Type | Transformation Rule | Example |
| :--- | :--- | :--- |
| **Direct Alphabet Shift** | Each letter shifted by $+N$ or $-N$ | `CAT` (+1) $\rightarrow$ `DBU` |
| **Reverse Alphabet (Opposite Pair)** | Position $i \leftrightarrow 27 - i$ | `A` (1) $\leftrightarrow$ `Z` (26), `B` (2) $\leftrightarrow$ `Y` (25) |
| **Vowel / Consonant Split** | Vowels$+1$, Consonants$-1$ | `DOG` $\rightarrow$ `CPH` |
| **Word Reversal / Cross Swap** | Swap letters in pairs or reverse string | `BEAT` $\rightarrow$ `EBTA` |

---

## Shortcut: The Fixed 3-Step Pattern Hierarchy

> [!TIP]
> ### Fixed Pattern Search Order
> Test potential coding rules strictly in this fixed 3-step order:
> 
> $$\text{1. Letter Shift (+/-N)} \longrightarrow \text{2. String Reversal / Pair Swap} \longrightarrow \text{3. Alphabet Opposite Pair (27 - Position)}$$
> 
> *Why it works*: Over 80% of corporate assessment questions use simple $+N/-N$ shifts or pair reversals. Checking in this fixed sequence prevents wasting time guessing complex symbol rules.

---

## Worked Examples

### Example 1: Direct Shift (Easy)
- **Question**: If `SYSTEM` is coded as `SYSMET`, how is `FRACTION` coded?
- **Step-by-step Solution**:
  1. Inspect `SYSTEM`: First 3 letters `SYS` unchanged; last 3 letters `TEM` reversed to `MET`.
  2. Apply to `FRACTION`: Split into `FRAC` and `TION`.
  3. Reverse second half: `TION` $\rightarrow$ `NOIT`.
  4. **Code**: `FRACNOIT`.

### Example 2: Letter Shift Pattern (Medium)
- **Question**: In a certain code, `TEACHER` is written as `VGCEJGT`. How is `STUDENT` written in that code?
- **Step-by-step Solution**:
  1. Compare `T` $\rightarrow$ `V` (+2), `E` $\rightarrow$ `G` (+2), `A` $\rightarrow$ `C` (+2).
  2. Rule: Shift every letter by $+2$.
  3. Apply to `STUDENT`:
     - S (+2) $\rightarrow$ U, T (+2) $\rightarrow$ V, U (+2) $\rightarrow$ W, D (+2) $\rightarrow$ F, E (+2) $\rightarrow$ G, N (+2) $\rightarrow$ P, T (+2) $\rightarrow$ V.
  4. **Code**: `UVWGEPV`.

### Example 3: Opposite Pair Sum 27 (Hard)
- **Question**: If `LIGHT` is coded as `OIRTS`, how is `HEAVY` coded?
- **Step-by-step Solution**:
  1. Check positions: L(12) $\rightarrow$ O(15) [Sum = 27]. I(9) $\rightarrow$ R(18) [Sum = 27]. G(7) $\rightarrow$ T(20) [Sum = 27].
  2. Rule: Opposite alphabet letter ($27 - \text{Pos}$).
  3. Apply to `HEAVY`:
     - H(8) $\rightarrow 27-8 = 19$ (S)
     - E(5) $\rightarrow 27-5 = 22$ (V)
     - A(1) $\rightarrow 27-1 = 26$ (Z)
     - V(22) $\rightarrow 27-22 = 5$ (E)
     - Y(25) $\rightarrow 27-25 = 2$ (B)
  4. **Code**: `SVZEB`.

---

## Practice Questions (PYQ Bank)

Q1. If `COMPUTER` is written as `RFUVQNPC`, how is `MEDICINE` written in that code?  
a) EOJDEJFM  
b) MFEJDJOE  
c) EOJDJEFM  
d) EOJDEJME  

Q2. In a code language, `DISTASTE` is written as `132120119205`. What is the position encoding logic?  
a) Alphabet numerical positions  
b) Reverse alphabet numbers  
c) Vowel count  
d) Random digits  

Q3. If `ROSE` is coded as 6821, `CHAIR` as 73456, `PREACH` as 961473, what is the code for `SEARCH`?  
a) 214673  
b) 214763  
c) 241673  
d) 214637  

Q4. If `GIVE` is coded as `5137` and `BAT` is coded as `924`, how is `GATE` coded?  
a) 5247  
b) 5427  
c) 2547  
d) 5724  

Q5. In a certain code, `MONKEY` is written as `XDJMNL`. How is `TIGER` written in that code?  
a) QDFHS  
b) SDFHS  
c) SHFDQ  
d) UJHFS  

Q6. If `A = 2`, `M = 26`, `Z = 52`, what is `BET` coded as?  
a) 44  
b) 54  
c) 64  
d) 36  

Q7. In a code, `ORANGE` is written as `PUBOHF`. What is the transformation?  
a) $+1$ to all letters  
b) $-1$ to all letters  
c) Alternating $+1, -1$  
d) Reverse string  

Q8. If `WATER` is coded as `YCVGT`, what is the code for `FIRE`?  
a) HKTG  
b) HKTF  
c) HKUG  
d) HLUG  

Q9. In a certain code, `123` means "bright little boy", `145` means "tall big boy", and `637` means "beautiful little flower". Which digit means "bright"?  
a) 1  
b) 2  
c) 3  
d) 4  

Q10. If `PALE` is coded as 2134 and `EARTH` is coded as 41590, how is `PEARL` coded?  
a) 24153  
b) 24135  
c) 25130  
d) 24150  

Q11. If `DELHI` is coded as `CCIDD`, how is `BOMBAY` coded?  
a) AMJXVS  
b) AJMTVT  
c) AMJXVT  
d) ABJXVT  

Q12. What is the opposite alphabet pair letter for `K` (11th letter)?  
a) P (16)  
b) Q (17)  
c) O (15)  

Q13. In a code, `TAP` is 39. `LAP` is 31. What is `MAP`?  
a) 32  
b) 34  
c) 36  
d) 38  

Q14. If `FISH` is written as `EHRG`, how is `JUNGLE` written?  
a) ITMFKD  
b) ITNFKD  
c) KVOHMF  
d) ITMFKE  

Q15. Why does $27 - \text{Pos}$ yield the reverse alphabet letter?  
a) Sum of forward position $i$ and reverse position $(27 - i)$ always equals 27 in a 26-letter alphabet  
b) 27 is a prime number  
c) Keyboard layout rule  
d) ASCII offset  

---

## Answers

1. **c) EOJDJEFM** — Reverse the word, then add $+1$ to each letter.
2. **a) Alphabet numerical positions** — Direct letter position matching.
3. **a) 214673** — S=2, E=1, A=4, R=6, C=7, H=3.
4. **a) 5247** — G=5, A=2, T=4, E=7.
5. **a) QDFHS** — Reverse string first (`YEKNOM`), then $-1$ to each letter.
6. **b) 54** — Each letter position doubled. B(2$\times$2=4) + E(5$\times$2=10) + T(20$\times$2=40) $= 54$.
7. **a) $+1$ to all letters** — O+1=P, R+1=U, A+1=B, N+1=O, G+1=H, E+1=F.
8. **a) HKTG** — Shift $+2$ for each letter. F+2=H, I+2=K, R+2=T, E+2=G.
9. **b) 2** — In `123` and `145`, `1` = "boy". In `123` and `637`, `3` = "little". Thus `2` = "bright".
10. **a) 24153** — P=2, E=4, A=1, R=5, L=3.
11. **a) AMJXVS** — Shift pattern: $-1, -2, -3, -4, -5...$
12. **a) P (16)** — $27 - 11 = 16$ (P).
13. **a) 32** — M(13) + A(1) + P(16) $= 30$? Wait: T(20)+A(1)+P(16)=37 (+2=39). L(12)+A(1)+P(16)=29 (+2=31). M(13)+A(1)+P(16)=30 (+2=32). Answer: **32**.
14. **a) ITMFKD** — Shift $-1$ for all letters. J-1=I, U-1=T, N-1=M, G-1=F, L-1=K, E-1=D.
15. **a) Sum of forward position i and reverse position...** — Mathematical definition of complement index.

---

## Where this appears in the real Accenture test
Appears in Stage 1 & Stage 2: Logical Reasoning section.

---

## Recommended videos
- [PrepInsta Logical Reasoning Bank](https://prepinsta.com/accenture/cognitive/) — Coding-decoding practice.
