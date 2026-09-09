# Quantitative Aptitude: Ratios, Proportions & Averages

## What this is
Ratios compare relative magnitudes between two or more quantities of the same units, while averages compute the single central representative value of a numerical distribution. In Accenture assessments, ratios and weighted averages appear frequently in mixture problems, age comparisons, and company performance statistics.

---

## Formula / Rule / Pattern

| Concept | Mathematical Formula | Usage Context |
| :--- | :--- | :--- |
| **Ratio Division** | Share of $A = \left(\frac{a}{a+b}\right) \times \text{Total}$ | Dividing total quantity in ratio $a:b$ |
| **Simple Average** | $\text{Average} = \frac{\sum x}{N}$ | Sum of items divided by count |
| **Weighted Average** | $\text{Weighted Avg} = \frac{n_1 A_1 + n_2 A_2}{n_1 + n_2}$ | Combining groups of different sizes |
| **Mixture Rule (Alligation)** | $\frac{\text{Cheaper Quantity}}{\text{Dearer Quantity}} = \frac{d - m}{m - c}$ | Finding mixing ratio of two prices |

---

## Shortcuts & Tricks

### Shortcut 1: The Weighted Average Shift Trick
> [!TIP]
> When adding a new item $X$ to a group of size $N$ with existing average $A$:
> 
> $$\text{New Average} = A + \frac{X - A}{N + 1}$$
> 
> *Why it works*: Evaluates only the deviation of the incoming value $(X - A)$ distributed across the updated total count $(N + 1)$, eliminating the need to re-multiply large sums.

### Shortcut 2: Ratio Equalization Matrix
> [!TIP]
> If $A:B = a:b$ and $B:C = c:d$, combine into $A:B:C$ by multiplying the first ratio by $c$ and the second by $b$:
> 
> $$A:B:C = (a \times c) : (b \times c) : (b \times d)$$
> 
> *Why it works*: Equalizes the common term $B$ to a single common denominator value $(b \times c)$.

---

## Worked Examples

### Example 1: Combining Ratios (Easy)
- **Question**: Given $A:B = 2:3$ and $B:C = 4:5$. Find $A:B:C$.
- **Step-by-step Solution**:
  1. Equalize $B$: Common multiple of 3 and 4 is 12.
  2. Multiply $A:B$ by 4 $\implies 8:12$.
  3. Multiply $B:C$ by 3 $\implies 12:15$.
  4. **Combine**: $A:B:C = 8:12:15$.

### Example 2: Excluded Average Deviation (Medium)
- **Question**: The average age of 24 students and 1 teacher is 15 years. If the teacher's age is excluded, the average decreases by 1 year. Find the teacher's age.
- **Step-by-step Solution**:
  1. Total group count $= 25$. Original Average $= 15$.
  2. Excluded average for 24 students $= 14$.
  3. Teacher's age $= \text{Original Sum} - \text{Students Sum} = (25 \times 15) - (24 \times 14) = 375 - 336 = 39 \text{ years}$.
  4. *Shortcut*: Teacher $= 15 + (24 \times 1) = 39$ years.

### Example 3: Alligation Mixture Ratio (Hard)
- **Question**: In what ratio must rice at ₹40/kg be mixed with rice at ₹60/kg so that the mixture is worth ₹52/kg?
- **Step-by-step Solution**:
  1. Cheaper price ($c$) $= 40$, Dearer price ($d$) $= 60$, Mean price ($m$) $= 52$.
  2. $d - m = 60 - 52 = 8$.
  3. $m - c = 52 - 40 = 12$.
  4. Ratio of Cheaper : Dearer $= 8:12 = 2:3$.

---

## Practice Questions (PYQ Bank)

Q1. Divide ₹700 among A, B, and C in the ratio 2:3:5. What is C's share?  
a) ₹140  
b) ₹210  
c) ₹350  
d) ₹400  

Q2. Average of 10 numbers is 15. If each number is multiplied by 3, what is the new average?  
a) 15  
b) 30  
c) 45  
d) 50  

Q3. Ratio of ages of A and B is 4:5. After 5 years, the ratio becomes 5:6. Find A's present age.  
a) 20 years  
b) 25 years  
c) 15 years  
d) 30 years  

Q4. Average mark of 40 students is 68. Later it was found that a score of 45 was misread as 85. What is the correct average?  
a) 67  
b) 69  
c) 66.5  
d) 67.5  

Q5. A mixture of 60 liters contains milk and water in the ratio 2:1. How much water must be added to make ratio 1:2?  
a) 40 liters  
b) 60 liters  
c) 20 liters  
d) 30 liters  

Q6. If $A:B = 3:5$ and $B:C = 6:7$, what is $A:C$?  
a) 18:35  
b) 9:14  
c) 3:7  
d) 12:35  

Q7. The mean of 5 numbers is 20. If a number 40 is added, what is the new mean?  
a) 22  
b) 23.33  
c) 25  
d) 24  

Q8. A batsman scores 80 runs in his 17th inning, increasing his average by 3 runs. Find his average after 17th inning.  
a) 29  
b) 32  
c) 35  
d) 26  

Q9. In a class of 50 students, 30 are boys with average weight 60 kg, and 20 are girls with average weight 50 kg. Find class average weight.  
a) 54 kg  
b) 55 kg  
c) 56 kg  
d) 57 kg  

Q10. Two numbers are in the ratio 3:4. If their LCM is 180, find the smaller number.  
a) 45  
b) 60  
c) 30  
d) 15  

Q11. Average temperature for Mon, Tue, Wed is 37°C. For Tue, Wed, Thu is 34°C. If Thursday's temp is 4/5 of Monday's, find Thursday's temp.  
a) 36°C  
b) 38°C  
c) 40°C  
d) 34°C  

Q12. What is the fourth proportional to 4, 9, 12?  
a) 27  
b) 36  
c) 18  
d) 24  

Q13. In a bag, coins of 50p, 25p, and 10p are in the ratio 5:9:4 amounting to ₹206. Find total number of coins.  
a) 360  
b) 720  
c) 540  
d) 800  

Q14. Average age of a family of 5 members is 24 years. If age of youngest member is 8 years, find average age of family at birth of youngest member.  
a) 16 years  
b) 20 years  
c) 18 years  
d) 22 years  

Q15. Why does multiplying every element in a dataset by constant $k$ multiply the mean by $k$?  
a) Mean is a linear operator: $\frac{\sum k x_i}{N} = k \left(\frac{\sum x_i}{N}\right)$  
b) It only works for even numbers  
c) Ratio scales double  
d) It changes count $N$  

---

## Answers

1. **c) ₹350** — $C$'s share $= 5/10 \times 700 = ₹350$.
2. **c) 45** — Multiplying all values by 3 multiplies average by 3 ($15 \times 3 = 45$).
3. **a) 20 years** — Let ages be $4x, 5x$. $(4x+5)/(5x+5) = 5/6 \implies 24x+30 = 25x+25 \implies x=5$. A's age $= 4(5) = 20$.
4. **a) 67** — Error $= 85 - 45 = +40$. Correct sum $= \text{Old Sum} - 40$. Correct average $= 68 - 40/40 = 68 - 1 = 67$.
5. **b) 60 liters** — Initial: Milk $= 40$, Water $= 20$. Desired ratio $40/(20+W) = 1/2 \implies 80 = 20 + W \implies W = 60$.
6. **a) 18:35** — $A/C = (3/5) \times (6/7) = 18/35$.
7. **c) 23.33** — New mean $= 20 + (40 - 20)/6 = 20 + 20/6 = 23.33$.
8. **b) 32** — Let old avg $= A$. $16A + 80 = 17(A+3) \implies 16A + 80 = 17A + 51 \implies A = 29$. New avg $= 29 + 3 = 32$.
9. **c) 56 kg** — $\frac{30(60) + 20(50)}{50} = \frac{1800 + 1000}{50} = \frac{2800}{50} = 56$ kg.
10. **a) 45** — Let numbers be $3x, 4x$. $\text{LCM} = 12x = 180 \implies x = 15$. Smaller number $= 3(15) = 45$.
11. **a) 36°C** — Mon - Thu $= 3 \times (37 - 34) = 9^\circ$. Mon - $(4/5)\text{Mon} = 9 \implies \text{Mon}/5 = 9 \implies \text{Mon} = 45^\circ$. Thu $= 45 - 9 = 36^\circ$.
12. **a) 27** — $4/9 = 12/x \implies 4x = 108 \implies x = 27$.
13. **b) 720** — Total value $= 5x(0.50) + 9x(0.25) + 4x(0.10) = 2.5x + 2.25x + 0.4x = 5.15x = 206 \implies x = 40$. Total coins $= 18x = 18 \times 40 = 720$.
14. **b) 20 years** — Total age now $= 5 \times 24 = 120$. 8 years ago, sum $= 120 - (5 \times 8) = 80$. Remaining members $= 4$. Avg at birth $= 80/4 = 20$ years.
15. **a) Mean is a linear operator...** — Distributive property of summation over constant scalar multiplication.

---

## Where this appears in the real Accenture test
Appears in Stage 1 & Stage 2: Quantitative Aptitude MCQ section.

---

## Recommended videos
- [PrepInsta Quantitative Syllabus Hub](https://prepinsta.com/accenture/cognitive/) — Ratios and Averages question bank.
