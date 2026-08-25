# Core CS Fundamentals: Operating Systems Basics

## 1. What is it?
An **Operating System (OS)** is master system software that manages computer hardware resources (CPU, RAM, Disk, Input/Output devices) and provides common services for user applications.

### Beginner Vocabulary Glossary
Before looking at OS algorithms, let's define fundamental terms in plain language:
- **Hardware**: The physical electronic components of a computer (CPU chips, RAM sticks, hard drives).
- **CPU (Central Processing Unit)**: The "brain" of the computer that executes software instructions.
- **RAM (Random Access Memory)**: Fast, temporary memory used to hold active programs currently running. When computer turns off, RAM clears completely (Volatile).
- **Disk / Storage (Hard Drive / SSD)**: Permanent, slower storage holding your files and installed programs (Non-volatile).
- **Process**: A program in execution loaded into RAM memory (e.g., launching Google Chrome).
- **Thread**: A lightweight segment or unit of execution *within* a process (e.g., one tab playing audio inside Chrome).
- **Context Switch**: The process of the CPU saving the state of one process/thread and loading the state of another.

---

## 2. Why does it matter?
1. **Accenture Assessment Core**: Process management, CPU scheduling calculations, deadlocks, and virtual memory are standard MCQ topics.
2. **System Stability**: Prevents one buggy application from crashing your entire computer or monopolizing all RAM.
3. **Application Performance**: Helps developers write efficient multi-threaded code that maximizes multi-core CPU hardware.

---

## 3. When to use it?
- **Understand OS Scheduling when**: Designing high-throughput web servers or background job processors.
- **Understand Multithreading when**: Building responsive applications where UI rendering must not freeze while performing background network calls.

---

## 4. How it works
1. **Program to Process**: When you double-click an application icon, the OS loads executable code from Disk into RAM memory.
2. **Process Control Block (PCB)**: The OS creates a PCB tracking Process ID (PID), memory limits, program counter, and open files.
3. **Process Life Cycle**:
   - **New**: Process being created.
   - **Ready**: Loaded into RAM waiting for CPU time.
   - **Running**: Instructions being executed by the CPU.
   - **Waiting (Blocked)**: Waiting for an Event or I/O operation (e.g., reading disk file).
   - **Terminated**: Finished execution; OS reclaims memory.

---

## 5. Key rules or syntax

### Process Control Block (PCB) Structure
```
+------------------------------------+
| Process ID (PID: 4082)             |
| Process State (RUNNING / READY)    |
| Program Counter (Next Instruction) |
| CPU Registers & Stack Pointer      |
| Memory Management (Page Tables)    |
| Open File Descriptors              |
+------------------------------------+
```
*Why PCB works*: When CPU switches between applications 1,000 times per second, the PCB acts as a exact snapshot so a process can resume execution without losing progress.

---

## 6. Simple example

### Level 1 (Easy): Opening a Browser vs. Multiple Tabs
- **Process**: Launching Chrome creates a **Process** with its own allocated RAM space.
- **Threads**: Opening 3 tabs creates 3 separate **Threads** inside that process—tab 1 streams audio, tab 2 renders HTML, tab 3 downloads a PDF concurrently.

---

## 7. Detailed example

### Part A: Process vs. Thread Comparison

| Feature | Process | Thread |
| :--- | :--- | :--- |
| **Memory Allocation** | Dedicated separate address space (Heap, Stack, Data). | Shares Heap and Data with parent process; has own Stack. |
| **Context Switching** | Slow (requires changing memory pages & virtual address space). | Fast (only saves registers and stack pointer). |
| **Communication** | Inter-Process Communication (IPC: Sockets, Pipes). | Shared memory access directly. |
| **Crash Impact** | Isolated (one process crash doesn't crash others). | Vulnerable (one thread crash can crash entire process). |

- **Simple Beginner Example**: Separate houses (Processes) vs. Rooms inside a single house (Threads).
- **Realistic Enterprise Example**: Node.js running single-threaded event loop vs. Java Spring Boot application utilizing thread pools to handle 1,000 concurrent HTTP client connections.

---

### Part B: CPU Scheduling Algorithms

CPU Scheduling determines which process in the Ready Queue receives CPU execution time.

#### 1. First-Come, First-Served (FCFS)
- **Concept**: Non-preemptive. Processes executed in arrival order.
- **Problem**: Suffers from the **Convoy Effect** (short processes wait behind a massive 100-second job).

#### 2. Shortest Job First (SJF)
- **Concept**: Selects process with shortest CPU burst time. Proven optimal minimum average waiting time.
- **Problem**: Can cause **Starvation** for long processes if short processes keep arriving.

#### 3. Round Robin (RR)
- **Concept**: Preemptive. Assigns a fixed time slice (**Time Quantum $q$**) to each process in round-robin sequence.
- **Realistic Calculation Example**:
  - Processes: $P_1 (Burst=10ms), P_2 (Burst=4ms), P_3 (Burst=2ms)$. Time Quantum $q = 3ms$.
  - Execution Sequence: $P_1 (3ms) ightarrow P_2 (3ms) ightarrow P_3 (2ms) ightarrow P_1 (3ms) ightarrow P_2 (1ms) ightarrow P_1 (4ms)$.

#### 4. Priority Scheduling
- **Concept**: CPU allocated to highest priority process (preemptive or non-preemptive). Mitigated using **Aging** (gradually increasing priority of long-waiting processes).

---

### Part C: Deadlocks & The 4 Necessary Conditions

A **Deadlock** is a situation where two or more processes are blocked forever, each holding a resource the other needs.

- **The 4 Necessary Conditions (Must ALL hold simultaneously)**:
  1. **Mutual Exclusion**: At least one resource is held in a non-shareable mode (only 1 process at a time).
  2. **Hold and Wait**: Process holds a resource while waiting to acquire another resource held by someone else.
  3. **No Preemption**: Resources cannot be forcibly taken away; must be released voluntarily.
  4. **Circular Wait**: Closed loop chain ($P_0$ waits for $P_1$, $P_1$ waits for $P_2$, $P_2$ waits for $P_0$).

- **Deadlock Handling**:
  - *Avoidance*: **Banker's Algorithm** (checks if allocating resources leaves system in a Safe State).

---

### Part D: Virtual Memory & Paging
- **Paging**: Physical RAM is divided into fixed-size blocks called **Frames**, and Virtual Memory is divided into same-sized blocks called **Pages**.
- **Page Table**: Maps Virtual Page numbers to physical RAM Frame numbers.
- **Page Fault**: Occurs when a process accesses a page not currently loaded in physical RAM, forcing the OS to fetch it from Disk.
- **LRU Page Replacement**: Least Recently Used algorithm evicts the page that hasn't been accessed for the longest time.

---

## 8. Practical use case
**Web Server Architecture**:
A web server handling 10,000 requests per second:
1. Uses a **Thread Pool** (Threads) instead of spawning 10,000 separate Processes, reducing memory overhead by 90%.
2. Uses **Virtual Memory** so the server can run large applications without purchasing expensive physical RAM sticks.
3. Uses **Round Robin CPU Scheduling** to keep customer API response times balanced.

---

## 9. Common mistakes

### Concept 1: Process vs Thread Mistakes
- *Mistake*: Assuming threads have separate heaps.
- *Why it happens*: Threads have separate *stacks* (local function variables), but share the *same heap* (global/instantiated object memory).

### Concept 2: Scheduling Mistakes
- *Mistake*: Setting Round Robin Time Quantum $q$ too small.
- *Why it happens*: If $q = 0.001ms$, CPU spends 90% of its time performing **context switching overhead** rather than actual work!

### Concept 3: Deadlock Condition Mistakes
- *Mistake*: Thinking a deadlock can happen if only 3 of the 4 deadlock conditions are present.
- *Why it happens*: ALL 4 conditions MUST hold simultaneously. Breaking even ONE condition (e.g., eliminating Circular Wait) completely prevents deadlocks!

---

## 10. Tips & tricks

### Shortcut 1: The Deadlock 4-Condition Mnemonic
- **Mnemonic**: **M-H-N-C** ("Many Hungry Neighbors Crying")
  - **M**utual Exclusion
  - **H**old and Wait
  - **N**o Preemption
  - **C**ircular Wait

### Shortcut 2: Round Robin Time Quantum Goldilocks Rule
- **Rule**:
  - $q$ too large $ightarrow$ Degenerates into FCFS.
  - $q$ too small $ightarrow$ Context switch overhead destroys performance.
  - *Ideal*: $q$ should be larger than 80% of CPU burst times.

### Shortcut 3: Process vs Thread Memory Shortcut
- **Rule**:
  - **Separate**: Memory (Processes), PCB, Address Space.
  - **Shared**: Heap (Threads), Global Variables, Open Files.

---

## 11. Practice exercises

1. **(Easy - Recall)** What is the difference between volatile RAM and non-volatile Hard Disk storage?
2. **(Easy - Recall)** Which OS component tracks a process's PID, state, and program counter?
3. **(Easy - Concept)** Is Context Switching faster between two processes or two threads of the same process?
4. **(Medium - Why)** Why does Shortest Job First (SJF) scheduling guarantee minimum average waiting time?
5. **(Medium - Scenario)** What happens when a Page Fault occurs during application execution?
6. **(Medium - Applied)** Calculate the Average Waiting Time under FCFS for 3 processes arriving at time 0:
   - $P_1 = 24ms, P_2 = 3ms, P_3 = 3ms$.
7. **(Medium - Scenario)** Name the 4 necessary conditions required for a Deadlock to exist.
8. **(Hard - Applied)** How does the **Aging** technique solve the Starvation problem in Priority CPU Scheduling?
9. **(Hard - Scenario)** A process attempts to write to a variable shared across 4 threads without synchronization. What issue occurs?
10. **(Hard - Architecture)** Explain how Banker's Algorithm determines if a state is "Safe" or "Unsafe".

---

## 12. Q&A with explanations

1. **Answer**: **RAM** is fast, temporary storage cleared on reboot (volatile). **Hard Disk** is slower, permanent storage (non-volatile).
2. **Answer**: **Process Control Block (PCB)**.
3. **Answer**: **Two threads of the same process** (since they share memory space and page tables, avoiding virtual memory remap overhead).
4. **Answer**: SJF moves shorter tasks to the front, minimizing the cumulative delay experienced by subsequent tasks.
5. **Answer**: The CPU pauses execution $ightarrow$ generates hardware interrupt $ightarrow$ OS fetches required page from Disk into RAM $ightarrow$ updates Page Table $ightarrow$ resumes process execution.
6. **Answer**:
   - $P_1$ waiting time = 0ms.
   - $P_2$ waiting time = 24ms.
   - $P_3$ waiting time = $24 + 3 = 27ms$.
   - Average Waiting Time $= (0 + 24 + 27) / 3 = 51 / 3 =$ **17 ms**.
7. **Answer**: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait.
8. **Answer**: Aging gradually increases the priority of processes that wait in the ready queue for a long time, ensuring even low-priority jobs eventually run.
9. **Answer**: A **Race Condition** (data corruption caused by non-atomic simultaneous writes). Fixed using Mutex / Semaphores.
10. **Answer**: Banker's Algorithm simulates resource allocation to find if there exists at least one valid execution order where EVERY process can obtain its maximum declared resources and finish without deadlocking.

---

## 13. Quick revision

> [!TIP]
> ### 🚀 Operating Systems Cheat-Sheet
> - **Process**: Independent, isolated memory space.
> - **Thread**: Lightweight, shares heap memory with parent process.
> - **FCFS**: Simple, subject to Convoy Effect.
> - **SJF**: Optimal average waiting time, risk of Starvation.
> - **Round Robin**: Preemptive, uses fixed Time Quantum $q$.
> - **Deadlock 4 Conditions**: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait.
> - **Virtual Memory / Paging**: Fixed-size Pages mapped to physical Frames via Page Table.

---

## 14. Connection to next topic
Now that you understand how Operating Systems manage local hardware, processes, and RAM memory, let's explore how computers communicate across global networks! Continue to **[networking-basics.md](networking-basics.md)**.
