# Time, Speed & Distance — Complete Study Guide

## 1. Definition
**Speed** measures how fast an object moves, representing the distance covered per unit of time. 
- **Distance ($D$)**: Total spatial length traveled.
- **Speed ($S$)**: Rate of distance covered ($D / T$).
- **Time ($T$)**: Duration spent moving ($D / S$).
- **Relative Speed**: The effective speed of one moving body relative to another moving body.
- **Average Speed**: Total distance traveled divided by the total time taken across all segments.

---

## 2. Core Formula(s) / Rules

1. **Fundamental TSD Relation**: $D = S \times T$
   - *Why it works*: Distance is the accumulated product of rate of travel multiplied by duration.
2. **Unit Conversion Factor (km/h to m/s)**: $1 \text{ km/h} = \frac{5}{18} \text{ m/s}$ (and $1 \text{ m/s} = \frac{18}{5} \text{ km/h}$)
   - *Why it works*: $1 \text{ km} = 1000 \text{ m}$ and $1 \text{ hour} = 3600 \text{ s}$. Thus $\frac{1000}{3600} = \frac{5}{18}$.
3. **Relative Speed (Opposite Direction)**: $S_{\text{rel}} = S_1 + S_2$
   - *Why it works*: Objects moving toward each other close the distance between them at the combined rate of both speeds.
4. **Relative Speed (Same Direction)**: $S_{\text{rel}} = |S_1 - S_2|$
   - *Why it works*: The faster object pulls away or gains ground at the speed difference.
5. **Average Speed (Equal Distances)**: $S_{\text{avg}} = \frac{2 x y}{x + y}$
   - *Why it works*: Harmonic mean of two speeds $x$ and $y$ covering equal distances $D$, derived from $\text{Total Distance} (2D) / \text{Total Time} (D/x + D/y)$.
6. **Boats and Streams**:
   - Downstream Speed ($D_s$) = $u + v$ (Boat speed in still water $u$ + River current speed $v$).
   - Upstream Speed ($U_s$) = $u - v$.
   - *Why it works*: Water current assists motion downstream and opposes motion upstream.

---

## 3. Tricks & Shortcuts

### Shortcut 1: Speed-Time Inversion Trick (Fixed Distance)
- **Concept**: When distance is constant, Speed and Time are inversely proportional ($S_1 / S_2 = T_2 / T_1$).
- **Long Method**:
  - Distance $D = 60$ km. Speed 1 = 20 km/h $\implies T_1 = 60 / 20 = 3$ hours.
  - Speed 2 = 30 km/h $\implies T_2 = 60 / 30 = 2$ hours. Ratio $T_1 : T_2 = 3 : 2$. (Calculates $D$ first)
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
  $$D = \frac{S_1 \times S_2}{|S_1 - S_2|} \times \left(\frac{t_1 + t_2}{60}\right)$$
- **Long Method**:
  - Let distance be $D$. $\frac{D}{S_1} - \frac{t_1}{60} = \frac{D}{S_2} + \frac{t_2}{60}$. Solve for $D$. (Takes 60 seconds)
- **Shortcut Method**: Plug speeds and time difference straight into product-over-difference formula. (Takes 10 seconds)

---

## 4. Worked Examples

### Example 1 (Easy): Unit Conversion & Train Length
**Question**: A train 180 meters long is traveling at a constant speed of 72 km/h. How many seconds will it take to pass a telegraph pole standing beside the track?
- **Step 1**: Convert train speed from km/h to m/s: $72 \times \frac{5}{18} = 4 \times 5 = 20 \text{ m/s}$.
- **Step 2**: Identify total distance to cross telegraph pole = Length of train = $180 \text{ m}$.
- **Step 3**: Calculate time: $T = \frac{D}{S} = \frac{180}{20} = 9 \text{ seconds}$.

### Example 2 (Medium): Relative Speed & Train Crossing Platform
**Question**: A train 200 m long traveling at 54 km/h meets a second train 160 m long coming from the opposite direction at 36 km/h. How long will it take for the two trains to completely pass each other?
- **Step 1**: Total distance to be covered = $L_1 + L_2 = 200 + 160 = 360 \text{ m}$.
- **Step 2**: Calculate relative speed (opposite directions $\implies$ sum speeds):
  - $S_{\text{rel}} = 54 + 36 = 90 \text{ km/h}$.
- **Step 3**: Convert relative speed to m/s: $90 \times \frac{5}{18} = 25 \text{ m/s}$.
- **Step 4**: Calculate passing time: $T = \frac{360}{25} = 14.4 \text{ seconds}$.

### Example 3 (Hard): Boats & Streams with Round Trip Time
**Question**: A motorboat can travel at 15 km/h in still water. It goes 30 km downstream and returns to the starting point in a total time of 4 hours 30 minutes. Find the speed of the river current.
- **Step 1**: Let speed of current be $v$ km/h.
  - Downstream speed $D_s = 15 + v$.
  - Upstream speed $U_s = 15 - v$.
- **Step 2**: Total time $= T_{\text{down}} + T_{\text{up}} = \frac{30}{15 + v} + \frac{30}{15 - v} = 4.5 = \frac{9}{2}$ hours.
- **Step 3**: Combine terms: $30 \left(\frac{15 - v + 15 + v}{225 - v^2}\right) = \frac{9}{2} \implies 30 \left(\frac{30}{225 - v^2}\right) = \frac{9}{2}$.
- **Step 4**: Simplify: $\frac{900}{225 - v^2} = \frac{9}{2} \implies 225 - v^2 = 200 \implies v^2 = 25 \implies v = 5 \text{ km/h}$.

---

## 5. Common Mistakes

1. **Forgetting Unit Conversions**:
   - *Why it happens*: Mixing speeds in km/h with distance in meters or time in seconds. Always convert speeds to m/s when distances are given in meters.
2. **Simple Average of Speeds**:
   - *Why it happens*: Calculating average speed as $\frac{x + y}{2}$ instead of $\frac{2xy}{x + y}$. Arithmetic mean is ONLY valid if travel time intervals are identical, NOT distances.
3. **Incorrect Relative Speed Direction**:
   - *Why it happens*: Subtracting speeds when objects move towards each other. Remember: Opposite directions = ADD speeds; Same direction = SUBTRACT speeds.

---

## 6. Practice Questions

1. **(Easy)** A car covers 240 km in 4 hours. How much time will it take to cover the same distance at a speed of 40 km/h?
2. **(Easy)** Convert a speed of 25 m/s into km/h.
3. **(Easy)** A cyclist travels at 12 km/h for 2 hours and then at 18 km/h for 3 hours. What is his average speed for the whole journey?
4. **(Medium)** Walking at $\frac{3}{4}$ of his usual speed, a man reaches his office 20 minutes late. What is his usual time to reach the office?
5. **(Medium)** Two cities A and B are 300 km apart. Train 1 starts from A towards B at 60 km/h at 8:00 AM. Train 2 starts from B towards A at 90 km/h at 9:00 AM. At what time will they meet?
6. **(Medium)** A train 150 meters long passes a platform 250 meters long in 20 seconds. What is the speed of the train in km/h?
7. **(Hard)** A man can row 6 km/h in still water. If the river flows at 2 km/h, it takes him 3 hours more to row upstream than downstream for the same distance. Find the distance.
8. **(Hard)** A thief steals a car at 1:30 PM and drives it at 40 km/h. The theft is discovered at 2:00 PM and the owner sets off in another car at 50 km/h. At what time will the owner catch the thief?

---

## 7. Answer Key with Explanations

1. **Answer: 6 hours**
   - *Explanation*: Original speed $= 240 / 4 = 60$ km/h.
   - New speed $= 40$ km/h.
   - Time required $= \frac{240}{40} = 6$ hours.

2. **Answer: 90 km/h**
   - *Explanation*: $25 \times \frac{18}{5} = 5 \times 18 = 90$ km/h.

3. **Answer: 15.6 km/h**
   - *Explanation*: Total distance $= (12 \times 2) + (18 \times 3) = 24 + 54 = 78$ km.
   - Total time $= 2 + 3 = 5$ hours.
   - Average speed $= \frac{78}{5} = 15.6$ km/h.

4. **Answer: 60 minutes (1 hour)**
   - *Explanation*: Speed ratio (new : usual) $= 3 : 4$.
   - Time ratio (new : usual) $= 4 : 3$.
   - Let usual time $= 3x$, new time $= 4x$. Difference $= 4x - 3x = x = 20$ minutes.
   - Usual time $= 3x = 3 \times 20 = 60$ minutes.

5. **Answer: 10:36 AM**
   - *Explanation*: By 9:00 AM (1 hour), Train 1 covers $60 \times 1 = 60$ km.
   - Remaining distance between trains at 9:00 AM $= 300 - 60 = 240$ km.
   - Relative speed $= 60 + 90 = 150$ km/h.
   - Time taken to meet after 9:00 AM $= \frac{240}{150} = 1.6$ hours $= 1 \text{ hour } 36 \text{ mins}$.
   - Meeting time $= 9:00 \text{ AM} + 1 \text{h } 36 \text{m} = 10:36 \text{ AM}$.

6. **Answer: 72 km/h**
   - *Explanation*: Total distance $= 150 + 250 = 400$ m.
   - Time $= 20$ seconds.
   - Speed in m/s $= \frac{400}{20} = 20$ m/s.
   - Convert to km/h $= 20 \times \frac{18}{5} = 72$ km/h.

7. **Answer: 24 km**
   - *Explanation*: Downstream speed $D_s = 6 + 2 = 8$ km/h.
   - Upstream speed $U_s = 6 - 2 = 4$ km/h.
   - Let distance be $D$. $\frac{D}{4} - \frac{D}{8} = 3 \implies \frac{D}{8} = 3 \implies D = 24$ km.

8. **Answer: 4:00 PM**
   - *Explanation*: Head start time for thief $= 30$ minutes ($0.5$ hours).
   - Distance covered by thief before pursuit $= 40 \times 0.5 = 20$ km.
   - Relative speed $= 50 - 40 = 10$ km/h.
   - Time to overtake $= \frac{20}{10} = 2$ hours.
   - Pursuit starts at 2:00 PM $\implies$ Thief caught at $2:00 \text{ PM} + 2 \text{ hours} = 4:00 \text{ PM}$.
