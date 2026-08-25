# Core CS Fundamentals: DBMS, Normalization & SQL Joins

## 1. Database Normalization Forms

Normalization reduces data redundancy and prevents insertion, update, and deletion anomalies.

- **1NF (First Normal Form)**:
  - *Rule*: Every column cell must contain atomic (indivisible) values; no repeating groups or arrays.
- **2NF (Second Normal Form)**:
  - *Rule*: Must be in 1NF AND all non-key attributes must be fully functionally dependent on the primary key (eliminates partial dependency).
- **3NF (Third Normal Form)**:
  - *Rule*: Must be in 2NF AND no non-key attribute depends transitively on another non-key attribute (eliminates transitive dependency: $A ightarrow B$ and $B ightarrow C$).
- **BCNF (Boyce-Codd Normal Form)**:
  - *Rule*: For every functional dependency $X ightarrow Y$, $X$ must be a super key.

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
