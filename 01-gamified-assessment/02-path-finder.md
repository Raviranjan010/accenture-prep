# Accenture Cognitive Assessment: Path Finder (Tile Rotation) Master Guide

> **Target Assessment**: Accenture Recruitment — Stage 1: Gamified Cognitive Assessment (Aon / cut-e & SHL Platforms)  
> **Topic**: Spatial Rotation, Continuous Grid Pathfinding & Tile Connector Logic  
> **Repository Target**: `02-path-finder.md`  
> **Language**: Hinglish (In-Depth, Conceptual, Zero Fluff)

---

## 1. Game Overview & Assessment Mechanism

**Path Finder** (jise *Tile Rotation*, *Pipe Connector*, ya *Grid Path Game* bhi kehte hain) Accenture ke Cognitive Assessment ka ek elimination-grade mini-game hai. Screen par aapko ek $3\times3$, $4\times4$, ya $5\times5$ matrix milti hai jisme fragmented paths/pipes (straight lines, L-bends, T-junctions, cross tiles) scattered hote hain.

Aapka primary task hota hai tiles ko rotate karke **Entry (Start Node)** se **Exit (End Node)** tak ek seamless, continuous, unbroken connection banana before the countdown timer hits zero.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                 CORE GAME OBJECTIVE                                     │
│                                                                                         │
│   [ START NODE ] ───▶ [ Rotatable Tile 1 ] ───▶ [ Rotatable Tile 2 ] ───▶ [ END NODE ]   │
│   Fixed Entry          Orient Connection         Orient Connection         Fixed Exit   │
│                                                                                         │
│   Rule: Har intermediate tile ka input previous tile se aur output next tile se        │
│         perfectly aligned hona chahiye without open/leaking ends.                       │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### Cognitive Metrics Tracked by the Engine
1. **Mental Rotation Speed**: 2D shape ko dimag me $90^\circ, 180^\circ, 270^\circ$ ghumakar fit karne ki raw speed.
2. **Move Efficiency (Click Economy)**: Tile ko bina soche baar-baar 360° click spam karna score penalty deta hai. Minimum rotation clicks me path complete karna hota hai.
3. **Deductive Pruning**: Invalid branches ko explore kiye bina direct boundary constraints se eliminate karna.
4. **Time to First Move vs. Completion Time**: Start hote hi instant boundary anchors fix karna.

---

## 2. Tile Types & Mathematical Orientation Table

Har tile type ke physical rotation states aur available connections fix hote hain. Unhe samajhna clicks bachane ke liye sabse zaruri hai:

| Tile Type | Visual Symbol | Rotation Step | Unique Orientations | Clicks to Reset ($360^\circ$) | Usable Connection Paths |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Straight Line** | `│` / `─` | $90^\circ$ | **2** (Vertical, Horizontal) | 2 clicks / 4 clicks | Opposite sides connect karta hai (`N-S` ya `E-W`). |
| **Elbow Bend (L-Tile)** | `┌` `┐` `└` `┘` | $90^\circ$ | **4** (Top-Right, Right-Down, Down-Left, Left-Up) | 4 clicks | Adjacent sides ko $90^\circ$ pe turn deta hai. Corner routing ke liye mandatory. |
| **T-Junction** | `┬` `┴` `├` `┤` | $90^\circ$ | **4** (Har side 1 dead end + 3 open arms) | 4 clicks | 3 directions connect karta hai; 1 side blind wall hoti hai. |
| **Cross Tile (+)** | `┼` | $90^\circ$ | **1** (Visually symmetric) | 0 / 1 click | Chaaro taraf (`N, S, E, W`) connect karta hai. Isko rotate karne ki zarurat nahi hoti. |

---

## 3. High-Speed Shortcuts & Core Strategies

### Strategy 1: The "Backward End-Search" Technique (Pruning Shortcut)

> [!TIP]
> **Backward Search Trick:** Path ko hamesha **Exit (End Tile)** se reverse solve karna start karo, na ki Start Tile se!
>
> **Why It Works:**
> - **Start Node** aksar grid ke open area me hota hai jahan 2 se 3 directions open hoti hain, jisse options ka branching tree bada ho jata hai.
> - **End Node** lagbhag hamesha corner ya constrained edge par locked hota hai jahan aane ka sirf **1 hi valid orientation** possible hota hai.
> - Backward chalne se grid ki 70% se 80% invalid rotations instantly prune (filter out) ho jati hain.

```
Start (Multiple Choices)                      End (Single Fixed Inflow)
      ┌───┐                                         ┌───┐
  ┌──▶│ ? │                                     ───▶│END│ (Only 1 valid side)
  │   └───┘                                         └───┘
[START]───▶ [ ? ] ─── ... ───▶ [ ? ] ◀──────────────┘
  │   ┌───┐
  └──▶│ ? │
      └───┘
(Branching factor = 3)                       (Branching factor = 1 -> ZERO GUESSWORK)
```

---

### Strategy 2: The Anchor Tile Rule (Boundary Elimination)

Grid ke corners aur edges par lage hue tiles ke paas restricted degrees of freedom hoti hain:

1. **Corner L-Tiles Deterministic Hote Hain**:
   - **Top-Left Corner $(1,1)$**: Sirf `DOWN` aur `RIGHT` connect kar sakta hai (Up ya Left bahar chala jayega).
   - **Top-Right Corner $(1,N)$**: Sirf `DOWN` aur `LEFT` connect kar sakta hai.
   - **Bottom-Left Corner $(N,1)$**: Sirf `UP` aur `RIGHT` connect kar sakta hai.
   - **Bottom-Right Corner $(N,N)$**: Sirf `UP` aur `LEFT` connect kar sakta hai.
2. **First Move Rule**: Level shuru hote hi middle tiles chhoone ke bajay pehle boundary aur corner tiles ko unki compulsory orientation me turn kar do.

---

### Strategy 3: Click Economy & Modular Arithmetic

Har tile clockwise $90^\circ$ ghumti hai:
- Target orientation agar $180^\circ$ door hai $\implies$ **2 Clicks**.
- Target orientation agar $270^\circ$ clockwise hai $\implies$ Sirf **3 Clicks** (ya counter-clockwise interface ho toh 1 click).
- **Spamming Penalty**: Kisi tile ko bina dekhe 4-5 baar ghumana engine me trial-and-error metric ko trigger karta hai, jisse candidate ka executive planning score girta hai.

---

## 4. Worked Scenarios & Tactical Walkthroughs

```
Matrix Notation: (Row, Column)
Row 1 = Topmost Row; Row N = Bottommost Row.
Col 1 = Leftmost Col; Col N = Rightmost Col.
```

### Scenario 1: Easy $3\times3$ Grid (Linear Connection)
- **Start Node**: $(1,1)$ [Top-Left] facing **East** (Right).
- **End Node**: $(1,3)$ [Top-Right] facing **West** (Left).
- **Intermediate Tile**: $(1,2)$ par ek L-Tile hai jo currently South-East face kar raha hai.

```
       Col 1        Col 2        Col 3
Row 1 [START ▶] ── [ (1,2) ] ── [◀ END ]
Row 2 [       ]    [       ]    [      ]
Row 3 [       ]    [       ]    [      ]
```

- **Trace Analysis**:
  - Start $(1,1)$ ka flow East ja raha hai $\to (1,2)$ me entering from Left (West).
  - End $(1,3)$ ka flow West se accept hona hai $\to (1,2)$ me exiting towards Right (East).
  - Cell $(1,2)$ ko horizontal straight line banana mandatory hai (`East-West`).
- **Execution**: Tile $(1,2)$ ko rotate karo jab tak horizontal path na ban jaye $\implies$ **Solved in 1-2 clicks**.

---

### Scenario 2: Medium $4\times4$ Grid with Obstacles & Bends
- **Start**: $(1,1)$ [Top-Left], Exit facing Down.
- **End**: $(4,4)$ [Bottom-Right], Entrance facing Up.
- **Dead/Blocked Tile**: Cell $(3,4)$ dead tile hai (impassable).

```
        Col 1     Col 2     Col 3     Col 4
Row 1  [START]    [ · ]     [ · ]     [ · ]
Row 2  [  │  ]    [ · ]     [ · ]     [ · ]
Row 3  [  └  ]─── [ ─ ]───▶ [ ┐ ]   [BLOCKED]
Row 4  [ · ]      [ · ]     [ └ ]───▶ [END]
```

- **Backward Deduction**:
  1. End $(4,4)$ par entrance UP se expected hai, par cell $(3,4)$ BLOCKED hai! Iska matlab path UP se nahi, balki LEFT $(4,3)$ se aayega!
  2. Isliye $(4,4)$ ke L-tile ko rotate karke `UP-LEFT` orient kiya.
  3. Cell $(4,3)$ par L-tile ko `UP-RIGHT` orient kiya jo row 3 ke $(3,3)$ se connect karega.
  4. Cell $(3,3)$ par L-tile ko `DOWN-LEFT` orient kiya jo row 3 col 2 se connect hoga.
- **Result**: Ek structured backward chain ne pure blocked region ko instantly bypass kar diya.

---

### Scenario 3: Complex $5\times5$ Hard Level (KN Academy PYQ Breakdown)

As demonstrated in the verified [KN Academy Accenture Path Game Walkthrough](https://youtu.be/tCQ0hDEWJSI?si=vY7fjCPEHAvLGsLH):
- **Problem Nature**: Grid me continuous loop distractions aur multiple T-junctions hote hain jo false paths banate hain.
- **KN Academy Strategy**:
  1. Subah pehle entry vector identify karo: Start cell se continuous chain banate huye down jao.
  2. Middle junctions par T-tile ke flat blind-end ko bahar ki boundary par align karo taaki wo unwanted cycles me flow na bhej sake `[00:16:50]`.
  3. Direction flipping: Jab tile turn leti hai, check karo ki incoming arrow aur outgoing arrow match ho rahe hain ya nahi `[00:17:17]`.
  4. Ek baar final corridor set ho jaye, last 3 horizontal/vertical straight tiles ko 2-2 clicks me sync karo `[00:17:25]`.

---

## 5. Comprehensive Practice Question Bank (PYQs)

### Question 1
In Path Finder, corner tiles ko sabse pehle kyu identify aur rotate karna chahiye?  
- a) Corner tiles ke 4 valid orientations hote hain  
- b) Corner tiles grid boundary ke karan sirf 2 inner directions me connect ho sakte hain, jisse unki orientation deterministic ho jati hai  
- c) Corner tiles rotate karne par bonus points milte hain  
- d) Corner tiles locked hote hain aur rotate nahi ho sakte  

---

### Question 2
Ek straight-line tile ke total kitne visually unique orientations hote hain?  
- a) 1  
- b) 2 (Horizontal aur Vertical)  
- c) 3  
- d) 4  

---

### Question 3
Agar ek L-bend tile top-right corner $(1,N)$ par placed hai, to kaunsi direction uske path ka hissa KABHI nahi ho sakti?  
- a) Left  
- b) Down  
- c) Up ya Right (grid boundary ke bahar)  
- d) Down aur Left  

---

### Question 4
Ek $3\times3$ grid me Start=(1,1) pointing Right hai. Intermediate cell (1,2) par ek T-junction tile hai. (1,1) ko (1,3) se connect karne ke liye T-junction ka flat side kidhar hona chahiye?  
- a) Flat side facing Top (Left, Right, aur Down connect karta hua)  
- b) Flat side facing Left  
- c) Flat side facing Right  
- d) Pointing Upwards only  

---

### Question 5
Kisi L-tile ko rotate karke dobara uski original position par laane ke liye kitne clicks required hote hain?  
- a) 2 clicks  
- b) 3 clicks  
- c) 4 clicks ($4 \times 90^\circ = 360^\circ$)  
- d) 1 click  

---

### Question 6
Start=(1,1), End=(3,3). Path route: $(1,1) \to (2,1) \to (2,2) \to (3,2) \to (3,3)$. Is pooray path me total kitne L-bend (turning) tiles ki zarurat hogi?  
- a) 1  
- b) 3 (Turns at (2,1), (2,2), and (3,2))  
- c) 4  
- d) 2  

---

### Question 7
Agar grid me ek cross (`+`) tile present hai, to adjacent tiles ko connect karne ke liye use kitne rotation clicks dene padenge?  
- a) 0 clicks (Ye symmetric hota hai aur 4-way connect karta hai)  
- b) 1 click  
- c) 2 clicks  
- d) 4 clicks  

---

### Question 8
Agar tile path ek closed circular loop bana le jo End node tak nahi pahunchta, to game me kya hoga?  
- a) Aap instant match jeet jaoge  
- b) Level unsolved rahega jab tak path End node tak link na ho  
- c) Time increase ho jayega  
- d) Points double ho jayenge  

---

### Question 9
Ek $4\times4$ grid me End node bottom-left corner $(4,1)$ par hai. Wahan par situated L-tile ki ONLY valid orientation kaunsi hogi?  
- a) Up and Right (Row 3 aur Col 2 ki taraf)  
- b) Down and Left  
- c) Up and Left  
- d) Down and Right  

---

### Question 10
Path Finder game me "Backward End-Search" technique sabse zyada effective kyu mani jaati hai?  
- a) End tiles ke paas Start tiles ke mukable kam open connections hote hain, jisse invalid branches jaldi filter out ho jaate hain  
- b) Is se timer pause ho jata hai  
- c) Ye tiles ko automatically rotate kar deta hai  
- d) Is se tiles ka color change ho jata hai  

---

### Question 11
Ek $3\times3$ grid me ek straight tile cell $(2,2)$ par hai. Start=(2,1) [Left] aur End=(2,3) [Right] hai. Cell $(2,2)$ ki valid orientation kya hogi?  
- a) Vertical  
- b) Horizontal (Connecting West to East)  
- c) Diagonal  
- d) Locked  

---

### Question 12
Path Finder level screen par aate hi candidate ka optimal initial move kya hona chahiye?  
- a) Sabhi tiles ko bina dekhe ek-ek baar click karna  
- b) Start aur End ke adjacent corner/boundary anchor tiles ko pehle lock karna  
- c) Center tile ko 10 baar click karna  
- d) 30 seconds tak timer ka wait karna  

---

### Question 13
Ek standard T-junction tile kitni directions me simultaneously connections provide karti hai?  
- a) 2  
- b) 3  
- c) 4  
- d) 1  

---

### Question 14
Ek $5\times5$ grid me jisme 10–12 movable tiles hain, candidate ka per-level benchmark solving time kitna hona chahiye?  
- a) 10–15 seconds  
- b) 2 minutes  
- c) 5 minutes  
- d) 30 milliseconds  

---

### Question 15
Accenture ka Path Finder mini-game candidate ki kaunsi core cognitive abilities measure karta hai?  
- a) English vocabulary  
- b) 2D Spatial mental rotation, deductive reasoning aur visual pattern synthesis  
- c) Coding syntax  
- d) Typing speed  

---

## 6. Complete Answer Key & Step-by-Step Logic

| Q.No | Correct Option | Detailed Step-by-Step Logic |
| :---: | :---: | :--- |
| **Q1** | **b** | Grid borders ke karan corner tiles ke 2 sides external wall se block hote hain. Isliye unka orientation fixed hota hai. |
| **Q2** | **b** | Straight line ko $90^\circ$ ghumao toh Vertical, $180^\circ$ pe wapas Horizontal. Total unique visual states = 2. |
| **Q3** | **c** | Top-right cell $(1,N)$ se Up jana Row 0 (out of bounds) hoga aur Right jana Col $N+1$ (out of bounds) hoga. |
| **Q4** | **a** | Flat back agar Top pe hogi to uski bottom opening Row 2 me jayegi aur horizontal arms Left (Start) aur Right (End) ko seamless connect karengi. |
| **Q5** | **c** | Ek click = $90^\circ$. $360^\circ$ complete rotation ke liye $360 / 90 = 4$ discrete clicks lagte hain. |
| **Q6** | **b** | Movement direction 3 baar badalti hai: $(2,1)$ pe South se East, $(2,2)$ pe East se South, aur $(3,2)$ pe South se East $\implies$ 3 L-bends. |
| **Q7** | **a** | Cross tile $90^\circ$ rotational symmetry rakhta hai. Iske chaaro arms har waqt connected rehte hain, rotation clicks = 0. |
| **Q8** | **b** | System tabhi clearance signal deta hai jab Start cell se nikla hua continuous vector End node cell ke terminal point me enter kare. |
| **Q9** | **a** | Bottom-left corner $(N,1)$ se Left aur Down grid se bahar hain. Rasta sirf UP (Row $N-1$) aur RIGHT (Col 2) ja sakta hai. |
| **Q10** | **a** | Reverse engineering branching factor ko 3 se ghata kar 1 kar deti hai, jisse time aur redundant clicks bachte hain. |
| **Q11** | **b** | Same row $(2)$ me Left cell $(2,1)$ se Right cell $(2,3)$ connect karne ke liye tile ko Horizontal (`─`) hona compulsory hai. |
| **Q12** | **b** | Boundary anchors fix karne se puzzle ka perimeter lock ho jata hai, jisse middle tiles ka rasta clear dikhne lagta hai. |
| **Q13** | **b** | T-shape tile me 3 open terminals aur 1 blind boundary hoti hai $\implies$ 3 connections. |
| **Q14** | **a** | Accenture ke high score percentile band me aane ke liye 10–15 seconds per grid ka benchmark speed standard mana jata hai. |
| **Q15** | **b** | Assessment engine candidate ki mental rotation speed aur spatial deductive reasoning ko score karta hai. |

---

## 7. Verified Practice Simulator & Video Resources

In verified links se live practice karein aur gameplay strategies internalize karein:

### Interactive Practice Tool
- **[BuildUForward Accenture Path Finder Practice Tool](https://www.builduforward.com/accenture-gamified-assessment/path-finder)**  
  *Free browser simulator jisme real assessment UI, rotatable tile matrices ($3\times3, 4\times4, 5\times5$), live timers aur scoring metrics available hain bina kisi sign-up ke.*
- **[JustNK Accenture Gaming Round Detailed Notes](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html)**  
  *Mini-game timings, platform patterns aur stage cut-offs ka comprehensive written analysis.*

### Video Walkthroughs
- **[KN Academy: Accenture Path Game Solution (Hardest PYQs Explained)](https://youtu.be/tCQ0hDEWJSI?si=vY7fjCPEHAvLGsLH)**  
  *Detailed 18-minute breakdown jisme complex $5\times5$ grids, direction flipping aur tile rotation shortcuts step-by-step sikhaye gaye hain.*
- **[Accenture Cognitive Assessment Full Gameplay Walkthrough](https://www.youtube.com/watch?v=tsW_BL8hSBY)**  
  *Live recording of all mini-games under actual platform conditions and time limits.*

---

## 8. Test-Day Golden Checklist for Path Finder

```
[ ] Rule 1: Level load hote hi End node ka incoming vector check karo (Reverse Search).
[ ] Rule 2: Corner tiles aur outer boundary tiles ko pehle rotate karke lock karo (Anchor Strategy).
[ ] Rule 3: Cross (+) tiles par kabhi click mat karo—unka orientation already perfect hota hai.
[ ] Rule 4: Clicks count bachao; L-tile ko 3 baar clockwise ghumane ke bajay visualize karo.
[ ] Rule 5: Target benchmark: Har puzzle 10–15 seconds me finish karo with zero broken loops.
```
