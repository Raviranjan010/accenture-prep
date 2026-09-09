# Gamified Assessment: Path Finder

## What this is
Path Finder (also known as Tile Rotation or Grid Connector) is a spatial logic mini-game in the Accenture 2026 Gamified Assessment. You are presented with a grid (3x3, 4x4, or 5x5) filled with tile segments (straight lines, T-junctions, elbow bends, cross intersections). Your goal is to rotate individual tiles to form a continuous, unbroken path connecting the Start node (Entry) to the End node (Exit) before the timer expires.

---

## Formula / Rule / Pattern

| Tile Type | Degree Rotations | Number of Unique Orientations | Connection Paths Provided |
| :--- | :--- | :--- | :--- |
| **Straight Line** | 90° increments | 2 (Horizontal, Vertical) | Connects opposite sides |
| **Elbow Bend (L-Tile)** | 90° increments | 4 (Top-Right, Right-Bottom, Bottom-Left, Left-Top) | Connects adjacent sides |
| **T-Junction** | 90° increments | 4 (3 sides connected, 1 dead end) | Connects 3 directions |
| **Cross (+ Tile)** | Fixed | 1 (Symmetric) | Connects all 4 directions |

---

## Shortcut: The Backward End-Search Technique

> [!TIP]
> ### Backward End-Search Trick
> Start solving the tile path **from the End tile backward** to the Start tile, rather than starting at the Start tile.
> 
> *Why it works*: Start tiles often connect to multiple adjacent movable tiles with many rotation options, creating a wide branching tree of possibilities. End tiles are usually located in corners or constrained edges with only **one** valid incoming tile orientation. Searching backward prunes 70–80% of invalid rotation paths immediately.

---

## Worked Examples & Practice Scenarios

### Scenario 1 (Easy 3x3 Grid Connection)
- **Grid Setup**: Start at Top-Left (1,1) facing East. End at Top-Right (1,3) facing West. Tile at (1,2) is an L-tile currently facing South-East.
- **Solving Steps**:
  1. Look at End (1,3): Needs incoming connection from West (1,2).
  2. Look at Start (1,1): Emits connection to East (1,2).
  3. Intermediate tile (1,2): Must connect West AND East (Straight horizontal path).
  4. Action: Rotate (1,2) L-tile until it forms horizontal line or replace/orient straight connection $\implies$ Path complete in 1 rotation.

### Scenario 2 (Medium 4x4 Grid with Obstacles)
- **Grid Setup**: Start at (1,1) [Top-Left], End at (4,4) [Bottom-Right].
- **Corner Constraint**: Tile at (4,4) is an L-tile. Since it is at the bottom-right corner, its ONLY valid orientation is UP and LEFT.
- **Backward Step**: Connect (4,4) to (4,3) [Left] or (3,4) [Up].
- **Trace**: Tile at (3,4) is blocked/dead tile. Thus, path MUST go through (4,3). Rotate (4,3) to connect to (4,4).

### Scenario 3 (Hard 5x5 Grid with Multiple T-Junctions)
- **Grid Setup**: Start at (2,1), End at (5,3).
- **Strategy**: Identify "Anchor Tiles"—tiles bounded by 2 outer walls that have ONLY ONE possible orientation regardless of the rest of the grid. Rotate all Anchor Tiles first, then connect the middle section.

---

## Practice Scenarios & PYQ Bank

Q1. In Path Finder, why should you identify corner tiles first?  
a) Corner tiles have 4 valid orientations  
b) Corner tiles can only connect in 2 directions (towards the inner grid), making their orientation deterministic  
c) Corner tiles give bonus points  
d) Corner tiles cannot be rotated  

Q2. How many unique visual orientations does a straight line tile have?  
a) 1  
b) 2  
c) 3  
d) 4  

Q3. If an L-bend tile is located at the top-right corner of a grid, which direction CANNOT be part of its path?  
a) Left  
b) Down  
c) Up or Right (outside grid boundary)  
d) Down and Left  

Q4. In a 3x3 grid, Start is at (1,1) pointing Right. Tile (1,2) is a T-junction. To connect (1,1) to (1,3), how should the T-junction be oriented?  
a) Flat side facing Top (connecting Left, Right, Down)  
b) Flat side facing Left (connecting Top, Down, Right)  
c) Flat side facing Right (connecting Top, Down, Left)  
d) Pointing Up only  

Q5. What is the maximum number of clicks required to return an L-tile to its original orientation?  
a) 2 clicks  
b) 3 clicks  
c) 4 clicks  
d) 1 click  

Q6. Start is at (1,1), End is at (3,3). Path goes (1,1) $\rightarrow$ (2,1) $\rightarrow$ (2,2) $\rightarrow$ (3,2) $\rightarrow$ (3,3). How many L-bend tiles are required for this 4-step turn path?  
a) 1  
b) 3  
c) 4  
d) 2  

Q7. If a cross (+) tile is present in the grid, how many rotations does it require to connect adjacent tiles?  
a) 0 rotations (it connects all 4 directions symmetrically)  
b) 1 rotation  
c) 2 rotations  
d) 4 rotations  

Q8. What happens if a path forms a closed loop that does NOT connect to the End node?  
a) You win the game  
b) The puzzle remains unsolved until the path reaches the End node  
c) Time increases  
d) Points double  

Q9. In a 4x4 grid, End is at (4,1) [Bottom-Left]. Which orientation must an L-tile at (4,1) have?  
a) Up and Right  
b) Down and Left  
c) Up and Left  
d) Down and Right  

Q10. Why is the "Backward End-Search" technique effective in Path Finder?  
a) End tiles usually have fewer open connections than Start tiles, rapidly pruning invalid paths  
b) It pauses the timer  
c) It automatically rotates tiles  
d) It changes tile colors  

Q11. In a 3x3 grid, a straight tile is at (2,2). Start is at (2,1) and End is at (2,3). What orientation must (2,2) have?  
a) Vertical  
b) Horizontal  
c) Diagonal  
d) Locked  

Q12. What is the optimal initial move when a new Path Finder level loads?  
a) Randomly rotate every tile once  
b) Scan End and Start tiles to fix corner orientations immediately  
c) Click the middle tile 10 times  
d) Wait for 30 seconds  

Q13. How many connections does a T-junction tile provide?  
a) 2  
b) 3  
c) 4  
d) 1  

Q14. In a 5x5 grid with 12 movable tiles, what is the maximum time you should spend per level on average?  
a) 10–15 seconds  
b) 2 minutes  
c) 5 minutes  
d) 30 milliseconds  

Q15. Which cognitive ability does Path Finder evaluate?  
a) Verbal vocabulary  
b) Spatial rotation, logical deductive reasoning, and pattern synthesis  
c) Audio pitch detection  
d) Typing speed  

---

## Answers

1. **b) Corner tiles can only connect in 2 directions...** — Grid boundaries restrict corner orientations.
2. **b) 2** — Horizontal and Vertical (90° = Vertical, 180° = Horizontal).
3. **c) Up or Right (outside grid boundary)** — Connecting outside boundary results in a dead end.
4. **a) Flat side facing Top (connecting Left, Right, Down)** — Connects Left (Start) and Right (End).
5. **c) 4 clicks** — Each click rotates 90°; $4 \times 90^\circ = 360^\circ$.
6. **b) 3** — Turns occur at (2,1), (2,2), and (3,2), requiring 3 L-bends.
7. **a) 0 rotations** — Cross tiles are 4-way symmetric.
8. **b) The puzzle remains unsolved...** — Connection to Exit node is mandatory.
9. **a) Up and Right** — Bottom-left corner can only connect UP into row 3 and RIGHT into col 2.
10. **a) End tiles usually have fewer open connections...** — Reduces search space.
11. **b) Horizontal** — Connects left cell (2,1) to right cell (2,3).
12. **b) Scan End and Start tiles to fix corner orientations immediately** — Fastest anchor strategy.
13. **b) 3** — T-junction has 3 branches.
14. **a) 10–15 seconds** — High-speed performance target for top score band.
15. **b) Spatial rotation, logical deductive reasoning, and pattern synthesis** — Standard assessment metric.

---

## Where this appears in the real Accenture test
Appears in Stage 1: Gamified Assessment (Mini-game 2 of 3/4).

---

## Recommended videos
- [BuildUForward Accenture Path Finder Practice Tool](https://www.builduforward.com/accenture-gamified-assessment) — Free interactive tile-rotation grid practice.
- [Accenture Gaming Cognitive Assessment Detailed Walkthrough Video](https://www.youtube.com/watch?v=tsW_BL8hSBY) — Video showing tile rotation strategies under time pressure.
- [JustNK Accenture Gaming Round Practice Notes](https://www.justnk.in/2025/12/accenture-gaming-round-practice.html) — Game mechanics and tile rotation tips.
