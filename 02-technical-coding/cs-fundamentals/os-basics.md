# CS Fundamentals: Operating Systems (OS)

## What this is
An Operating System (OS) acts as the system software interface managing computer hardware, CPU scheduling, process synchronization, memory allocation, virtual memory paging, and file system storage.

---

## Formula / Rule / Pattern

| OS Concept | Mechanism / Formula | Key Characteristics |
| :--- | :--- | :--- |
| **Process vs Thread** | Process = Independent execution space; Thread = Lightweight sub-unit sharing process memory | Threads share heap/globals, have private stacks |
| **CPU Scheduling** | Turnaround Time $= T_{\text{Completion}} - T_{\text{Arrival}}$ | Waiting Time $= T_{\text{Turnaround}} - T_{\text{Burst}}$ |
| **Deadlock Conditions** | Coffman 4 Conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait | All 4 must hold simultaneously for deadlock |
| **Virtual Memory** | Page Table translation: Logical Address $\rightarrow$ Physical Address | Handled via Memory Management Unit (MMU) & TLB |

---

## Shortcut: The Coffman Deadlock 4-Condition Checklist

> [!TIP]
> ### Deadlock Prevention Checklist
> To break a deadlock, break at least **one** of the 4 Coffman conditions:
> 
> 1. **Mutual Exclusion**: Allow shared read access (e.g. read-only files).
> 2. **Hold & Wait**: Require processes to request ALL needed resources at start.
> 3. **No Preemption**: Forcibly take away resources from waiting processes.
> 4. **Circular Wait**: Impose total ordering on all resource requests ($R_1 < R_2 < R_3$).
> 
> *Why it works*: Deadlock requires all 4 conditions simultaneously. Eliminating 1 condition mathematically guarantees deadlock immunity.

---

## Worked Examples

### Example 1: CPU Scheduling Calculation (Easy)
- **Processes**:
  - P1: Arrival $= 0$, Burst Time $= 5$
  - P2: Arrival $= 1$, Burst Time $= 3$
- **FCFS Scheduling**:
  1. P1 runs from $t=0$ to $t=5$. Completion $= 5$. Turnaround $= 5 - 0 = 5$. Waiting $= 5 - 5 = 0$.
  2. P2 runs from $t=5$ to $t=8$. Completion $= 8$. Turnaround $= 8 - 1 = 7$. Waiting $= 7 - 3 = 4$.
  3. **Average Waiting Time**: $(0 + 4)/2 = 2$ units.

### Example 2: Page Fault Calculation (Medium)
- **Reference String**: `1, 2, 3, 4, 1, 2`. Frame Capacity $= 3$ (FIFO replacement).
- **Step-by-step Execution**:
  1. Access 1: `[1, _, _]` (Fault 1)
  2. Access 2: `[1, 2, _]` (Fault 2)
  3. Access 3: `[1, 2, 3]` (Fault 3)
  4. Access 4: Replace 1 $\implies `[4, 2, 3]`$ (Fault 4)
  5. Access 1: Replace 2 $\implies `[4, 1, 3]`$ (Fault 5)
  6. Access 2: Replace 3 $\implies `[4, 1, 2]`$ (Fault 6)
  7. **Total Page Faults**: 6.

---

## Practice Questions (PYQ Bank)

Q1. What is the primary difference between a process and a thread?  
a) Threads have separate memory address spaces  
b) Threads of the same process share code, data, and OS resources, but maintain private stack and registers  
c) Processes run faster  
d) Threads do not use CPU  

Q2. Which CPU scheduling algorithm can lead to the "Convoy Effect"?  
a) Round Robin  
b) First-Come, First-Served (FCFS)  
c) Shortest Remaining Time First (SRTF)  
d) Priority Scheduling  

Q3. What is Thrashing in virtual memory management?  
a) Disk fragmentation  
b) Excessive page swapping activity spending more time swapping pages than executing instructions  
c) CPU overheating  
d) Memory leak  

Q4. Which algorithm is used for Deadlock Avoidance in operating systems?  
a) Round Robin  
b) Banker's Algorithm  
c) LRU Algorithm  
d) Elevator Algorithm  

Q5. What is a Semaphore?  
a) A hardware cable  
b) An integer variable used for signaling and process synchronization to solve critical section problems  
c) A file type  
d) A memory bus  

Q6. What is Belady's Anomaly?  
a) Page faults increase when adding more memory page frames (observed in FIFO replacement)  
b) CPU speed drops  
c) Deadlock occurs  
d) Stack overflows  

Q7. In Round Robin scheduling, what happens if the time quantum is extremely large?  
a) Behaves like FCFS  
b) Behaves like SJF  
c) Causes deadlock  
d) System crashes  

Q8. What is the Critical Section in concurrent programming?  
a) Code segment accessing shared resources that must not be concurrently accessed by multiple threads  
b) Emergency boot code  
c) Main function  
d) Exception handler  

Q9. What hardware component speeds up virtual to physical address translation in virtual memory?  
a) ALU  
b) Translation Lookaside Buffer (TLB)  
c) L3 Cache  
d) ROM  

Q10. What state transition occurs when a process in the Running state is interrupted by the CPU scheduler timer?  
a) Running $\rightarrow$ Waiting  
b) Running $\rightarrow$ Ready  
c) Running $\rightarrow$ Terminated  
d) Ready $\rightarrow$ Running  

Q11. What is internal fragmentation?  
a) Unused allocated memory within a fixed-size page/partition block  
b) Free memory between partitions  
c) Disk bad sectors  
d) Network loss  

Q12. How many Coffman conditions must hold simultaneously for a deadlock to occur?  
a) 1  
b) 2  
c) 3  
d) 4  

Q13. What is a Mutex?  
a) A binary locking mechanism providing mutual exclusion for shared resource access  
b) A thread pool  
c) A system call  
d) A process state  

Q14. In virtual memory, what is a Page Fault?  
a) An interrupt generated when a program accesses a page not currently loaded in physical RAM  
b) A hardware failure  
c) A corrupted file  
d) Segmentation fault  

Q15. Why does LRU (Least Recently Used) page replacement avoid Belady's Anomaly?  
a) LRU belongs to the class of stack-based page replacement algorithms  
b) LRU uses disk  
c) LRU ignores frames  
d) LRU runs in hardware  

---

## Answers

1. **b) Threads share code, data, and OS resources...** — Definition of thread vs process.
2. **b) First-Come, First-Served (FCFS)** — Short processes get stuck behind long process (Convoy effect).
3. **b) Excessive page swapping activity...** — Definition of thrashing.
4. **b) Banker's Algorithm** — Dijkstra's safe-state deadlock avoidance algorithm.
5. **b) An integer variable used for signaling and synchronization...** — Definition of semaphore.
6. **a) Page faults increase when adding more memory page frames...** — Definition of Belady's anomaly in FIFO.
7. **a) Behaves like FCFS** — Large quantum eliminates preemptive context switches.
8. **a) Code segment accessing shared resources...** — Definition of critical section.
9. **b) Translation Lookaside Buffer (TLB)** — MMU associative cache for address translation.
10. **b) Running $\rightarrow$ Ready** — Preempted process returns to ready queue.
11. **a) Unused allocated memory within a fixed block** — Definition of internal fragmentation.
12. **d) 4** — All 4 Coffman conditions required.
13. **a) A binary locking mechanism providing mutual exclusion...** — Definition of mutex.
14. **a) An interrupt generated when a program accesses a page not in RAM** — Page fault mechanism.
15. **a) LRU belongs to the class of stack-based algorithms** — Mathematical property of stack algorithms.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Core CS Fundamentals Technical MCQ section.

---

## Recommended videos
- [Accenture Technical Assessment Prep Video](https://www.youtube.com/watch?v=DwZZNJxBAn0) — OS questions.
- [Mock Technical Assessment Walkthrough](https://www.youtube.com/watch?v=JM2Uc9KJ-Ys) — OS & process management review.
