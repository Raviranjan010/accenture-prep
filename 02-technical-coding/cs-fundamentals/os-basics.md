# Core CS Fundamentals: Operating Systems Basics

## 1. Process vs. Thread

| Feature | Process | Thread |
| :--- | :--- | :--- |
| **Definition** | An independent executing program in memory. | A lightweight execution unit within a process. |
| **Memory** | Has separate address space (heap, stack, data). | Shares address space and heap with parent process. |
| **Context Switch** | Slower (requires saving CPU registers & memory maps). | Faster (only requires saving thread CPU registers & stack). |
| **Isolation** | High (one process crash does not affect others). | Low (one thread crash can take down entire process). |

---

## 2. CPU Scheduling Algorithms

- **First-Come, First-Served (FCFS)**: Non-preemptive, suffers from Convoy Effect (short processes waiting behind long ones).
- **Shortest Job First (SJF)**: Optimal theoretical waiting time; can cause starvation for long processes.
- **Round Robin (RR)**: Preemptive, allocates fixed time quantum ($q$) to each process in FIFO queue.
- **Priority Scheduling**: Preemptive/non-preemptive based on assigned process priority.

---

## 3. Deadlocks & 4 Necessary Conditions

A deadlock occurs when processes are blocked forever waiting for resources held by each other. All 4 conditions MUST hold simultaneously:

1. **Mutual Exclusion**: At least one resource is held in a non-shareable mode.
2. **Hold and Wait**: Process holding a resource is waiting to acquire additional resources held by others.
3. **No Preemption**: Resources cannot be forcibly taken from a process holding them.
4. **Circular Wait**: A closed chain of processes exists ($P_0 ightarrow P_1 ightarrow P_2 ightarrow P_0$).

*Handling Deadlocks*: Banker's Algorithm (Deadlock Avoidance), Resource Allocation Graphs.

---

## 4. Virtual Memory & Paging

- **Paging**: Memory management scheme storing process data in fixed-size blocks called **Pages**, mapped to physical RAM blocks called **Frames** via a **Page Table**.
- **Virtual Memory**: Allows execution of processes larger than physical RAM by swapping pages between RAM and disk storage (Page Faults handled via LRU/FIFO page replacement).
