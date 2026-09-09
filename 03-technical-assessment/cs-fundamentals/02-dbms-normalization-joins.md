# CS Fundamentals: DBMS, Normalization & SQL Joins

## What this is
Database Management Systems (DBMS) organize structured data storage, querying, transaction processing, and data integrity. Normalization reduces data redundancy and eliminates insertion/deletion/update anomalies, while SQL Joins combine attributes across multiple related tables.

---

## Formula / Rule / Pattern

| Normal Form | Rule Requirement | Elimination Target |
| :--- | :--- | :--- |
| **1NF (First Normal Form)** | Atomic column values; no repeating groups/arrays | Multi-valued attributes |
| **2NF (Second Normal Form)** | Must be in 1NF AND no Partial Dependencies | Non-prime attributes dependent on part of composite key |
| **3NF (Third Normal Form)** | Must be in 2NF AND no Transitive Dependencies | Non-prime attributes dependent on another non-prime attribute |
| **BCNF (Boyce-Codd NF)** | For every functional dependency $X \rightarrow Y$, $X$ must be a Super Key | Anomalies left in 3NF |

**SQL Join Types Summary**:
- `INNER JOIN`: Returns rows matching on join condition in **both** tables.
- `LEFT JOIN`: Returns **all** rows from left table + matching rows from right table (fills `NULL` for non-matches).
- `RIGHT JOIN`: Returns **all** rows from right table + matching rows from left table.
- `FULL OUTER JOIN`: Returns all rows when there is a match in either left or right table.

---

## Shortcut: The 3-Step Normalization Diagnostic

> [!TIP]
> ### 3-Step Normalization Diagnostic
> Check a database relation schema in this 3-step order:
> 
> 1. **1NF Check**: Are all column values single atomic values? (If yes $\implies$ 1NF).
> 2. **2NF Check**: Is any non-key attribute dependent on *only part* of a composite Primary Key? (If no $\implies$ 2NF).
> 3. **3NF Check**: Is any non-key attribute dependent on *another non-key* attribute? ($A \rightarrow B \rightarrow C$, If no $\implies$ 3NF).
> 
> *Why it works*: Evaluates dependencies sequentially against key definitions, pinpointing the highest normal form of any relation table in under 30 seconds.

---

## Worked Examples

### Example 1: SQL Join Evaluation (Easy)
- **Tables**:
  - `Students`: `(id, name)` $\rightarrow$ `(1, "Alice"), (2, "Bob"), (3, "Charlie")`
  - `Grades`: `(student_id, grade)` $\rightarrow$ `(1, "A"), (2, "B")`
- **Query**: `SELECT Students.name, Grades.grade FROM Students LEFT JOIN Grades ON Students.id = Grades.student_id;`
- **Output Rows**:
  1. `Alice | A`
  2. `Bob | B`
  3. `Charlie | NULL` (Kept because LEFT JOIN preserves all rows of `Students`).

### Example 2: Normalization Anomaly Diagnosis (Medium)
- **Relation**: `Employee(EmpID, EmpName, DeptID, DeptName)`. Primary Key $= \text{EmpID}$. Functional Dependency: $\text{DeptID} \rightarrow \text{DeptName}$.
- **Step-by-step Solution**:
  1. Primary key is single attribute `EmpID` (No composite key $\implies$ Automatically 2NF).
  2. Check Transitive Dependency: $\text{EmpID} \rightarrow \text{DeptID}$ AND $\text{DeptID} \rightarrow \text{DeptName}$.
  3. Non-key attribute `DeptName` depends on non-key attribute `DeptID`.
  4. **Diagnosis**: Violates 3NF due to transitive dependency. Decompose into `Employee(EmpID, EmpName, DeptID)` and `Department(DeptID, DeptName)`.

---

## Practice Questions (PYQ Bank)

Q1. What is the primary objective of Database Normalization?  
a) Maximize query speed  
b) Minimize data redundancy and eliminate update/insertion/deletion anomalies  
c) Encrypt storage  
d) Increase table size  

Q2. Which normal form eliminates Partial Functional Dependencies?  
a) 1NF  
b) 2NF  
c) 3NF  
d) BCNF  

Q3. What does ACID stand for in DBMS transactions?  
a) Accuracy, Consistency, Isolation, Durability  
b) Atomicity, Consistency, Isolation, Durability  
c) Atomicity, Concurrency, Integrity, Durability  
d) Access, Control, Isolation, Data  

Q4. Which SQL clause is used to filter aggregated group records produced by `GROUP BY`?  
a) `WHERE`  
b) `HAVING`  
c) `ORDER BY`  
d) `LIKE`  

Q5. Which JOIN returns all rows from the right table even if there are no matches in the left table?  
a) INNER JOIN  
b) LEFT JOIN  
c) RIGHT JOIN  
d) CROSS JOIN  

Q6. A Super Key is defined as:  
a) Any column with numbers  
b) A set of one or more attributes that uniquely identifies a row in a table  
c) A foreign key  
d) A primary key without index  

Q7. In a relational table, what is a candidate key?  
a) A minimal Super Key with no redundant attributes  
b) Any column  
c) A non-key column  
d) Secondary key  

Q8. What happens during a `DELETE` command versus a `TRUNCATE` command in SQL?  
a) `DELETE` is DML (logged per row, can be rolled back); `TRUNCATE` is DDL (deletes all rows faster, resets auto-increment)  
b) `TRUNCATE` deletes table structure  
c) `DELETE` cannot be rolled back  
d) They are identical  

Q9. What property of ACID guarantees that all operations of a transaction execute completely or none execute at all?  
a) Atomicity  
b) Consistency  
c) Isolation  
d) Durability  

Q10. Which SQL key constraints enforces referential integrity between two tables?  
a) PRIMARY KEY  
b) FOREIGN KEY  
c) UNIQUE  
d) CHECK  

Q11. What type of database join produces a Cartesian product of two tables (rows in A $\times$ rows in B)?  
a) INNER JOIN  
b) CROSS JOIN  
c) LEFT JOIN  
d) FULL JOIN  

Q12. What does BCNF require for every functional dependency $X \rightarrow Y$?  
a) $Y$ must be a super key  
b) $X$ must be a Super Key  
c) $X$ must be prime  
d) $Y$ must be atomic  

Q13. In SQL, what is the default sorting order of `ORDER BY` if unspecified?  
a) `ASC` (Ascending)  
b) `DESC` (Descending)  

Q14. Which command is DDL (Data Definition Language)?  
a) `SELECT`  
b) `INSERT`  
c) `CREATE`  
d) `UPDATE`  

Q15. Why does 3NF require eliminating transitive dependencies?  
a) Transitive dependencies cause update anomalies when dependent non-key attributes change  
b) To reduce column count  
c) To force primary keys  
d) SQL syntax error  

---

## Answers

1. **b) Minimize data redundancy and eliminate anomalies** — Goal of normalization.
2. **b) 2NF** — 2NF eliminates partial dependency on composite keys.
3. **b) Atomicity, Consistency, Isolation, Durability** — Definition of ACID properties.
4. **b) `HAVING`** — `HAVING` filters post-aggregation groups; `WHERE` filters pre-aggregation rows.
5. **c) RIGHT JOIN** — Preserves all rows of right-side table.
6. **b) A set of one or more attributes that uniquely identifies a row...** — Definition of Super Key.
7. **a) A minimal Super Key with no redundant attributes** — Definition of Candidate Key.
8. **a) `DELETE` is DML... `TRUNCATE` is DDL...** — Key distinction between DML delete and DDL truncate.
9. **a) Atomicity** — All-or-nothing property.
10. **b) FOREIGN KEY** — Enforces link referential integrity.
11. **b) CROSS JOIN** — Produces $M \times N$ row Cartesian combinations.
12. **b) $X$ must be a Super Key** — Strict requirement of BCNF.
13. **a) `ASC`** — Default sort order.
14. **c) `CREATE`** — DDL command altering schema definition.
15. **a) Transitive dependencies cause update anomalies...** — Rationale for 3NF decomposition.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Core CS Fundamentals Technical MCQ section.

---

## Recommended videos
- [Accenture Technical Assessment MCQs & Pseudocode Video](https://www.youtube.com/watch?v=DwZZNJxBAn0) — CS fundamentals section.
- [Accenture Technical Practice Walkthrough](https://www.youtube.com/watch?v=1pW3xrNu1z8) — DBMS & SQL join practice.
