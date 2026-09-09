# Accenture Gamified Assessment: Memory Maze & Door Navigation Guide

> **Target Assessment**: Accenture Cognitive / Gamified Assessment (powered by SHL, Aon / cut-e, and HireVue platforms)  
> **Topic**: Spatial Working Memory, Executive Planning, and Hidden Maze Navigation  
> **Document Purpose**: Comprehensive master guide synthesizing mechanics, variants, mathematical chunking frameworks, worked scenarios, PYQ question bank, and verified practice resources.

---

## 1. Assessment Overview & Cognitive Profile

Memory Maze (also termed **Door & Maze** or **Pathfinder / Grid Navigation**) is an elimination-grade mini-game featured in **Stage 1 (Cognitive Gamified Assessment)** of the Accenture recruitment pipeline. It evaluates non-verbal reasoning, spatial short-term working memory, and adaptive decision-making under high time pressure.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CORE GAME PROGRESSION                              │
│                                                                             │
│   [ Start Cell ] ──────(Path A)──────> [ Key Cell ] ──────(Path B)──────>   │
│   Initial Position                     Objective 1                          │
│                                                                             │
│                                        [ Exit Door ]                        │
│                                        Final Exit (Unlocks only with Key)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Cognitive Metrics Tracked by the Engine
1. **Spatial Working Memory**: Ability to store mental representations of grid matrices ($3\times3$ to $6\times6$).
2. **Executive Routing & Path Efficiency**: Calculation of optimal Manhattan distances without redundant moves.
3. **Resilience & Negative Memory Updating**: Rapidly mapping collision points without panic-clicking after forced resets.
4. **Processing Speed vs. Error Rate Trade-off**: Balancing swift keyboard/click execution against collision penalties.

---

## 2. The Two Assessment Variants: Comparative Analysis

Candidates across testing cycles encounter two distinct implementations depending on the underlying test provider. Understanding which version is on your screen within the first two seconds is critical.

| Assessment Dimension | Variant A: Classic Memory Maze (Aon / cut-e style) | Variant B: Trial-and-Error Blind Maze (SHL / Custom style) |
| :--- | :--- | :--- |
| **Preview Window** | **3 to 5 seconds visible preview** displaying walls, start, key, and door before darkening. | **No initial preview** of walls. Grid displays only Start, Key, and Door. Walls are completely invisible. |
| **Primary Challenge** | Rapid spatial encoding into working memory before screen hides walls. | Dynamic hypothesis testing, path probing, and negative obstacle mapping. |
| **Collision Consequence** | Step rollback with time penalty or brief grid flicker. | **Immediate full reset** back to the initial starting position. |
| **Exploration Mode** | Deterministic pre-planned execution. | Incremental route discovery across repeated attempts. |
| **Optimal Strategy** | **3-Anchor Vector Chunking** (`R2-U3` $\rightarrow$ `U2-L1`). | **Greedy Shortest Path Probing + Mental Obstacle Tagging**. |

---

## 3. Core Strategy Frameworks

### Strategy 1: The 3-Anchor Chunking Technique (For Variant A)

Human working memory reliably maintains only $3\text{ to }4$ information units ("chunks") under acute stress (Miller's Law / Cowan's working memory model). Attempting to memorize all 25 cells of a $5\times5$ grid induces immediate cognitive overload.

#### Chunking Breakdown:
- **Anchor 1**: Start Coordinate $(x_1, y_1)$
- **Anchor 2**: Key Coordinate $(x_2, y_2)$
- **Anchor 3**: Exit Door Coordinate $(x_3, y_3)$

Convert the visual path into a **2-part directional vector chain**:
$$\text{Vector Sequence} = \underbrace{\Big[ \Delta x_A, \Delta y_A \Big]}_{\text{Path A: Start } \to \text{ Key}} \quad \longrightarrow \quad \underbrace{\Big[ \Delta x_B, \Delta y_B \Big]}_{\text{Path B: Key } \to \text{ Door}}$$

```
Visual Matrix (Overload)                 Chunked Vector Code (Optimal)
┌───┬───┬───┬───┐                        
│ D │ · │ · │ K │                        Path A (Start → Key):
├───┼───┼───┼───┤                        "2 Up, 3 Right" -> [U2, R3]
│ · │ ■ │ · │ · │                        
├───┼───┼───┼───┤                        Path B (Key → Door):
│ · │ · │ ■ │ · │                        "3 Left"        -> [L3]
├───┼───┼───┼───┤                        
│ S │ · │ · │ · │                        Memory footprint: 2 chunks only!
└───┴───┴───┴───┘                        
```

---

### Strategy 2: Blind Probing & Negative-Space Mapping (For Variant B)

When navigating blind grids with automatic resets:

1. **Greedy Manhattan Initialization**: On Run 1, always attempt the direct Manhattan vector toward the Key:
   $$D_{\text{Manhattan}} = |x_{\text{key}} - x_{\text{start}}| + |y_{\text{key}} - y_{\text{start}}|$$
2. **Tag the Obstacle Junction**: When a collision resets you, store the blocked transition in memory as a forbidden coordinate (e.g., $(2,2) \xrightarrow{\text{UP}} (2,3)$ is blocked).
3. **Execute the Pivot**: Retrace the verified safe steps at maximum speed, then pivot one coordinate before the known wall.
4. **Preserve Key Checkpoints**: After obtaining the Key, explore toward the Door. If reset, remember that the Key path is already solved; you simply re-execute Path A without hesitation and branch only on Path B.

---

## 4. Worked Scenarios & Tactical Walkthroughs

```
Coordinate Notation: (x, y) where x = Column (1 to N, Left to Right), y = Row (1 to N, Bottom to Top).
Standard Directional Controls: U = Up (+y), D = Down (-y), L = Left (-x), R = Right (+x).
```

### Scenario 1: Easy $3\times3$ Grid (Variant A Walkthrough)
- **Start**: $(1, 1)$ [Bottom-Left]
- **Key**: $(1, 3)$ [Top-Left]
- **Door**: $(3, 3)$ [Top-Right]
- **Obstacle**: Wall at $(2, 3)$

```
  y
3 ┌──────┬──────┬──────┐
  │ Key  │ Wall │ Door │
  │(1,3) │(2,3) │(3,3) │
2 ├──────┼──────┼──────┤
  │      │      │      │
  │(1,2) │(2,2) │(3,2) │
1 ├──────┼──────┼──────┤
  │Start │      │      │
  │(1,1) │(2,1) │(3,1) │
  └──────┴──────┴──────┘
     1      2      3   x
```

- **Path A (Start $\to$ Key)**: $(1,1) \to (1,2) \to (1,3)$ $\implies$ **`U, U`** (2 steps)
- **Path B (Key $\to$ Door)**: Direct move right blocked by $(2,3)$. Bypass via row 2: $(1,3) \to (1,2) \to (2,2) \to (3,2) \to (3,3)$ $\implies$ **`D, R, R, U`** (4 steps)
- **Consolidated Vector Code**: `[U2] -> [D1, R2, U1]` (Total = 6 moves).

---

### Scenario 2: Medium $4\times4$ Grid with Obstacles
- **Start**: $(1, 1)$
- **Key**: $(3, 3)$
- **Door**: $(4, 1)$
- **Obstacles**: Walls at $(2, 2)$ and $(3, 2)$

```
  y
4 ┌──────┬──────┬──────┬──────┐
  │      │      │      │      │
3 ├──────┼──────┼──────┼──────┤
  │      │      │ Key  │      │
2 ├──────┼──────┼──────┼──────┤
  │      │ Wall │ Wall │      │
1 ├──────┼──────┼──────┼──────┤
  │Start │      │      │ Door │
  └──────┴──────┴──────┴──────┘
     1      2      3      4   x
```

- **Analysis to Key**: Moving along row 1 then up to $(3,3)$ encounters wall $(3,2)$. Route through column 1: $(1,1) \to (1,2) \to (1,3) \to (2,3) \to (3,3)$ $\implies$ **`U, U, R, R`**.
- **Analysis to Door**: From $(3,3)$, moving down encounters wall $(3,2)$. Step right into column 4, then straight down: $(3,3) \to (4,3) \to (4,2) \to (4,1)$ $\implies$ **`R, D, D`**.
- **Consolidated Vector Code**: `[U2, R2] -> [R1, D2]` (Total = 7 moves).

---

### Scenario 3: Hard $5\times5$ Grid (Perimeter Bypass)
- **Start**: $(2, 1)$
- **Key**: $(5, 5)$
- **Door**: $(1, 5)$
- **Obstacles**: Cluster blocking central interior cells $(3,2), (3,3), (3,4), (4,3)$
- **Optimal Route**:
  - Start $(2,1)$ to Key $(5,5)$: Perimeter right and up $\to (5,1) \to (5,5)$ $\implies$ **`R3, U4`** (7 steps).
  - Key $(5,5)$ to Door $(1,5)$: Direct unobstructed top corridor $\to$ **`L4`** (4 steps).
- **Consolidated Vector Code**: `[R3, U4] -> [L4]` (Total = 11 moves).

---

## 5. Comprehensive Practice Question Bank (PYQs)

### Question 1
In a $4\times4$ grid, Start is at $(1,1)$, Key is at $(1,4)$, and Door is at $(4,4)$. A wall blocks cell $(1,3)$. What is the shortest safe movement sequence to collect the Key?  
- a) `UP, UP, UP`  
- b) `RIGHT, UP, UP, LEFT, UP`  
- c) `UP, RIGHT, UP, LEFT, UP`  
- d) `RIGHT, RIGHT, UP, UP`  

---

### Question 2
What is the primary factor that causes score reductions in the Accenture Memory Maze assessment?  
- a) Taking more than 2 seconds to view the initial preview  
- b) Colliding with an obstacle/wall boundary  
- c) Reaching the Door cell before collecting the Key  
- d) Both b and c  

---

### Question 3
In a $3\times3$ grid, Start=$(2,1)$, Key=$(2,3)$, and Door=$(3,1)$. A wall is located at $(2,2)$. Which of the following routes reaches the Key safely?  
- a) $(2,1) \to (2,2) \to (2,3)$  
- b) $(2,1) \to (1,1) \to (1,3) \to (2,3)$  
- c) $(2,1) \to (3,1) \to (3,3) \to (2,3)$  
- d) Both b and c are valid paths  

---

### Question 4
According to cognitive chunking models, what is the most efficient data format to retain in memory for a $4\times4$ maze?  
- a) All 16 individual grid cell states  
- b) 2 directional vector sequences (Start $\to$ Key, Key $\to$ Door)  
- c) Coordinate pairs of every wall tile  
- d) Visual color shading of the board  

---

### Question 5
In an open $4\times4$ maze with zero internal walls, Start is at $(1,2)$, Key is at $(4,2)$, and Door is at $(4,4)$. What is the minimum number of steps required to finish?  
- a) 3 steps  
- b) 5 steps  
- c) 7 steps  
- d) 4 steps  

---

### Question 6
In the blind trial-and-error variant (Variant B), what happens immediately when your character collides with a hidden wall?  
- a) The assessment is instantly terminated with a zero score  
- b) The player position resets back to the initial starting cell  
- c) The wall becomes permanently transparent and you pass through  
- d) You automatically skip to the next game  

---

### Question 7
In a $5\times5$ grid, Start=$(1,1)$, Key=$(1,5)$, Door=$(5,5)$. Interior walls block cells $(1,2), (1,3),$ and $(1,4)$. How must you navigate to the Key?  
- a) Step RIGHT to $(2,1)$, move UP 4 steps to $(2,5)$, then step LEFT to $(1,5)$  
- b) Move straight UP through the walls  
- c) Step to the Door first to trigger a bypass  
- d) The maze is mathematically unsolvable  

---

### Question 8
Why is backward planning (Door $\to$ Key $\to$ Start) often effective during the initial preview window?  
- a) The exit door area frequently features more corridor constraints, narrowing route permutations early  
- b) It extends the preview countdown timer  
- c) It reverses the positions of obstacles  
- d) It is required by the game engine to submit scores  

---

### Question 9
In a $4\times4$ grid, Key is located at $(3,3)$ and Door is located at $(3,3)$. How many steps are required between collecting the Key and exiting?  
- a) 1 step  
- b) 0 steps (instant level completion upon arrival)  
- c) 4 steps  
- d) 2 steps  

---

### Question 10
Start=$(1,1)$, Key=$(2,2)$, Door=$(1,1)$. Path taken: $(1,1) \to (1,2) \to (2,2)$ [Key] $\to (2,1) \to (1,1)$ [Door]. What is the total move count?  
- a) 2  
- b) 3  
- c) 4  
- d) 5  

---

### Question 11
What is the recommended recovery technique if you experience cognitive blackout halfway through a maze run?  
- a) Rapidly spam all directional keys randomly  
- b) Let the timer expire without touching the controls  
- c) Safely retrace moves along the confirmed open path or systematically probe adjacent open cells  
- d) Refresh the browser window  

---

### Question 12
In a $4\times4$ square navigation grid, what is the total number of cells?  
- a) 12  
- b) 16  
- c) 20  
- d) 25  

---

### Question 13
In a $3\times3$ grid: Start=$(1,1)$, Key=$(3,3)$, Door=$(1,3)$. Path to Key: $(1,1) \to (3,1) \to (3,3)$. Path to Door: $(3,3) \to (1,3)$. What is the total step distance?  
- a) 4 steps  
- b) 6 steps  
- c) 8 steps  
- d) 5 steps  

---

### Question 14
True or False: Diagonal directional inputs (e.g., UP-RIGHT) are permitted in standard Memory Maze assessments.  
- a) True  
- b) False (movement is strictly 4-directional cardinal: Up, Down, Left, Right)  

---

### Question 15
Which core cognitive executive functions are tested by the Memory Maze challenge?  
- a) Verbal comprehension and lexical recall  
- b) Spatial working memory, visuospatial reasoning, and motor execution speed  
- c) Abstract code debugging  
- d) Complex numerical trigonometry  

---

## 6. Complete Answer Key & Explanations

| Question | Correct Option | Detailed Explanation |
| :---: | :---: | :--- |
| **Q1** | **b** | Direct upward movement along Column 1 is blocked at $(1,3)$. Shifting right to Column 2 via $(2,1)$, moving up to $(2,4)$, and stepping left into $(1,4)$ safely circumvents the barrier. |
| **Q2** | **d** | Both wall collisions and sequence violations (reaching exit before key) incur heavy penalties or immediate reset loops. |
| **Q3** | **d** | Both the left flank ($(1,1) \to (1,3)$) and right flank ($(3,1) \to (3,3)$) offer obstacle-free paths around central block $(2,2)$. |
| **Q4** | **b** | Directional vectors condense complex 2D arrays into 2 atomic chunks, fitting within human working memory bandwidth ($7 \pm 2$, reduced to $3-4$ under stress). |
| **Q5** | **b** | Manhattan distance: $(1,2) \to (4,2)$ is $|4-1| + |2-2| = 3$ steps right. $(4,2) \to (4,4)$ is $|4-4| + |4-2| = 2$ steps up. Total = $3 + 2 = 5$ steps. |
| **Q6** | **b** | As demonstrated in trial-and-error variants, hitting an invisible boundary immediately resets the avatar to the starting point. |
| **Q7** | **a** | Column 1 is entirely barricaded between rows 2 and 4. Navigating into Column 2 is compulsory to bypass the vertical wall segment. |
| **Q8** | **a** | Endpoints often sit near corners or bottlenecks with fewer degree-of-freedom exits, making them faster to prune during preview analysis. |
| **Q9** | **b** | Because the Key and Door occupy the exact same coordinate cell, reaching the Key automatically triggers the Door clearance. |
| **Q10** | **c** | Step 1: $(1,1) \to (1,2)$; Step 2: $(1,2) \to (2,2)$ [Key]; Step 3: $(2,2) \to (2,1)$; Step 4: $(2,1) \to (1,1)$ [Door]. Total = 4 discrete moves. |
| **Q11** | **c** | Panic clicking triggers repeated collisions. Methodical backtracking or conservative probing prevents compounding penalty points. |
| **Q12** | **b** | Standard quadratic dimension: $4 \times 4 = 16$ total grid cells. |
| **Q13** | **b** | Leg 1: $(1,1) \to (3,1)$ [2 steps right] + $(3,1) \to (3,3)$ [2 steps up] = 4 steps. Leg 2: $(3,3) \to (1,3)$ [2 steps left] = 2 steps. Total = 6 steps. |
| **Q14** | **b** | Input schemes are strictly cardinal (North, South, East, West / 4-way direction pad). |
| **Q15** | **b** | Test engines explicitly evaluate visuospatial scratchpad capacity and spatial execution planning. |

---

## 7. Verified Interactive Tools & Video Resources

Practice and internalize these patterns using these verified resources:

### Interactive Practice Platforms
- **[BuildUForward Accenture Memory Maze Practice Simulator](https://www.builduforward.com/accenture-gamified-assessment/memory-maze)**  
  *Direct interactive browser simulator replicating Accenture/Aon grid constraints, preview timers, and scoring conditions without login.*
- **[JustNK Accenture Gamified Round Detailed Analysis](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html)**  
  *Detailed breakdowns of game types, mini-game sequences, and benchmark scoring metrics.*

### Video Walkthroughs & Game Demos
- **[OnlineStudy4u: Accenture Door & Maze Problems Explained](https://www.youtube.com/watch?v=ll1srQueVrQ)**  
  *Detailed 16-minute step-by-step video breakdown of the trial-and-error blind maze variant, obstacle collision handling, and reset rules.*
- **[Accenture Gaming Cognitive Assessment Walkthrough Video](https://www.youtube.com/watch?v=tsW_BL8hSBY)**  
  *Visual guide demonstrating real-time memory chunking, keyboard movement flow, and preview strategy.*

---

## 8. Summary Checklist for Test Day

```
[ ] Step 1: Check preview condition.
            - If grid is visible: Lock 3 Anchors (Start, Key, Door) -> Derive vector code.
            - If walls are hidden: Probe direct Manhattan route -> Log collisions on reset.
[ ] Step 2: Chunk vectors as [Path A] -> [Path B] (e.g., U2-R3 -> D2-L1).
[ ] Step 3: Maintain strict cardinal inputs; avoid spamming keyboard buttons.
[ ] Step 4: Prioritize zero collisions over sub-second speed; accuracy dominates cognitive scoring.
```
