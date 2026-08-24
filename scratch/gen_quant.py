import os

# 1. Percentages, Profit & Loss
percentages_content = """# Percentages, Profit & Loss — Complete Study Guide

## 1. Definition
**Percentage** means 'per hundred'—it is simply a ratio expressed as a fraction of 100. It allows us to compare proportions across different totals.
- **Cost Price (CP)**: The actual amount spent to purchase or manufacture an item.
- **Selling Price (SP)**: The price at which the item is sold to a customer.
- **Marked Price (MP)**: The list price printed on the label before any discount.
- **Profit**: Occurs when SP > CP.
- **Loss**: Occurs when CP > SP.
- **Discount**: A reduction offered on the Marked Price (MP - SP).

---

## 2. Core Formula(s) / Rules

1. **Percentage Value**: $\\text{Percentage} = \\left(\\frac{\\text{Part}}{\\text{Whole}}\\right) \\times 100$
   - *Why it works*: Normalizes any ratio onto a standardized scale of 100 for direct comparison.
2. **Percentage Increase / Decrease**: $\\text{\\% Change} = \\left(\\frac{\\text{New Value} - \\text{Base Value}}{\\text{Base Value}}\\right) \\times 100$
   - *Why it works*: Measures change relative strictly to the starting (original) baseline.
3. **Profit \\%**: $\\text{Profit \\%} = \\left(\\frac{\\text{SP} - \\text{CP}}{\\text{CP}}\\right) \\times 100$
   - *Why it works*: Profit is financial gain calculated on the capital invested (CP).
4. **Loss \\%**: $\\text{Loss \\%} = \\left(\\frac{\\text{CP} - \\text{SP}}{\\text{CP}}\\right) \\times 100$
   - *Why it works*: Loss is financial loss calculated on the capital invested (CP).
5. **Discount \\%**: $\\text{Discount \\%} = \\left(\\frac{\\text{MP} - \\text{SP}}{\\text{MP}}\\right) \\times 100$
   - *Why it works*: Discounts are always offered on the marked/list price, not the cost price.
6. **Net Percentage Change (Successive)**: $\\text{Net \\%} = a + b + \\frac{ab}{100}$
   - *Why it works*: Accounts for compounding where the second percentage change $b$ applies to the result of the first percentage change $a$.

---

## 3. Tricks & Shortcuts

### Shortcut 1: Decimal Multipliers for Fast Calculations
- **Concept**: Instead of calculating percentage separately and adding, multiply CP directly by $(1 + \\text{profit rate})$. For a 20% profit, multiply by 1.20; for a 15% loss, multiply by 0.85.
- **Long Method**: 
  - Find 20% of 450: $\\frac{20}{100} \\times 450 = 90$.
  - Add to original: $450 + 90 = 540$. (Takes 2 steps & 25 seconds)
- **Shortcut Method**: 
  - $450 \\times 1.2 = 540$. (Takes 1 step & 3 seconds)

### Shortcut 2: Net Effect of Two Successive Percentage Changes ($a\\%$ and $b\\%$)
- **Formula**: $\\text{Net \\%} = a + b + \\frac{ab}{100}$ (Use positive for increase, negative for decrease).
- **Long Method**: 
  - Price of ₹100 increased by 20% = ₹120.
  - Then decreased by 10% = $120 - 12 = ₹108$.
  - Change = $108 - 100 = +8\\%$. (3 calculation steps)
- **Shortcut Method**: 
  - $\\text{Net} = 20 + (-10) + \\frac{20 \\times (-10)}{100} = 10 - 2 = 8\\%$. (Mental math in 4 seconds)

### Shortcut 3: Same Profit \\% and Loss \\% on Two Items Sold at Same SP
- **Rule**: If two items are sold at the same Selling Price, one at $x\\%$ profit and the other at $x\\%$ loss, there is **ALWAYS an overall net loss** of $\\frac{x^2}{100}\\%$.
- **Long Method**:
  - Item 1: $SP = 1200$, Profit $20\\% \\implies CP_1 = 1200 / 1.2 = 1000$.
  - Item 2: $SP = 1200$, Loss $20\\% \\implies CP_2 = 1200 / 0.8 = 1500$.
  - Total $CP = 2500$, Total $SP = 2400$. Loss = 100. Loss $\% = (100 / 2500) \\times 100 = 4\\%$. (45 seconds)
- **Shortcut Method**:
  - Net Loss $\% = \\frac{20^2}{100} = \\frac{400}{100} = 4\\%$. (2 seconds)

---

## 4. Worked Examples

### Example 1 (Easy): Basic Percentage Increase
**Question**: A candidate scores 420 marks out of 600 in an exam. What is their percentage score? If the passing requirement is 75%, by how many marks did the candidate pass or fail?
- **Step 1**: Calculate percentage score = $\\left(\\frac{420}{600}\\right) \\times 100 = 0.70 \\times 100 = 70\\%$.
- **Step 2**: Calculate passing marks required = $75\\%$ of $600 = 0.75 \\times 600 = 450$ marks.
- **Step 3**: Compare marks: $450 - 420 = 30$ marks.
- **Conclusion**: The candidate scored 70% and failed by 30 marks.

### Example 2 (Medium): Profit and Discount Combination
**Question**: A retailer marks up an item by 40% above its Cost Price (₹800) and then offers a discount of 15% on the Marked Price. Calculate the Marked Price, Selling Price, and Net Profit Percentage.
- **Step 1**: Calculate Marked Price (MP): $MP = 800 \\times 1.40 = ₹1120$.
- **Step 2**: Calculate Selling Price (SP): $SP = MP \\times (1 - 0.15) = 1120 \\times 0.85 = ₹952$.
- **Step 3**: Calculate Profit Amount: $\\text{Profit} = SP - CP = 952 - 800 = ₹152$.
- **Step 4**: Calculate Profit Percentage: $\\text{Profit \\%} = \\left(\\frac{152}{800}\\right) \\times 100 = 19\\%$.

### Example 3 (Hard): Dishonest Dealer / False Weights
**Question**: A dishonest shopkeeper claims to sell sugar at Cost Price, but uses a false weight of 900 grams instead of 1 kilogram (1000 grams). Find his actual profit percentage.
- **Step 1**: Let the Cost Price of 1 gram sugar be ₹1.
- **Step 2**: Cost Price of 1000g (claimed quantity) = ₹1000.
- **Step 3**: Actual weight delivered = 900g. Cost Price of actual sugar given ($CP$) = ₹900.
- **Step 4**: Money collected from customer ($SP$) = ₹1000 (since he claims to sell 1000g at CP).
- **Step 5**: Calculate Profit: $SP - CP = 1000 - 900 = ₹100$.
- **Step 6**: Calculate Profit Percentage: $\\text{Profit \\%} = \\left(\\frac{\\text{Error}}{\\text{True Value} - \\text{Error}}\\right) \\times 100 = \\left(\\frac{100}{900}\\right) \\times 100 = 11.11\\%$.

---

## 5. Common Mistakes

1. **Calculating Profit or Loss percentage on SP instead of CP**:
   - *Why it happens*: Students use SP in the denominator because it is given last in the question text. Always remember: Profit/Loss is based on CP unless explicitly stated otherwise.
2. **Incorrectly compounding successive discounts**:
   - *Why it happens*: Assuming two successive discounts of 20% and 10% equal a single discount of 30%. In reality, 10% applies on the reduced price (80% of original), making the net discount 28%.
3. **Confusing Percentage Change Base**:
   - *Why it happens*: If A is 25% more than B, students incorrectly assume B is 25% less than A. If A = 125 and B = 100, B is less than A by $\\frac{25}{125} \\times 100 = 20\\%$.

---

## 6. Practice Questions

1. **(Easy)** If the price of petrol increases by 25%, by what percentage must a driver reduce petrol consumption so that the overall expenditure remains unchanged?
2. **(Easy)** An article bought for ₹600 is sold for ₹750. What is the profit percentage?
3. **(Easy)** A laptop is marked at ₹45,000. If a festival discount of 12% is offered, what is the final selling price?
4. **(Medium)** A trader sells two watch models for ₹2,400 each. On the first watch, he gains 20%, and on the second, he loses 20%. What is his overall gain or loss percentage and total monetary loss?
5. **(Medium)** By selling an item for ₹1,440, a shopkeeper loses 10%. At what price must he sell it to gain 15%?
6. **(Medium)** A person spends 30% of his income on house rent, 20% of the remaining on food, and 50% of the remaining on children's education. If he saves ₹8,400 per month, what is his total monthly income?
7. **(Hard)** A manufacturer sells an article to a wholesale dealer at 10% profit. The wholesale dealer sells it to a retailer at 20% profit, and the retailer sells it to a customer for ₹3,267 at a profit of 25%. Find the cost price of the article for the manufacturer.
8. **(Hard)** A merchant buys 80 kg of rice at ₹40/kg and 120 kg of rice at ₹50/kg. He mixes them and sells 40% of the mixture at ₹55/kg. At what price per kg must he sell the remaining mixture to earn an overall profit of 25%?

---

## 7. Answer Key with Explanations

1. **Answer: 20%**
   - *Explanation*: Let original price = ₹100, consumption = 100 units. Total expenditure = ₹10,000.
   - New price = ₹125. New consumption required = $\\frac{10000}{125} = 80$ units.
   - Reduction = $100 - 80 = 20$ units $\\implies 20\\%$.
   - *Shortcut formula*: $\\left(\\frac{r}{100 + r}\\right) \\times 100 = \\left(\\frac{25}{125}\\right) \\times 100 = 20\\%$.

2. **Answer: 25%**
   - *Explanation*: $CP = 600$, $SP = 750$.
   - Profit = $750 - 600 = 150$.
   - Profit $\% = \\left(\\frac{150}{600}\\right) \\times 100 = 25\\%$.

3. **Answer: ₹39,600**
   - *Explanation*: $MP = 45000$, Discount = $12\\%$.
   - $SP = MP \\times (1 - 0.12) = 45000 \\times 0.88 = ₹39,600$.

4. **Answer: 4% overall loss; ₹200 monetary loss**
   - *Explanation*: Overall loss $\% = \\frac{20^2}{100} = 4\\%$.
   - Total $SP = 2400 + 2400 = ₹4,800$.
   - Since there is a $4\\%$ loss, Total $SP = 96\\%$ of Total $CP$.
   - Total $CP = \\frac{4800}{0.96} = ₹5,000$.
   - Total monetary loss = $5000 - 4800 = ₹200$.

5. **Answer: ₹1,840**
   - *Explanation*: $SP_1 = 1440$, Loss = $10\\% \\implies SP_1 = 90\\%$ of $CP$.
   - $CP = \\frac{1440}{0.90} = ₹1,600$.
   - Desired profit = $15\\% \\implies SP_2 = CP \\times 1.15 = 1600 \\times 1.15 = ₹1,840$.

6. **Answer: ₹30,000**
   - *Explanation*: Let income = $I$.
   - After rent ($30\\%$): remaining = $0.70I$.
   - After food ($20\\%$ of remaining): remaining = $0.70I \\times 0.80 = 0.56I$.
   - After education ($50\\%$ of remaining): remaining = $0.56I \\times 0.50 = 0.28I$.
   - Given savings $= 0.28I = 8400 \\implies I = \\frac{8400}{0.28} = ₹30,000$.

7. **Answer: ₹2,250**
   - *Explanation*: Let manufacturer CP = $X$.
   - Wholesale CP = $1.10 X$.
   - Retailer CP = $1.10 X \\times 1.20 = 1.32 X$.
   - Customer price = $1.32 X \\times 1.25 = 1.65 X$.
   - $1.65 X = 3267 \\implies X = \\frac{3267}{1.65} = ₹2,250$.

8. **Answer: ₹59.17 per kg**
   - *Explanation*: Total weight = $80 + 120 = 200$ kg.
   - Total Cost Price = $(80 \\times 40) + (120 \\times 50) = 3200 + 6000 = ₹9,200$.
   - Desired total revenue at $25\\%$ profit = $9200 \\times 1.25 = ₹11,500$.
   - $40\\%$ of mixture sold = $0.40 \\times 200 = 80$ kg at ₹55/kg $\\implies$ Revenue collected = $80 \\times 55 = ₹4,400$.
   - Remaining revenue needed = $11500 - 4400 = ₹7,100$.
   - Remaining weight = $200 - 80 = 120$ kg.
   - Required SP per kg for remaining = $\\frac{7100}{120} = ₹59.17$ per kg.
"""

# 2. Time, Speed & Distance
tsd_content = """# Time, Speed & Distance — Complete Study Guide

## 1. Definition
**Speed** measures how fast an object moves, representing the distance covered per unit of time. 
- **Distance ($D$)**: Total spatial length traveled.
- **Speed ($S$)**: Rate of distance covered ($D / T$).
- **Time ($T$)**: Duration spent moving ($D / S$).
- **Relative Speed**: The effective speed of one moving body relative to another moving body.
- **Average Speed**: Total distance traveled divided by the total time taken across all segments.

---

## 2. Core Formula(s) / Rules

1. **Fundamental TSD Relation**: $D = S \\times T$
   - *Why it works*: Distance is the accumulated product of rate of travel multiplied by duration.
2. **Unit Conversion Factor (km/h to m/s)**: $1 \\text{ km/h} = \\frac{5}{18} \\text{ m/s}$ (and $1 \\text{ m/s} = \\frac{18}{5} \\text{ km/h}$)
   - *Why it works*: $1 \\text{ km} = 1000 \\text{ m}$ and $1 \\text{ hour} = 3600 \\text{ s}$. Thus $\\frac{1000}{3600} = \\frac{5}{18}$.
3. **Relative Speed (Opposite Direction)**: $S_{\\text{rel}} = S_1 + S_2$
   - *Why it works*: Objects moving toward each other close the distance between them at the combined rate of both speeds.
4. **Relative Speed (Same Direction)**: $S_{\\text{rel}} = |S_1 - S_2|$
   - *Why it works*: The faster object pulls away or gains ground at the speed difference.
5. **Average Speed (Equal Distances)**: $S_{\\text{avg}} = \\frac{2 x y}{x + y}$
   - *Why it works*: Harmonic mean of two speeds $x$ and $y$ covering equal distances $D$, derived from $\\text{Total Distance} (2D) / \\text{Total Time} (D/x + D/y)$.
6. **Boats and Streams**:
   - Downstream Speed ($D_s$) = $u + v$ (Boat speed in still water $u$ + River current speed $v$).
   - Upstream Speed ($U_s$) = $u - v$.
   - *Why it works*: Water current assists motion downstream and opposes motion upstream.

---

## 3. Tricks & Shortcuts

### Shortcut 1: Speed-Time Inversion Trick (Fixed Distance)
- **Concept**: When distance is constant, Speed and Time are inversely proportional ($S_1 / S_2 = T_2 / T_1$).
- **Long Method**:
  - Distance $D = 60$ km. Speed 1 = 20 km/h $\\implies T_1 = 60 / 20 = 3$ hours.
  - Speed 2 = 30 km/h $\\implies T_2 = 60 / 30 = 2$ hours. Ratio $T_1 : T_2 = 3 : 2$. (Calculates $D$ first)
- **Shortcut Method**:
  - Ratio of speeds $S_1 : S_2 = 20 : 30 = 2 : 3$.
  - Invert ratio immediately for time: $T_1 : T_2 = 3 : 2$. (1 second calculation)

### Shortcut 2: Trains Crossing Objects (Platform vs Man)
- **Rule**:
  - Distance to cross a stationary point (man, pole, tree) = Length of train ($L_t$).
  - Distance to cross a platform/bridge/tunnel = Length of train ($L_t$) + Length of platform ($L_p$).
- **Long Method**: Set up custom algebraic equations for each situation.
- **Shortcut Method**: Extra distance covered when crossing platform vs man is ALWAYS equal to platform length $L_p$. Extra time taken $= L_p / S_t$.

### Shortcut 3: Early / Late Arrival Formula
- **Formula**: If traveling at speed $S_1$ makes you late by $t_1$ and speed $S_2$ makes you early by $t_2$, the distance to destination is:
  $$D = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\left(\\frac{t_1 + t_2}{60}\\right)$$
- **Long Method**:
  - Let distance be $D$. $\\frac{D}{S_1} - \\frac{t_1}{60} = \\frac{D}{S_2} + \\frac{t_2}{60}$. Solve for $D$. (Takes 60 seconds)
- **Shortcut Method**: Plug speeds and time difference straight into product-over-difference formula. (Takes 10 seconds)

---

## 4. Worked Examples

### Example 1 (Easy): Unit Conversion & Train Length
**Question**: A train 180 meters long is traveling at a constant speed of 72 km/h. How many seconds will it take to pass a telegraph pole standing beside the track?
- **Step 1**: Convert train speed from km/h to m/s: $72 \\times \\frac{5}{18} = 4 \\times 5 = 20 \\text{ m/s}$.
- **Step 2**: Identify total distance to cross telegraph pole = Length of train = $180 \\text{ m}$.
- **Step 3**: Calculate time: $T = \\frac{D}{S} = \\frac{180}{20} = 9 \\text{ seconds}$.

### Example 2 (Medium): Relative Speed & Train Crossing Platform
**Question**: A train 200 m long traveling at 54 km/h meets a second train 160 m long coming from the opposite direction at 36 km/h. How long will it take for the two trains to completely pass each other?
- **Step 1**: Total distance to be covered = $L_1 + L_2 = 200 + 160 = 360 \\text{ m}$.
- **Step 2**: Calculate relative speed (opposite directions $\\implies$ sum speeds):
  - $S_{\\text{rel}} = 54 + 36 = 90 \\text{ km/h}$.
- **Step 3**: Convert relative speed to m/s: $90 \\times \\frac{5}{18} = 25 \\text{ m/s}$.
- **Step 4**: Calculate passing time: $T = \\frac{360}{25} = 14.4 \\text{ seconds}$.

### Example 3 (Hard): Boats & Streams with Round Trip Time
**Question**: A motorboat can travel at 15 km/h in still water. It goes 30 km downstream and returns to the starting point in a total time of 4 hours 30 minutes. Find the speed of the river current.
- **Step 1**: Let speed of current be $v$ km/h.
  - Downstream speed $D_s = 15 + v$.
  - Upstream speed $U_s = 15 - v$.
- **Step 2**: Total time $= T_{\\text{down}} + T_{\\text{up}} = \\frac{30}{15 + v} + \\frac{30}{15 - v} = 4.5 = \\frac{9}{2}$ hours.
- **Step 3**: Combine terms: $30 \\left(\\frac{15 - v + 15 + v}{225 - v^2}\\right) = \\frac{9}{2} \\implies 30 \\left(\\frac{30}{225 - v^2}\\right) = \\frac{9}{2}$.
- **Step 4**: Simplify: $\\frac{900}{225 - v^2} = \\frac{9}{2} \\implies 225 - v^2 = 200 \\implies v^2 = 25 \\implies v = 5 \\text{ km/h}$.

---

## 5. Common Mistakes

1. **Forgetting Unit Conversions**:
   - *Why it happens*: Mixing speeds in km/h with distance in meters or time in seconds. Always convert speeds to m/s when distances are given in meters.
2. **Simple Average of Speeds**:
   - *Why it happens*: Calculating average speed as $\\frac{x + y}{2}$ instead of $\\frac{2xy}{x + y}$. Arithmetic mean is ONLY valid if travel time intervals are identical, NOT distances.
3. **Incorrect Relative Speed Direction**:
   - *Why it happens*: Subtracting speeds when objects move towards each other. Remember: Opposite directions = ADD speeds; Same direction = SUBTRACT speeds.

---

## 6. Practice Questions

1. **(Easy)** A car covers 240 km in 4 hours. How much time will it take to cover the same distance at a speed of 40 km/h?
2. **(Easy)** Convert a speed of 25 m/s into km/h.
3. **(Easy)** A cyclist travels at 12 km/h for 2 hours and then at 18 km/h for 3 hours. What is his average speed for the whole journey?
4. **(Medium)** Walking at $\\frac{3}{4}$ of his usual speed, a man reaches his office 20 minutes late. What is his usual time to reach the office?
5. **(Medium)** Two cities A and B are 300 km apart. Train 1 starts from A towards B at 60 km/h at 8:00 AM. Train 2 starts from B towards A at 90 km/h at 9:00 AM. At what time will they meet?
6. **(Medium)** A train 150 meters long passes a platform 250 meters long in 20 seconds. What is the speed of the train in km/h?
7. **(Hard)** A man can row 6 km/h in still water. If the river flows at 2 km/h, it takes him 3 hours more to row upstream than downstream for the same distance. Find the distance.
8. **(Hard)** A thief steals a car at 1:30 PM and drives it at 40 km/h. The theft is discovered at 2:00 PM and the owner sets off in another car at 50 km/h. At what time will the owner catch the thief?

---

## 7. Answer Key with Explanations

1. **Answer: 6 hours**
   - *Explanation*: Original speed $= 240 / 4 = 60$ km/h.
   - New speed $= 40$ km/h.
   - Time required $= \\frac{240}{40} = 6$ hours.

2. **Answer: 90 km/h**
   - *Explanation*: $25 \\times \\frac{18}{5} = 5 \\times 18 = 90$ km/h.

3. **Answer: 15.6 km/h**
   - *Explanation*: Total distance $= (12 \\times 2) + (18 \\times 3) = 24 + 54 = 78$ km.
   - Total time $= 2 + 3 = 5$ hours.
   - Average speed $= \\frac{78}{5} = 15.6$ km/h.

4. **Answer: 60 minutes (1 hour)**
   - *Explanation*: Speed ratio (new : usual) $= 3 : 4$.
   - Time ratio (new : usual) $= 4 : 3$.
   - Let usual time $= 3x$, new time $= 4x$. Difference $= 4x - 3x = x = 20$ minutes.
   - Usual time $= 3x = 3 \\times 20 = 60$ minutes.

5. **Answer: 10:36 AM**
   - *Explanation*: By 9:00 AM (1 hour), Train 1 covers $60 \\times 1 = 60$ km.
   - Remaining distance between trains at 9:00 AM $= 300 - 60 = 240$ km.
   - Relative speed $= 60 + 90 = 150$ km/h.
   - Time taken to meet after 9:00 AM $= \\frac{240}{150} = 1.6$ hours $= 1 \\text{ hour } 36 \\text{ mins}$.
   - Meeting time $= 9:00 \\text{ AM} + 1 \\text{h } 36 \\text{m} = 10:36 \\text{ AM}$.

6. **Answer: 72 km/h**
   - *Explanation*: Total distance $= 150 + 250 = 400$ m.
   - Time $= 20$ seconds.
   - Speed in m/s $= \\frac{400}{20} = 20$ m/s.
   - Convert to km/h $= 20 \\times \\frac{18}{5} = 72$ km/h.

7. **Answer: 24 km**
   - *Explanation*: Downstream speed $D_s = 6 + 2 = 8$ km/h.
   - Upstream speed $U_s = 6 - 2 = 4$ km/h.
   - Let distance be $D$. $\\frac{D}{4} - \\frac{D}{8} = 3 \\implies \\frac{D}{8} = 3 \\implies D = 24$ km.

8. **Answer: 4:00 PM**
   - *Explanation*: Head start time for thief $= 30$ minutes ($0.5$ hours).
   - Distance covered by thief before pursuit $= 40 \\times 0.5 = 20$ km.
   - Relative speed $= 50 - 40 = 10$ km/h.
   - Time to overtake $= \\frac{20}{10} = 2$ hours.
   - Pursuit starts at 2:00 PM $\\implies$ Thief caught at $2:00 \\text{ PM} + 2 \\text{ hours} = 4:00 \\text{ PM}$.
"""

with open('01-aptitude/quantitative/percentages-profit-loss.md', 'w', encoding='utf-8') as f:
    f.write(percentages_content)

with open('01-aptitude/quantitative/time-speed-distance.md', 'w', encoding='utf-8') as f:
    f.write(tsd_content)

print("Percentages and TSD files written.")
