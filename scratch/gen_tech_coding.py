import os

os.makedirs('02-technical-coding/cs-fundamentals', exist_ok=True)
os.makedirs('02-technical-coding/dsa-practice', exist_ok=True)

# 1. 02-technical-coding/README.md
readme_content = """# Technical & Coding Preparation Index

Welcome to **Track 2: Technical & Coding Preparation**. This module covers Core Computer Science fundamentals (OOPs, DBMS, OS, Networking) and Data Structures & Algorithms (DSA) targeted for the Accenture Technical Assessment and Technical Interview.

## Recommended Study Strategy

Allocate a daily study budget of **120 minutes** for this track:
1. **60 Minutes — CS Fundamentals**: Revise 1 CS core subject daily from `cs-fundamentals/`. Focus on definition, core concepts, placement MCQs, and interview follow-up questions.
2. **60 Minutes — DSA Practice**: Solve 2 hands-on coding problems daily from `dsa-practice/`. Implement clean code, state time/space complexity, and log problem attempts in `solved-problems-log.md`.

---

## Folder Structure & Topic Checklist

### Core CS Fundamentals
- [ ] [OOP Concepts](cs-fundamentals/oop-concepts.md) — Encapsulation, Abstraction, Inheritance, Polymorphism, SOLID principles & C++/Java snippets.
- [ ] [DBMS, Normalization & Joins](cs-fundamentals/dbms-normalization-joins.md) — Relational concepts, 1NF to BCNF normalization, INNER/LEFT/RIGHT SQL joins, ACID properties.
- [ ] [OS Basics](cs-fundamentals/os-basics.md) — Process vs Thread, CPU scheduling algorithms, Deadlocks, Paging, Virtual Memory.
- [ ] [Networking Basics](cs-fundamentals/networking-basics.md) — OSI 7-Layer model vs TCP/IP, HTTP vs HTTPS, TCP vs UDP, DNS lookup flow.

### DSA Practice & Problem Logging
- [ ] [Arrays & Strings](dsa-practice/arrays-strings.md) — Two pointers, sliding window, prefix sums, string manipulation patterns & code.
- [ ] [DP & Graphs](dsa-practice/dp-graphs.md) — Dynamic programming (Memoization vs Tabulation, 0/1 Knapsack) & Graph traversals (BFS/DFS).
- [ ] [Solved Problems Log](dsa-practice/solved-problems-log.md) — Ready-to-fill table for tracking solved DSA coding questions.
"""

with open('02-technical-coding/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

# 2. oop-concepts.md
oop_content = """# Core CS Fundamentals: Object-Oriented Programming (OOP)

## 1. The 4 Pillars of OOP

### 1. Encapsulation
- **Definition**: Bundling data (variables) and methods operating on that data inside a single unit (class) while restricting direct access to internal state using access specifiers (`private`, `protected`).
- **Real-World Analogy**: A capsule medicine containing multiple ingredients hidden from the user.
- **Code Example (Java)**:
```java
public class BankAccount {
    private double balance; // Encapsulated data

    public void deposit(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }
    public double getBalance() {
        return this.balance;
    }
}
```

### 2. Abstraction
- **Definition**: Hiding background complex implementation details and displaying only essential functional interfaces to the user.
- **Real-World Analogy**: Driving a car by pressing the accelerator without needing to understand internal engine combustion logic.
- **Code Example (Java)**:
```java
abstract class Vehicle {
    abstract void startEngine(); // Essential interface
}

class Car extends Vehicle {
    void startEngine() {
        System.out.println("Engine started via electronic ignition.");
    }
}
```

### 3. Inheritance
- **Definition**: Mechanism where a child class (subclass) derives properties and behaviors from a parent class (superclass), promoting code reuse.
- **Types**: Single, Multilevel, Hierarchical, Multiple (supported via Interfaces in Java/C++).
- **Code Example (Java)**:
```java
class Animal {
    void eat() { System.out.println("Eating..."); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}
```

### 4. Polymorphism
- **Definition**: Ability of an object or method to take on multiple forms.
- **Compile-Time Polymorphism (Method Overloading)**: Same method name with different parameter signatures resolved at compile time.
- **Run-Time Polymorphism (Method Overriding)**: Child class provides a specific implementation of a method already declared in its parent class, resolved at runtime using virtual tables (vtable).
- **Code Example (Method Overriding)**:
```java
class Shape {
    void draw() { System.out.println("Drawing Shape"); }
}
class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing Circle"); }
}
```

---

## 2. SOLID Principles Overview

1. **Single Responsibility Principle (SRP)**: A class should have one, and only one, reason to change.
2. **Open/Closed Principle (OCP)**: Software entities should be open for extension, but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types without breaking application behavior.
4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules; both should depend on abstractions.

---

## 3. Top Interview Questions & MCQs

1. **What is the difference between Abstract Class and Interface in Java?**
   - *Answer*: Abstract classes can have state (instance variables) and implemented non-abstract methods. Interfaces (prior to Java 8) contain only method signatures (now support default/static methods) and cannot maintain instance state. A class can implement multiple interfaces but extend only one abstract class.
2. **What is Virtual Function in C++?**
   - *Answer*: A function declared in a base class using `virtual` keyword, overridden by derived classes to enable dynamic (runtime) dispatch via `vptr` and `vtable`.
"""

with open('02-technical-coding/cs-fundamentals/oop-concepts.md', 'w', encoding='utf-8') as f:
    f.write(oop_content)

# 3. dbms-normalization-joins.md
dbms_content = """# Core CS Fundamentals: DBMS, Normalization & SQL Joins

## 1. Database Normalization Forms

Normalization reduces data redundancy and prevents insertion, update, and deletion anomalies.

- **1NF (First Normal Form)**:
  - *Rule*: Every column cell must contain atomic (indivisible) values; no repeating groups or arrays.
- **2NF (Second Normal Form)**:
  - *Rule*: Must be in 1NF AND all non-key attributes must be fully functionally dependent on the primary key (eliminates partial dependency).
- **3NF (Third Normal Form)**:
  - *Rule*: Must be in 2NF AND no non-key attribute depends transitively on another non-key attribute (eliminates transitive dependency: $A \rightarrow B$ and $B \rightarrow C$).
- **BCNF (Boyce-Codd Normal Form)**:
  - *Rule*: For every functional dependency $X \rightarrow Y$, $X$ must be a super key.

---

## 2. SQL Joins Explained

Given tables `Students(id, name, dept_id)` and `Departments(dept_id, dept_name)`:

- **INNER JOIN**: Returns records that have matching values in both tables.
  ```sql
  SELECT S.name, D.dept_name 
  FROM Students S 
  INNER JOIN Departments D ON S.dept_id = D.dept_id;
  ```
- **LEFT (OUTER) JOIN**: Returns all records from the left table, and matched records from the right table (NULL if no match).
  ```sql
  SELECT S.name, D.dept_name 
  FROM Students S 
  LEFT JOIN Departments D ON S.dept_id = D.dept_id;
  ```
- **RIGHT (OUTER) JOIN**: Returns all records from the right table, and matched records from the left table.
- **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table.

---

## 3. ACID Properties of Transactions

- **Atomicity**: Transactions complete entirely or fail entirely ("All or Nothing").
- **Consistency**: Database transitions from one valid state to another valid state, preserving all constraints.
- **Isolation**: Concurrent execution of transactions yields the same state as if executed serially (Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable).
- **Durability**: Once a transaction commits, its changes persist permanently even after system crashes.
"""

with open('02-technical-coding/cs-fundamentals/dbms-normalization-joins.md', 'w', encoding='utf-8') as f:
    f.write(dbms_content)

# 4. os-basics.md
os_content = """# Core CS Fundamentals: Operating Systems Basics

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
4. **Circular Wait**: A closed chain of processes exists ($P_0 \rightarrow P_1 \rightarrow P_2 \rightarrow P_0$).

*Handling Deadlocks*: Banker's Algorithm (Deadlock Avoidance), Resource Allocation Graphs.

---

## 4. Virtual Memory & Paging

- **Paging**: Memory management scheme storing process data in fixed-size blocks called **Pages**, mapped to physical RAM blocks called **Frames** via a **Page Table**.
- **Virtual Memory**: Allows execution of processes larger than physical RAM by swapping pages between RAM and disk storage (Page Faults handled via LRU/FIFO page replacement).
"""

with open('02-technical-coding/cs-fundamentals/os-basics.md', 'w', encoding='utf-8') as f:
    f.write(os_content)

# 5. networking-basics.md
networking_content = """# Core CS Fundamentals: Computer Networks Basics

## 1. OSI 7-Layer Model vs. TCP/IP Model

| OSI Layer | Name | Function / Protocol | TCP/IP Layer |
| :--- | :--- | :--- | :--- |
| **7** | Application | HTTP, HTTPS, FTP, DNS, SMTP | Application |
| **6** | Presentation | Encryption, Data formatting (SSL/TLS) | Application |
| **5** | Session | Session establishment & maintenance | Application |
| **4** | Transport | End-to-end connection, reliability (TCP, UDP) | Transport |
| **3** | Network | Routing, IP Addressing (IP, ICMP) | Internet |
| **2** | Data Link | MAC Addressing, framing (Ethernet, Wi-Fi) | Network Access |
| **1** | Physical | Bits transmission over cables/fiber | Network Access |

---

## 2. TCP vs. UDP

- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, guarantees packet order via 3-Way Handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`), error checking, flow control. Used for HTTP/HTTPS, Web, Email.
- **UDP (User Datagram Protocol)**: Connectionless, fast, unreliable, no order guarantee. Used for Video streaming, Gaming, VoIP, DNS queries.

---

## 3. What Happens When You Type a URL in a Browser?

1. **DNS Lookup**: Browser checks local cache $\rightarrow$ OS cache $\rightarrow$ Resolver $\rightarrow$ Root/TLD DNS server to resolve `google.com` to IP `142.250.190.46`.
2. **TCP 3-Way Handshake**: Client sends `SYN`, server returns `SYN-ACK`, client confirms with `ACK`.
3. **TLS Handshake (HTTPS)**: Cipher suite negotiation and certificate verification.
4. **HTTP GET Request**: Browser sends request headers.
5. **Server Processing & Response**: Server returns HTML/CSS/JS payload.
6. **DOM Rendering**: Browser parses HTML and renders page.
"""

with open('02-technical-coding/cs-fundamentals/networking-basics.md', 'w', encoding='utf-8') as f:
    f.write(networking_content)

# 6. arrays-strings.md
arrays_content = """# DSA Practice: Arrays & Strings

Core algorithmic patterns and fully solved Python implementations commonly tested in Accenture technical coding assessments.

---

## Pattern 1: Two Pointers (Valid Palindrome)

- **Problem**: Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
- **Code Solution (Python)**:
```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

---

## Pattern 2: Sliding Window (Maximum Sum Subarray of Size K)

- **Problem**: Given an array of integers and a number $k$, find the maximum sum of any contiguous subarray of size $k$.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$
- **Code Solution (Python)**:
```python
def maxSubarraySum(arr, k):
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

---

## Pattern 3: Hashing / Frequency Map (Two Sum)

- **Problem**: Find indices of two numbers in an array that add up to a target value.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
- **Code Solution (Python)**:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```
"""

with open('02-technical-coding/dsa-practice/arrays-strings.md', 'w', encoding='utf-8') as f:
    f.write(arrays_content)

# 7. dp-graphs.md
dp_content = """# DSA Practice: Dynamic Programming & Graphs

Core concepts and solutions for high-frequency placement questions on Dynamic Programming and Graph Algorithms.

---

## Pattern 1: Dynamic Programming (0/1 Knapsack Problem)

- **Problem**: Given weights and values of $N$ items, put these items in a knapsack of capacity $W$ to get maximum total value.
- **Time Complexity**: $O(N \times W)$
- **Space Complexity**: $O(W)$
- **Code Solution (Python)**:
```python
def knapsack(W, wt, val, n):
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
    return dp[W]
```

---

## Pattern 2: Graph Traversal (Breadth-First Search - BFS)

- **Problem**: Traverse a graph level-by-level starting from a source node using a Queue.
- **Time Complexity**: $O(V + E)$
- **Space Complexity**: $O(V)$
- **Code Solution (Python)**:
```python
from collections import deque

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
```
"""

with open('02-technical-coding/dsa-practice/dp-graphs.md', 'w', encoding='utf-8') as f:
    f.write(dp_content)

# 8. solved-problems-log.md
dsa_log_content = """# Solved Problems Log (DSA Practice)

Use this table to record coding questions solved on LeetCode, GeeksforGeeks, or PrepInsta during your placement preparation.

---

## DSA Problem Log Table

| Date | Problem Name | Platform | Topic / Pattern | Time Complexity | Space Complexity | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 | Two Sum | LeetCode (#1) | Hash Map | $O(N)$ | $O(N)$ | ✅ Solved (12 mins) |
| 2026-08-23 | Valid Anagram | LeetCode (#242) | Frequency Counting | $O(N)$ | $O(1)$ | ✅ Solved (8 mins) |
| YYYY-MM-DD | [Insert Problem Title] | LeetCode / GFG | [Two Pointers / DP / Graph] | $O(\dots)$ | $O(\dots)$ | [Solved / Review Needed] |
| YYYY-MM-DD | [Insert Problem Title] | LeetCode / GFG | [Two Pointers / DP / Graph] | $O(\dots)$ | $O(\dots)$ | [Solved / Review Needed] |
| YYYY-MM-DD | [Insert Problem Title] | LeetCode / GFG | [Two Pointers / DP / Graph] | $O(\dots)$ | $O(\dots)$ | [Solved / Review Needed] |
"""

with open('02-technical-coding/dsa-practice/solved-problems-log.md', 'w', encoding='utf-8') as f:
    f.write(dsa_log_content)

print("All 02-technical-coding files generated successfully.")
