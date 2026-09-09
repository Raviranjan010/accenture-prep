# Accenture Cognitive Assessment: Memory Maze & Door Navigation Master Guide (Hinglish Edition)

> **Exam Target**: Accenture Placement - Stage 1 Gamified Cognitive Assessment (Aon / cut-e & SHL Platforms)  
> **Topic**: Spatial Working Memory, Rapid Vector Chunking & Hidden Maze Pathfinding  
> **Language**: Hinglish (Clear, In-Depth, Concept-Focused)

---

## 1. Game Ka Overview & Cognitive Architecture

Accenture ke assessment me **Memory Maze** (Door & Maze / Pathfinder) ek elimination-grade mini-game hai. Iska objective simple dikhta hai par iska backend engine complex cognitive metrics measure karta hai:

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CORE GAME LOOP                                        │
│                                                                                         │
│   [ START CELL ] ──────────(Path A)──────────> [ KEY CELL ] ──────────(Path B)──────>   │
│   Initial Avatar                               Primary Target                           │
│                                                                                         │
│                                                [ EXIT DOOR ]                            │
│                                                Final Objective (Only unlocks with Key)  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### System Backend Me Kya Track Karta Hai?
1. **Collision Count (Pure Accuracy)**: Wall ya hurdle se takraaye bina safe path nikalna. Zero collision walo ko maximum score milta hai.
2. **Manhattan Path Efficiency**: Kahi aap lambe routes to nahi le rahe? Formula:  
   $$\text{Manhattan Distance } D = |x_2 - x_1| + |y_2 - y_1|$$
3. **Negative Mental Mapping**: Agar wall se takraye, to reset hone ke baad kya aap usi galti ko dobara repeat karte ho ya turant pivot karte ho?
4. **Execution Speed vs. Error Balance**: Fast button press karna accha hai, par agar collision hui to speed ka koi faayda nahi.

---

## 2. Dono Assessment Variants Ka Comparison

Candidates sabse badi galti tab karte hain jab wo dono variants ko ek hi samajh lete hain. Test shuru hote hi pehle 2 seconds me identify karo:

| Comparison Parameter | Variant A: Classic Memory Maze (cut-e / Aon) | Variant B: Trial & Error Blind Maze (SHL Style) |
| :--- | :--- | :--- |
| **Preview Screen** | **3 se 5 seconds ka preview** milta hai jisme walls visible hoti hain, fir grid dark ho jati hai. | **Zero initial preview**. Walls shuru se invisible rehti hain, sirf Start, Key aur Door dikhte hain. |
| **Collision Rule** | Step rollback ya flicker hota hai, thoda time penalty milta hai. | **Strict Full Reset!** Collision hote hi avatar turant initial start point pe spawn ho jata hai. |
| **Solving Approach** | **3-Anchor Vector Chunking**: Preview me hi pura code dimag me ratt lo. | **Greedy Manhattan Probing + Negative Obstacle Tagging**. |
| **Core Skill Tested** | Visuospatial working memory & recall capacity. | Dynamic trial resilience, spatial mapping, and route re-planning. |

---

## 3. Proven Strategic Frameworks

### Strategy 1: The 3-Anchor Chunking Technique (Variant A ke liye)

Puri 25-cell ($5\times5$) grid ko visual image ki tarah yaad rakhna human memory limit ke khilaaf hai (Miller's Law ke mutabiq acute stress me brain sirf 3-4 chunks hold kar pata hai).

#### Three-Anchor Rule:
Puri grid yaad mat karo; sirf 3 reference coordinates lock karo:
- **Anchor 1**: Start Coordinate $(x_1, y_1)$
- **Anchor 2**: Key Coordinate $(x_2, y_2)$
- **Anchor 3**: Door Coordinate $(x_3, y_3)$

Isko 2 directional vectors me encode karo:
$$\text{Vector Memory Code} = \underbrace{\Big[ \text{Start } \to \text{ Key} \Big]}_{\text{Chunk 1 (Path A)}} \quad \longrightarrow \quad \underbrace{\Big[ \text{Key } \to \text{ Door} \Big]}_{\text{Chunk 2 (Path B)}}$$

```
Visual Matrix (Overload)                 Chunked Vector (Mental Shortcut)
┌───┬───┬───┬───┐                        
│ D │ · │ · │ K │                        Path A (Start → Key):
├───┼───┼───┼───┤                        "2 Up, 3 Right"  -> [U2, R3]
│ · │ ■ │ · │ · │                        
├───┼───┼───┼───┤                        Path B (Key → Door):
│ · │ · │ ■ │ · │                        "3 Left"         -> [L3]
├───┼───┼───┼───┤                        
│ S │ · │ · │ · │                        Dimag me sirf 2 vectors yaad rakhne hain!
└───┴───┴───┴───┘                        
```

---

### Strategy 2: Blind Probing & Negative-Space Mapping (Variant B ke liye)

Agar walls shuru se invisible hain:

1. **Greedy Manhattan Route Lo**: Shuru me assume karo koi wall nahi hai aur direct shortest route probe karo. Pehle hi lamba route lena bewakoofi hai.
2. **Takkar Point Yaad Rakho (Negative Tagging)**: Jaise hi kisi cell pe wall hit ho aur avatar reset ho jaye, us blocked direction ko mentally mark kar lo (e.g., `(2,2) se UP jana blocked hai`).
3. **Next Attempt me Fast Execution**: Pichle safe steps ko fast press karo aur wall se theek 1 step pehle detour le lo.
4. **Key Milne Ke Baad Door**: Key milte hi Path A solve ho chuka hai. Door jate waqt agar reset hue, to Path A bina soche fast chalna hai aur sirf Path B me naya turn try karna hai.

---

## 4. Step-by-Step Worked Scenarios

```
Coordinate Standard: (x, y) Jahan x = Column (Left to Right 1 to N), y = Row (Bottom to Top 1 to N).
Directions: U = Up (+y), D = Down (-y), L = Left (-x), R = Right (+x).
```

### Scenario 1: Easy $3\times3$ Grid (Wall Bypass)
- **Start**: $(1, 1)$ [Bottom-Left]
- **Key**: $(1, 3)$ [Top-Left]
- **Door**: $(3, 3)$ [Top-Right]
- **Wall**: $(2, 3)$ blocked

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

- **Path A (Start $\to$ Key)**: $(1,1) \to (1,2) \to (1,3)$ $\implies$ **`U, U`** (2 moves)
- **Path B (Key $\to$ Door)**: Right move blocked by $(2,3)$. Row 2 se bypass karo: $(1,3) \to (1,2) \to (2,2) \to (3,2) \to (3,3)$ $\implies$ **`D, R, R, U`** (4 moves)
- **Final Vector Sequence**: `[U2] -> [D1, R2, U1]` (Total = 6 moves)

---

### Scenario 2: Medium $4\times4$ Grid (Dual Obstacles)
- **Start**: $(1, 1)$, **Key**: $(3, 3)$, **Door**: $(4, 1)$
- **Walls**: $(2, 2)$ aur $(3, 2)$

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

- **Route to Key**: Bottom lane se right jana fail hoga kyuki $(3,2)$ blocked hai. Column 1 se upar jao: $(1,1) \to (1,2) \to (1,3) \to (2,3) \to (3,3)$ $\implies$ **`U, U, R, R`**.
- **Route to Door**: $(3,3)$ se neeche $(3,2)$ pe wall hai. Right shift karo Column 4 me fir straight down: $(3,3) \to (4,3) \to (4,2) \to (4,1)$ $\implies$ **`R, D, D`**.
- **Final Vector Sequence**: `[U2, R2] -> [R1, D2]` (Total = 7 moves).

---

### Scenario 3: Hard $5\times5$ Grid (Boundary Corridor Technique)
- **Start**: $(2, 1)$, **Key**: $(5, 5)$, **Door**: $(1, 5)$
- **Obstacles**: Center cells $(3,2), (3,3), (3,4)$ me maze clusters hain.
- **Route**:
  - Center me ghusne ke bajay perimeter pakdo: Right edge pe jao $(5,1)$, fir straight up to $(5,5)$ $\implies$ **`R3, U4`** (Key collect).
  - Key $(5,5)$ se direct open top lane pakad ke left door $(1,5)$ pe jao $\implies$ **`L4`**.
- **Final Vector Sequence**: `[R3, U4] -> [L4]` (Total = 11 moves).

---

## 5. Complete PYQ Question Bank (15 Practice Questions)

### Q1. Ek $4\times4$ grid me Start=(1,1), Key=(1,4), Door=(4,4) hai. Cell (1,3) blocked hai. Key tak ka safe shortest sequence kya hai?
- a) `UP, UP, UP`
- b) `RIGHT, UP, UP, LEFT, UP`
- c) `UP, RIGHT, UP, LEFT, UP`
- d) `RIGHT, RIGHT, UP, UP`

---

### Q2. Memory Maze me score girne ka sabse bada reason kya hota hai?
- a) 2 second se zyada preview dekhna
- b) Wall boundaries se takrana (Collisions)
- c) Key lene se pehle Door pe chale jana
- d) Dono b aur c

---

### Q3. Ek $3\times3$ grid me Start=(2,1), Key=(2,3), Door=(3,1) hai. Central wall (2,2) pe hai. Safe route kaunsa hai?
- a) $(2,1) \to (2,2) \to (2,3)$
- b) $(2,1) \to (1,1) \to (1,3) \to (2,3)$
- c) $(2,1) \to (3,1) \to (3,3) \to (2,3)$
- d) Dono b aur c valid hain

---

### Q4. Working memory load kam karne ke liye $4\times4$ grid me dimag me kya store karna sabse efficient hai?
- a) 16 individual grid cells ki picture
- b) 2 Directional vector sequences (Start $\to$ Key, Key $\to$ Door)
- c) Sabhi walls ke coordinate pairs
- d) Screen colors

---

### Q5. Ek khali $4\times4$ grid me koi internal wall nahi hai. Start=(1,2), Key=(4,2), Door=(4,4). Minimum kitne moves lagenge?
- a) 3 steps
- b) 5 steps
- c) 7 steps
- d) 4 steps

---

### Q6. Blind trial-and-error variant (Variant B) me agar character hidden wall se takraye to kya hota hai?
- a) Assessment fail ho jata hai
- b) Character starting point pe reset ho jata hai
- c) Wall visible ho jati hai aur aap pass kar jate ho
- d) Question skip ho jata hai

---

### Q7. $5\times5$ grid me Start=(1,1), Key=(1,5) aur Column 1 me cells (1,2), (1,3), (1,4) sabhi blocked hain. Key lene kaise jaoge?
- a) Move RIGHT to (2,1), UP 4 steps to (2,5), then LEFT to (1,5)
- b) Move straight UP wall ke aar-paar
- c) Pehle Door jaoge
- d) Level impossible hai

---

### Q8. Preview window me Backward planning (Door $\to$ Key $\to$ Start) kyu useful hoti hai?
- a) Door visual me bada hota hai
- b) Exit door ke aas-paas narrow corridor choices kam hoti hain, jisse path jaldi lock ho jata hai
- c) Timer reset ho jata hai
- d) Walls ki position change ho jati hai

---

### Q9. Agar Key=(3,3) pe hai aur Door bhi (3,3) pe hi hai, to Key lene ke baad Door tak kitne moves chalne honge?
- a) 1 move
- b) 0 moves (pahunchte hi automatically level clear)
- c) 4 moves
- d) 2 moves

---

### Q10. Start=(1,1), Key=(2,2), Door=(1,1). Route: (1,1) $\to$ (1,2) $\to$ (2,2) [Key] $\to$ (2,1) $\to$ (1,1) [Door]. Total discrete moves kitne hue?
- a) 2
- b) 3
- c) 4
- d) 5

---

### Q11. Agar test ke dauran bich raste me blackout ho jaye ya path bhool jao, to sabse safe recovery step kya hai?
- a) Tezi se randomly arrow keys spam karna
- b) Timer khatam hone dena
- c) Verified open path pe safe backtrack karna ya single adjacent cell probe karna
- d) Browser page refresh kar dena

---

### Q12. $4\times4$ square grid me total kitne individual cells hote hain?
- a) 12
- b) 16
- c) 20
- d) 25

---

### Q13. $3\times3$ grid me: Start=(1,1), Key=(3,3), Door=(1,3). Path to Key: (1,1) $\to$ (3,1) $\to$ (3,3). Path to Door: (3,3) $\to$ (1,3). Total kitne steps hue?
- a) 4 steps
- b) 6 steps
- c) 8 steps
- d) 5 steps

---

### Q14. True ya False: Memory Maze me kya candidate diagonal moves (tirche kadam) chal sakta hai?
- a) True (Diagonal movement allowed hai)
- b) False (Movement strictly 4-directional cardinal hoti hai: Up, Down, Left, Right)

---

### Q15. Ye mini-game candidate ki kaunsi cognitive capability sabse zyada test karta hai?
- a) English vocabulary
- b) Visuospatial working memory aur executive path planning
- c) Coding syntax
- d) Accounts & finance

---

## 6. Detailed Answer Key & Explanations

| Q.No | Ans | Detailed Explanation (Hinglish) |
| :---: | :---: | :--- |
| **Q1** | **b** | Direct up jana blocked hai (1,3) pe. Column 2 me shift karke bypass lena padega: $(1,1) \to (2,1) \to (2,4) \to (1,4)$. |
| **Q2** | **d** | Wall collisions accuracy ko khatam karti hain, aur bina Key liye Door pe jana sequence violation penalty deta hai. |
| **Q3** | **d** | Center wall (2,2) ke dono sides (Left flank Column 1 aur Right flank Column 3) clear hain. |
| **Q4** | **b** | 16 individual grid cells visual overload dete hain; 2 directional vectors chunking rules ke mutabiq perfect hain. |
| **Q5** | **b** | Manhattan distance: $(1,2) \to (4,2)$ = 3 Right steps; $(4,2) \to (4,4)$ = 2 Up steps. Total = $3 + 2 = 5$ moves. |
| **Q6** | **b** | Blind reset variant me kisi bhi wall collision pe avatar turant original starting cell pe spawn ho jata hai. |
| **Q7** | **a** | Column 1 pura vertical blocked hai rows 2-4 me. Column 2 se bypass mandatory hai. |
| **Q8** | **a** | Endpoints ke paas constrained corridors hote hain, isliye reverse analysis se false paths jaldi eliminate ho jate hain. |
| **Q9** | **b** | Jab Key aur Door same cell coordinate share karte hain, to Key pick karte hi stage 0 extra moves me pass ho jati hai. |
| **Q10** | **c** | Step 1: (1,1) to (1,2), Step 2: (1,2) to (2,2), Step 3: (2,2) to (2,1), Step 4: (2,1) to (1,1). Total 4 moves. |
| **Q11** | **c** | Random spamming se multiple collisions lagti hain jisse overall game score ruin ho jata hai. Safe retracing best hai. |
| **Q12** | **b** | Matrix dimensions: $4 \times 4 = 16$ total grid cells. |
| **Q13** | **b** | Leg 1: $(1,1) \to (3,1)$ (2 steps) + $(3,1) \to (3,3)$ (2 steps) = 4 steps. Leg 2: $(3,3) \to (1,3)$ (2 steps). Total = 6 steps. |
| **Q14** | **b** | False. Game strict cardinal grid control (Up, Down, Left, Right) pe locked rehta hai. |
| **Q15** | **b** | Test engine candidate ka visuospatial scratchpad aur rapid motor planning metrics measure karta hai. |

---

## 7. Verified Practice Tools & Video Resources

Aap in links pe click karke direct live simulation practice aur walkthrough dekh sakte hain:

### Live Interactive Practice
- **[BuildUForward Accenture Memory Maze Practice Simulator](https://www.builduforward.com/accenture-gamified-assessment/memory-maze)**  
  *Browser me bina login live grids practice karo. Isme actual assessment ke timers, 3-second preview aur score counters shamil hain.*
- **[JustNK Accenture Gaming Round Detailed Breakdown](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html)**  
  *Sare mini-games ka sequencing, sectional timing, aur cutoff analysis.*

### Video Walkthroughs
- **[OnlineStudy4u: Accenture Door & Maze Problems Explained](https://www.youtube.com/watch?v=ll1srQueVrQ)**  
  *Pratik Sir ka 16-minute step-by-step video walkthrough jisme blind reset maze, obstacle collisions aur reset mapping sikhayi gayi hai.*
- **[Accenture Cognitive Assessment Full Gameplay Walkthrough](https://www.youtube.com/watch?v=tsW_BL8hSBY)**  
  *Real gameplay footage jisme visual chunks aur keyboard speed tricks demo kiye gaye hain.*

---

## 8. Test-Day Golden Checklist

```
[ ] Rule 1: Screen aate hi Variant check karo.
            - Walls dikhi (Variant A) -> 3 Anchors (Start, Key, Door) lock karo aur Vector code banao.
            - Walls nahi dikhi (Variant B) -> Direct Manhattan route probe karo, reset hote hi wall map karo.
[ ] Rule 2: Vector code hamesha 2 parts me bolna: [Path to Key] -> [Path to Door].
[ ] Rule 3: Speed se zyada Accuracy matter karti hai; blind button spamming bilkul mat karna!
[ ] Rule 4: Key collect kiye bina door pe kabhi mat jana.
```
