# Gamified Assessment: Memory Maze

## What this is
Memory Maze is a spatial memory and rapid navigation mini-game featured in the Accenture 2026 Gamified Assessment (powered by platforms like Aon/Cut-e or SHL). You are briefly shown a grid containing obstacles/walls, a starting position, a target key, and an exit door. After a few seconds, the grid contents disappear or turn dark, and you must navigate step-by-step from Start → Key → Door entirely from memory without hitting invisible walls.

---

## Formula / Rule / Pattern

```
[Start Cell] ──(Path A)──> [Key Cell] ──(Path B)──> [Door Cell]
```

- **Grid Dimensions**: Typically 4x4, 5x5, or 6x6.
- **Time Pressure**: Memorization window = 3 to 5 seconds per maze; Navigation window = 10 to 15 seconds.
- **Scoring**: Higher accuracy (zero collisions) + faster completion time = higher cognitive score.
- **Key Constraint**: You CANNOT proceed to the Exit Door before collecting the Key first.

---

## Shortcut: The 3-Anchor Chunking Technique

> [!TIP]
> ### The 3-Anchor Chunking Trick
> Don't try to memorize the entire grid or every wall tile. Lock onto **three reference points only**—the **Start coordinate**, the **Key coordinate**, and the **Door coordinate**—and pre-calculate the directional vector sequence (e.g. "2 Right, 1 Up to Key; 2 Up, 1 Left to Door") during the 3-second preview window.
> 
> *Why it works*: Human short-term working memory can hold only 3 to 4 independent items ("chunks") reliably under high time pressure. Attempting to visually memorize an entire 5x5 matrix of 25 cells causes cognitive overload, whereas memorizing a 2-segment directional vector (e.g. `RRU → UUL`) uses only 2 memory chunks.

---

## Worked Examples & Practice Scenarios

### Scenario 1 (Easy 3x3 Grid)
- **Grid Setup**: Start at (1,1) [bottom-left]. Key at (1,3) [top-left]. Door at (3,3) [top-right]. Wall at (2,3).
- **Preview Phase**:
  - Start (1,1) to Key (1,3): Straight UP 2 steps (1,1 → 1,2 → 1,3).
  - Key (1,3) to Door (3,3): Wall at (2,3), so step DOWN to (1,2), RIGHT 2 steps to (3,2), UP 1 step to (3,3).
- **Vector Code**: `U, U` (Key) $\rightarrow$ `D, R, R, U` (Door).
- **Navigation Execution**: 6 directional button clicks executed seamlessly.

### Scenario 2 (Medium 4x4 Grid with Obstacles)
- **Grid Setup**: Start at (1,1). Key at (3,3). Door at (4,1). Walls at (2,2), (3,2).
- **Preview Phase**:
  - Path to Key: Go RIGHT 2 steps to (3,1), UP 2 steps to (3,3). (Avoids wall at 3,2? Wait, (3,1) to (3,3) passes through (3,2)! Must bypass: (1,1) $\rightarrow$ (1,3) $\rightarrow$ (3,3)).
  - Let's trace: (1,1) $\rightarrow$ UP 2 to (1,3) $\rightarrow$ RIGHT 2 to (3,3) [Key collected!].
  - Path from Key (3,3) to Door (4,1): Wall at (3,2). Step RIGHT to (4,3) $\rightarrow$ DOWN 2 to (4,1) [Door!].
- **Vector Code**: `U, U, R, R` (Key) $\rightarrow$ `R, D, D` (Door).

### Scenario 3 (Hard 5x5 Grid with Multiple Dead Ends)
- **Grid Setup**: Start at (2,1). Key at (5,5). Door at (1,5).
- **Preview Phase**:
  - Center wall block at (3,3).
  - Path to Key: `R, R, R, U, U, U, U` $\implies$ (5,1) to (5,5).
  - Path to Door: `L, L, L, L` $\implies$ (5,5) to (1,5).
- **Vector Code**: `R3, U4` (Key) $\rightarrow$ `L4` (Door).

---

## Practice Scenarios & PYQ Bank

Q1. In a 4x4 grid, Start is at (1,1), Key is at (1,4), Door is at (4,4). A wall blocks (1,3). What is the shortest safe sequence to reach the Key?  
a) UP, UP, UP  
b) RIGHT, UP, UP, LEFT, UP  
c) UP, RIGHT, UP, LEFT, UP  
d) RIGHT, RIGHT, UP, UP  

Q2. What is the primary cause of score penalties in Memory Maze?  
a) Taking more than 2 seconds to memorize  
b) Colliding with an unmemorized wall boundary  
c) Reaching the door before collecting the key  
d) Both b and c  

Q3. In a 3x3 grid, Start=(2,1), Key=(2,3), Door=(3,1). Wall at (2,2). Which path reaches the Key safely?  
a) (2,1) $\rightarrow$ (2,2) $\rightarrow$ (2,3)  
b) (2,1) $\rightarrow$ (1,1) $\rightarrow$ (1,3) $\rightarrow$ (2,3)  
c) (2,1) $\rightarrow$ (3,1) $\rightarrow$ (3,3) $\rightarrow$ (2,3)  
d) Both b and c are valid paths  

Q4. What is the optimal number of memory chunks to hold in working memory for a 4x4 maze?  
a) 16 individual grid cell states  
b) 2 directional vector sequences (Start $\rightarrow$ Key, Key $\rightarrow$ Door)  
c) 8 wall coordinates  
d) Every tile's color  

Q5. In a 4x4 maze, Start=(1,2), Key=(4,2), Door=(4,4). No internal walls exist. What is the minimum total steps required?  
a) 3 steps  
b) 5 steps  
c) 7 steps  
d) 4 steps  

Q6. If you collide with a wall during navigation, what usually happens in the assessment?  
a) Assessment terminates immediately  
b) The grid flickers briefly and resets your position to the last valid step with a time penalty  
c) Your total score increases  
d) You skip to the next game  

Q7. In a 5x5 grid, Start=(1,1), Key=(1,5), Door=(5,5). Walls exist at (1,2), (1,3), (1,4). How must you navigate to the Key?  
a) Move RIGHT to (2,1), UP 4 steps to (2,5), then LEFT 1 step to (1,5)  
b) Move straight UP through the walls  
c) Move to Door first  
d) Impossible to solve  

Q8. Why is backward planning (Door $\rightarrow$ Key $\rightarrow$ Start) sometimes useful during the 3-second preview?  
a) The door is always bigger  
b) The exit door area often has fewer path choices, making constraint identification faster  
c) It resets the timer  
d) It changes wall locations  

Q9. In a 4x4 grid, Key is at (3,3) and Door is at (3,3). How many steps are needed between collecting the key and exiting?  
a) 1 step  
b) 0 steps (instant completion upon reaching cell)  
c) 4 steps  
d) 2 steps  

Q10. Start=(1,1), Key=(2,2), Door=(1,1). Path: (1,1)$\rightarrow$(1,2)$\rightarrow$(2,2) [Key] $\rightarrow$(2,1)$\rightarrow$(1,1) [Door]. How many total moves were made?  
a) 2  
b) 3  
c) 4  
d) 5  

Q11. What is the recommended strategy if you completely forget the path halfway through?  
a) Panic-click random arrow keys  
b) Freeze and let the time run out  
c) Safely backtrack along the path you already know or systematically probe adjacent open cells  
d) Refresh the browser window  

Q12. In a 4x4 grid, how many total grid cells exist?  
a) 12  
b) 16  
c) 20  
d) 25  

Q13. In a 3x3 grid, Start=(1,1), Key=(3,3), Door=(1,3). Path to Key: (1,1)$\rightarrow$(3,1)$\rightarrow$(3,3). Path to Door: (3,3)$\rightarrow$(1,3). What is total step distance?  
a) 4 steps  
b) 6 steps  
c) 8 steps  
d) 5 steps  

Q14. True or False: You can collect the Key and reach the Door in diagonal moves in Memory Maze.  
a) True (diagonal moves are allowed)  
b) False (navigation is strictly cardinal: Up, Down, Left, Right)  

Q15. Which cognitive skill does Memory Maze primarily test?  
a) Verbal vocabulary  
b) Spatial working memory and executive planning  
c) Coding syntax  
d) Financial math  

---

## Answers

1. **b) RIGHT, UP, UP, LEFT, UP** — Bypasses wall at (1,3) via column 2.
2. **d) Both b and c** — Collisions and incorrect sequence order penalty your score.
3. **d) Both b and c are valid paths** — Left bypass and Right bypass are both obstacle-free.
4. **b) 2 directional vector sequences** — Minimizes cognitive load.
5. **b) 5 steps** — (1,2)$\rightarrow$(4,2) is 3 steps right; (4,2)$\rightarrow$(4,4) is 2 steps up. Total = 5 steps.
6. **b) The grid flickers briefly and resets your position...** — Standard game mechanism.
7. **a) Move RIGHT to (2,1), UP 4 steps to (2,5), then LEFT 1 step to (1,5)** — Detours around blocked column 1.
8. **b) The exit door area often has fewer path choices...** — Prunes choices faster.
9. **b) 0 steps** — Key and Door on the same cell complete upon arrival.
10. **c) 4 moves** — (1,1)$\rightarrow$(1,2) [1], (1,2)$\rightarrow$(2,2) [2], (2,2)$\rightarrow$(2,1) [3], (2,1)$\rightarrow$(1,1) [4].
11. **c) Safely backtrack along the path...** — Minimizes collision penalties.
12. **b) 16** — $4 \times 4 = 16$.
13. **b) 6 steps** — 2 steps right + 2 steps up + 2 steps left = 6 steps total.
14. **b) False** — Standard movement is strictly cardinal 4-way grid movement.
15. **b) Spatial working memory and executive planning** — Official assessment metric.

---

## Where this appears in the real Accenture test
Appears in Stage 1: Gamified Assessment (Mini-game 1 of 3/4).

---

## Recommended videos
- [BuildUForward Accenture Memory Maze Interactive Practice Tool](https://www.builduforward.com/accenture-gamified-assessment/memory-maze) — Practice live memory maze grids in browser with no login.
- [Accenture Gaming Cognitive Assessment Detailed Explanation Video](https://www.youtube.com/watch?v=tsW_BL8hSBY) — Video walkthrough of Memory Maze gameplay and visual tricks.
- [JustNK Gaming Round Breakdown Article](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html) — Game mechanics breakdown and tips.
