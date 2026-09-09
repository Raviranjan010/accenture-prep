# Accenture Cognitive Assessment: Quick-Fire Math (Select Bubbles) Master Guide

> **Target Assessment**: Accenture Recruitment — Stage 1: Gamified Cognitive Assessment (Aon / cut-e & SHL Platforms)  
> **Topic**: Rapid Numerical Agility, Mental Math Approximations, Fraction-to-Decimal Recall & Bubble Ordering  
> **Repository Target**: `03-quick-fire-math.md`  
> **Language**: Hinglish (In-Depth, Real Exam Timing, Concept-Focused, Zero Fluff)

---

## 1. Game Overview & Assessment Engine Mechanism

**Quick-Fire Math** (jise *Select Bubbles*, *Bubble Maths*, ya *Numerical Sprint* bhi kaha jata hai) Accenture ke Cognitive Assessment ka ek rapid-fire elimination mini-game hai. Screen par floating ya static circular bubbles aate hain jinke andar math expressions (addition, subtraction, multi-digit division, fractions, decimals, percentage of numbers) likhe hote hain.

Aapko in bubbles ko evaluate karke **Strict Ascending Order (Lowest to Highest)** ya **Descending Order (Highest to Lowest)** me rapidly click/pop karna hota hai.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CORE GAME LOOP                                        │
│                                                                                         │
│   [ Bubble A ]              [ Bubble B ]              [ Bubble C ]       [ Bubble D ]   │
│     14 + 18                    45 / 3                    7 × 6           30% of 120     │
│      (= 32)                    (= 15)                    (= 42)            (= 36)       │
│                                                                                         │
│   Ascending Order Click Sequence:                                                       │
│   1st: Bubble B (15) ──▶ 2nd: Bubble A (32) ──▶ 3rd: Bubble D (36) ──▶ 4th: Bubble C (42)│
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### Actual Exam Constraints & Format (KN Academy Verified Data)
- **Total Questions**: **24 Questions** back-to-back aate hain.
- **Timer per Question**: Har question ke liye screen par **14 seconds ka strict timer** chalta hai. Agar 14 seconds me solve nahi kiya, to question automatically skip ho jata hai aur next question load ho jata hai.
- **Passing Target**: 24 me se minimum **18 se 20 questions 100% accuracy** ke sath correctly solve karne hote hain high-percentile score band me aane ke liye.
- **Cognitive Skills Tested**: Mental numerical processing speed, executive decision-making under time pressure, and rapid magnitude comparison without scratchpad math.

---

## 2. Essential Mental Math Shortcuts & Fast Estimation Hacks

### Hack 1: The Nearest-10 Benchmark & Gap Elimination Trick

Har bubble ki exact calculation paper-pen leke karne baithoge toh 14 seconds nikal jayenge. Hamesha **Boundary Benchmarking** use karo:

```
Full Calculation (Time Wasting):
Bubble A: 7 × 6 = 42
Bubble B: 45 / 3 = 15
Time taken: 4-5 seconds calculation + mental strain

Benchmark Estimation (Lightning Fast):
Bubble A: 7 × 6 is clearly in the ~40 range
Bubble B: 45 / 3 is roughly in the ~15 range
Instant Insight: 15 < 40 (Difference > 25) -> Zero paper-work needed!
```

> [!TIP]
> **Tie-Breaker Rule:** Exact detailed calculation sirf un do bubbles ke beech karo jo aapas me bohot close dikh rahe hon (e.g., 42 vs 45). Baki 1–2 bubbles jo clearly bohot chhote ya bade hain, unhe direct range dekh kar eliminate kar do.

---

### Hack 2: Negative vs Positive Separation Trick

Actual exam me aisi mixed expressions aati hain jahan signs ka game hota hai (e.g., $4 - 5$, $11 - 13$, $0 + 3$):
1. **Pehle Sign Scan Karo**:
   - $4 - 5 = -1$ (Negative)
   - $11 - 13 = -2$ (Negative)
   - $0 + 3 = +3$ (Positive $\implies$ Clearly highest!)
2. **Negative Comparison Logic**: Negative numbers me jo magnitude me bada hota hai, uski actual numerical value sabse chhoti hoti hai:
   $$-2 < -1 < +3 \implies \text{Order: } (11-13) \longrightarrow (4-5) \longrightarrow (0+3)$$
   Is predictive scanning se question 3 seconds ke andar solve ho jata hai.

---

### Hack 3: Decimal & Multiplier Rules ($< 1$ vs $> 1$)

Jab points/decimals wale expressions aate hain (jaise $2.1 \times 0.75$):
- Kisi number ko agar **$< 1$** (jaise $0.75, 0.5, 0.8$) se multiply karoge, to result hamesha original number se **chhota** aayega:
  $$2.1 \times 0.75 < 2.1$$
- Kisi number ko agar **$> 1$** (jaise $1.2, 1.5$) se multiply karoge, to result hamesha original number se **bada** aayega.
- Is rule se bina point multiplication kare direct ranking mil jati hai.

---

### Hack 4: Must-Remember Fraction-to-Decimal Conversion Table

Actual questions me fractions aate hain (e.g., $\frac{3}{4} - \frac{1}{2}$ vs $\frac{6}{7}$). Agar ye values dimag me ready hongi, to direct decimal addition ho jayega:

| Fraction | Decimal Equivalent | Percentage Equivalent | Exam Shortcut / Memory Anchor |
| :---: | :---: | :---: | :--- |
| $\frac{1}{2}$ | **0.50** | $50\%$ | Half / Seedha aadha |
| $\frac{1}{3}$ | **0.333** | $33.33\%$ | One-third / Lagbhag 0.33 |
| $\frac{2}{3}$ | **0.667** | $66.67\%$ | Two-thirds / Lagbhag 0.67 |
| $\frac{1}{4}$ | **0.25** | $25\%$ | Quarter / Ek chauthai |
| $\frac{3}{4}$ | **0.75** | $75\%$ | Three quarters |
| $\frac{1}{5}$ | **0.20** | $20\%$ | Fifth |
| $\frac{2}{5}, \frac{3}{5}, \frac{4}{5}$ | **0.40, 0.60, 0.80** | $40\%, 60\%, 80\%$ | Multiples of 0.2 |
| $\frac{1}{6}$ | **0.167** | $16.67\%$ | $\approx 0.17$ |
| $\frac{5}{6}$ | **0.833** | $83.33\%$ | $\approx 0.83$ (Bohot close to 1) |
| $\frac{1}{7}$ | **0.143** | $14.28\%$ | $\approx 0.14$ |
| $\frac{6}{7}$ | **0.857** | $85.71\%$ | $\approx 0.86$ ($\frac{5}{6}$ se bhi bada) |
| $\frac{1}{8}$ | **0.125** | $12.5\%$ | $\frac{1}{4}$ ka aadha |
| $\frac{3}{8}$ | **0.375** | $37.5\%$ | $0.25 + 0.125$ |

> **Same Gap Fraction Rule**: Agar do fractions me Numerator aur Denominator ka difference same ho (jaise $\frac{1}{2}$ aur $\frac{6}{7}$ me dono me gap $1$ hai), to **bade numbers wala fraction hamesha bada hota hai**:
> $$\frac{6}{7} (0.86) > \frac{5}{6} (0.83) > \frac{3}{4} (0.75) > \frac{1}{2} (0.50)$$

---

## 3. Worked Scenarios & Tactical Walkthroughs

### Scenario 1: Basic 3-Bubble Ascending Order
- **Bubbles**: $A = 12 \times 4$, $B = 75 / 5$, $C = 19 + 24$
- **Quick Evaluation**:
  - $A = 12 \times 4 = 48$
  - $B = 75 / 5 = 15$
  - $C = 19 + 24 = 43$
- **Ascending Selection**: $B (15) \longrightarrow C (43) \longrightarrow A (48)$
- **Solving Time**: $\approx 2.5 \text{ seconds}$.

---

### Scenario 2: 4-Bubble Descending Order with Percentages
- **Bubbles**: $A = 25\% \text{ of } 160$, $B = 6^2$, $C = 11 \times 3$, $D = 100 - 62$
- **Evaluation**:
  - $A = 25\% \times 160 = \frac{160}{4} = 40$
  - $B = 6^2 = 36$
  - $C = 11 \times 3 = 33$
  - $D = 100 - 62 = 38$
- **Descending Selection (Highest to Lowest)**: $A (40) \longrightarrow D (38) \longrightarrow B (36) \longrightarrow C (33)$.

---

### Scenario 3: Mixed Fraction & Decimal Comparison (Actual Accenture PYQ)
- **Bubbles**: $A = \frac{3}{4} - \frac{1}{2}$, $B = \frac{6}{7}$, $C = 0.5$
- **Solving Steps via Decimal Memory**:
  - Bubble $A$: $\frac{3}{4} = 0.75$ aur $\frac{1}{2} = 0.50 \implies 0.75 - 0.50 = 0.25$
  - Bubble $B$: $\frac{6}{7}$ (Gap is 1, numbers are large) $\approx 0.86$
  - Bubble $C$: Given directly as $0.50$
- **Comparison**: $0.25 < 0.50 < 0.86$
- **Ascending Selection**: $A (0.25) \longrightarrow C (0.50) \longrightarrow B (0.86)$. Zero scratchpad used!

---

### Scenario 4: Complex Operators Under High Time Pressure
- **Bubbles**: $A = 14 \times 3 - 5$, $B = 88 / 2$, $C = 15 + 17 + 13$, $D = 5^2 + 18$
- **Quick Evaluation**:
  - $A = 42 - 5 = 37$
  - $B = 44$
  - $C = (15 + 17 + 13) = 15 + 30 = 45$
  - $D = 25 + 18 = 43$
- **Ascending Order**: $A (37) \longrightarrow D (43) \longrightarrow B (44) \longrightarrow C (45)$.

---

## 4. Comprehensive Practice Question Bank (PYQs)

### Question 1
In me se sabse SMALLEST bubble kaunsa hai?  
$A = 16 \times 4$, $B = 120 / 3$, $C = 15 + 27$, $D = 50$  
- a) A (64)  
- b) B (40)  
- c) C (42)  
- d) D (50)  

---

### Question 2
Bubble expression $X = 35\% \text{ of } 200$ ki exact numerical value kya hai?  
- a) 60  
- b) 70  
- c) 75  
- d) 80  

---

### Question 3
Following bubbles ko ASCENDING (chote se bada) order me rank karo:  
$A = 8 \times 7$, $B = 90 / 2$, $C = 14 + 38$, $D = 64$  
- a) B, C, A, D  
- b) C, B, A, D  
- c) B, A, C, D  
- d) D, A, C, B  

---

### Question 4
In me se kaunse bubble ki value LARGEST hai?  
- a) $15 \times 6$  
- b) $12^2 - 50$  
- c) $300 / 3$  
- d) $40\% \text{ of } 220$  

---

### Question 5
Bubble expression $P = 18 + 27 + 35$ ko solve karne par kya value aayegi?  
- a) 70  
- b) 80  
- c) 85  
- d) 75  

---

### Question 6
Identify karo kaunsa bubble exactly 48 ke barabar hai:  
- a) $14 \times 3 + 4$  
- b) $144 / 3$  
- c) $25\% \text{ of } 180$  
- d) Both a and b  

---

### Question 7
Quick-Fire Math me Nearest-10 rounding aur benchmark estimation kyu sabse effective strategy maani jaati hai?  
- a) Ye detailed calculation kiye bina obvious non-candidates ko instantly eliminate kar deta hai  
- b) Is se question automatically change ho jata hai  
- c) Ye countdown timer ko rok deta hai  
- d) Ye fractions ko khud ba khud add kar deta hai  

---

### Question 8
In me se LARGEST bubble select karo:  
$A = 9 \times 9$, $B = 160 / 2$, $C = 33 + 49$, $D = 15\% \text{ of } 500$  
- a) A (81)  
- b) B (80)  
- c) C (82)  
- d) D (75)  

---

### Question 9
Expression $18 \times 5 - 15$ ki numerical value kya hogi?  
- a) 75  
- b) 85  
- c) 90  
- d) 65  

---

### Question 10
DESCENDING order (bade se chota) me arrange karo:  
$A = 45 / 3$, $B = 4^2$, $C = 10\% \text{ of } 130$  
- a) B, A, C  
- b) A, B, C  
- c) C, B, A  
- d) B, C, A  

---

### Question 11
Kaunsi mathematical expression exactly 36 ke barabar hai?  
- a) $6 \times 6$  
- b) $72 / 2$  
- c) $120\% \text{ of } 30$  
- d) All of the above  

---

### Question 12
In expressions me se SMALLEST value identify karo:  
$A = 7 \times 8$, $B = 110 - 55$, $C = 200 / 4$, $D = 60\% \text{ of } 95$  
- a) A (56)  
- b) B (55)  
- c) C (50)  
- d) D (57)  

---

### Question 13
Expression $125 / 5 + 17$ ki value kya hogi?  
- a) 42  
- b) 37  
- c) 45  
- d) 40  

---

### Question 14
Agar Bubble 1 = 45, Bubble 2 = 42, aur Bubble 3 = 49 hai, to correct ASCENDING order sequence kya hoga?  
- a) $2 \longrightarrow 1 \longrightarrow 3$  
- b) $1 \longrightarrow 2 \longrightarrow 3$  
- c) $3 \longrightarrow 2 \longrightarrow 1$  
- d) $2 \longrightarrow 3 \longrightarrow 1$  

---

### Question 15
Accenture ka Quick-Fire Math mini-game candidate ki kaunsi primary competency evaluate karta hai?  
- a) Spatial working memory  
- b) Rapid numerical agility, mental math speed, and executive decision-making  
- c) English grammar & reading speed  
- d) Programming data structures  

---

## 5. Complete Answer Key & Step-by-Step Explanations

| Q.No | Correct Ans | Step-by-Step Detailed Logic (Hinglish) |
| :---: | :---: | :--- |
| **Q1** | **b** | $A = 16 \times 4 = 64$, $B = 120 / 3 = 40$, $C = 15 + 27 = 42$, $D = 50$. Sabse chhota 40 (B) hai. |
| **Q2** | **b** | $35\% \text{ of } 200 = \frac{35}{100} \times 200 = 35 \times 2 = 70$. |
| **Q3** | **a** | $A = 56$, $B = 45$, $C = 52$, $D = 64$. Ascending order: $45 (B) < 52 (C) < 56 (A) < 64 (D) \implies B, C, A, D$. |
| **Q4** | **c** | $A = 90$, $B = 144 - 50 = 94$, $C = 300 / 3 = 100$, $D = 0.4 \times 220 = 88$. Sabse bada 100 (C) hai. |
| **Q5** | **b** | $18 + 27 + 35 = (18 + 27) + 35 = 45 + 35 = 80$. |
| **Q6** | **b** | Verification: $14 \times 3 + 4 = 42 + 4 = 46$ (Not 48). Par $144 / 3 = 48$. Isliye answer sirf b hai. |
| **Q7** | **a** | Rough benchmarking se 1-2 obvious non-candidates bina calculation ke bahar ho jate hain, jisse time bachta hai. |
| **Q8** | **c** | $A = 81$, $B = 80$, $C = 33 + 49 = 82$, $D = 0.15 \times 500 = 75$. Sabse largest $C (82)$ hai. |
| **Q9** | **a** | $18 \times 5 = 90$, aur $90 - 15 = 75$. |
| **Q10** | **a** | $A = 15$, $B = 16$, $C = 13$. Descending (Bade se Chota): $16 (B) > 15 (A) > 13 (C) \implies B, A, C$. |
| **Q11** | **d** | $6 \times 6 = 36$; $72 / 2 = 36$; $120\% \text{ of } 30 = 1.2 \times 30 = 36$. Teeno expressions 36 ke barabar hain. |
| **Q12** | **c** | $A = 56$, $B = 55$, $C = 50$, $D = 0.6 \times 95 = 57$. Sabse smallest $C = 50$ hai. |
| **Q13** | **a** | $125 / 5 = 25$, aur $25 + 17 = 42$. |
| **Q14** | **a** | Chote se bada sequence: $42 (\text{Bubble 2}) < 45 (\text{Bubble 1}) < 49 (\text{Bubble 3}) \implies 2 \to 1 \to 3$. |
| **Q15** | **b** | Ye mini-game candidate ki mental calculation speed, presence of mind aur numerical ranking accuracy test karta hai. |

---

## 6. Verified Practice Simulator & Video Walkthrough Links

In verified links se practice karke actual exam timer pressure ko simulate karein:

### Live Practice Platforms
- **[BuildUForward Accenture Gamified Assessment Practice Hub](https://www.builduforward.com/accenture-gamified-assessment)**  
  *Free interactive gamified assessment practice tool jisme actual Accenture pattern ke bubble games, live countdown timers aur scoring modules available hain bina login ke.*
- **[JustNK Accenture Gaming Round Complete Preparation Notes](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html)**  
  *Detailed guide covering cutoffs, game sequence, scoring weights, and sample questions.*

### Video Walkthroughs
- **[KN Academy: Accenture Bubble Maths Game Solution & Actual PYQs](https://www.youtube.com/watch?v=ZJf6dzqK5VI)**  
  *KN Academy ka authentic 14-minute breakdown jisme 24-question structure, 14-second per-question timer, fraction shortcuts aur live mental solving tricks sikhaye gaye hain.*
- **[OnlineStudy4u Accenture Cognitive Assessment All Games Video](https://www.youtube.com/watch?v=ll1srQueVrQ)**  
  *Accenture Stage 1 mini-games ke rules aur strategy walkthroughs.*

---

## 7. Test-Day Golden Checklist for Quick-Fire Math

```
[ ] Rule 1: Timer par nazar rakho—har question ke liye strictly 14 seconds milte hain.
[ ] Rule 2: Screen aate hi pehle Lowest aur Highest bubble predict karo (Sign / Range check).
[ ] Rule 3: Fraction aate hi decimal table yaad karo: 3/4 = 0.75, 1/2 = 0.50, 1/3 = 0.33.
[ ] Rule 4: Question skip mat hone do; 24 me se target banao ki 18–20 questions 100% correct hon.
[ ] Rule 5: Ascending vs Descending instruction dhyan se padho—jaldbazi me reverse click mat karna!
```
