# Core CS Fundamentals: DBMS, Normalization & SQL Joins

## 1. What is it?
A **Database Management System (DBMS)** is specialized software used to store, organize, manage, and retrieve large amounts of structured data efficiently and securely.

### Beginner Vocabulary Glossary
Before exploring database queries, let's define core concepts in plain language:
- **Database**: A digital filing cabinet stored on a server.
- **Table**: A structured grid of data arranged in rows and columns (like a spreadsheet sheet).
- **Row (Record / Tuple)**: A single horizontal entry representing one specific entity (e.g., Student #101).
- **Column (Attribute / Field)**: A vertical category of information (e.g., `Email`, `Phone_Number`).
- **Primary Key (PK)**: A unique identifier column that guarantees no two rows in a table are identical (e.g., `Student_ID`, `Aadhaar_Number`).
- **Foreign Key (FK)**: A column in one table that links directly to the Primary Key of another table, establishing a connection between the two tables.
- **SQL (Structured Query Language)**: The standardized language used to communicate with relational databases.

---

## 2. Why does it matter?
1. **High Assessment Frequency**: DBMS concepts (Normalization, SQL Joins, ACID properties) appear in almost every Accenture technical test and interview.
2. **Data Integrity & Consistency**: Prevents duplicate records, conflicting customer records, and accidental data corruption in production apps.
3. **High-Speed Data Retrieval**: Indexes and optimized database structures allow apps to query millions of records in milliseconds.

---

## 3. When to use it?
- **Use Relational DBMS (SQL) when**: Data is highly structured with clear relationships (e.g., Banking systems, Order processing, Inventory management).
- **Use Non-Relational DBMS (NoSQL) when**: Handling unstructured or rapidly changing schemas (e.g., real-time social media feeds, raw event logs).

---

## 4. How it works
1. **Schema Definition**: You define tables, column data types (INTEGER, VARCHAR, DATE), and primary/foreign keys.
2. **Data Insertion & Storage**: Data is written to disk storage in structured data blocks.
3. **Query Execution**: When a user submits an SQL query (e.g., `SELECT * FROM Users`), the database query engine parses the query, optimizes the execution plan, fetches matching disk pages, and returns the result table.

---

## 5. Key rules or syntax

### Fundamental SQL Syntax
```sql
-- Creating a table with Primary Key
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Creating a table with Foreign Key reference
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- Basic Data Retrieval Query
SELECT student_id, student_name 
FROM Students 
WHERE dept_id = 10;
```
*Why primary and foreign keys work*: The primary key forces strict uniqueness constraints at the storage engine layer, while foreign keys prevent orphaned records (e.g., enrolling a student in a department ID that doesn't exist).

---

## 6. Simple example

### Level 1 (Easy): Linking Two Tables via Primary and Foreign Key
- **Departments Table**:
  | dept_id (PK) | dept_name |
  | :--- | :--- |
  | 1 | Computer Science |
  | 2 | Electronics |

- **Students Table**:
  | student_id (PK) | student_name | dept_id (FK) |
  | :--- | :--- | :--- |
  | 101 | Ravi | 1 |
  | 102 | Priya | 2 |

---

## 7. Detailed example

### Part A: Database Normalization Forms

Normalization is the process of organizing database tables to reduce redundancy and eliminate update/insertion/deletion anomalies.

#### 1NF (First Normal Form)
- **Rule**: Every table cell must contain **atomic** (indivisible) single values, and there must be no repeating groups.
- **Un-normalized Table (Bad)**:
  | Student_ID | Name | Subjects |
  | :--- | :--- | :--- |
  | 101 | Ravi | Java, DBMS, OS |
- **Simple Beginner Example (1NF Conversion)**:
  | Student_ID | Name | Subject |
  | :--- | :--- | :--- |
  | 101 | Ravi | Java |
  | 101 | Ravi | DBMS |
  | 101 | Ravi | OS |
- **Realistic Enterprise Example**: Separating multi-valued phone numbers or address lists into individual atomic rows or child relationship tables.

#### 2NF (Second Normal Form)
- **Rule**: Must be in **1NF** AND have **no partial dependency** (every non-key column must depend on the *entire* primary key, not just part of a composite key).
- **Non-2NF Table (Bad - Composite Key `{Student_ID, Course_ID}`)**:
  | Student_ID | Course_ID | Student_Name | Course_Fee |
  | :--- | :--- | :--- | :--- |
  | 101 | C1 | Ravi | ₹5000 |
  *Problem*: `Student_Name` depends only on `Student_ID` (partial dependency).
- **Realistic Enterprise Example (2NF Split)**: Split into two clean tables:
  1. `Students(Student_ID, Student_Name)`
  2. `CourseEnrollments(Student_ID, Course_ID, Course_Fee)`

#### 3NF (Third Normal Form)
- **Rule**: Must be in **2NF** AND have **no transitive dependency** (non-key columns must NOT depend on other non-key columns: $A ightarrow B$ and $B ightarrow C$).
- **Non-3NF Table (Bad)**:
  | Student_ID (PK) | Zip_Code | City |
  | :--- | :--- | :--- |
  | 101 | 144411 | Phagwara |
  *Problem*: `City` depends on `Zip_Code`, which depends on `Student_ID` ($Student\_ID ightarrow Zip\_Code ightarrow City$).
- **Realistic Enterprise Example (3NF Split)**:
  1. `Students(Student_ID, Zip_Code)`
  2. `ZipCodes(Zip_Code, City)`

#### BCNF (Boyce-Codd Normal Form)
- **Rule**: A stricter version of 3NF. For every functional dependency $X ightarrow Y$, $X$ MUST be a **super key**.

---

### Part B: SQL Joins Explained

#### 1. INNER JOIN
- **Concept**: Returns only records that have matching values in **both** tables.
- **Realistic Enterprise Example**:
```sql
SELECT Students.student_name, Departments.dept_name
FROM Students
INNER JOIN Departments ON Students.dept_id = Departments.dept_id;
```

#### 2. LEFT (OUTER) JOIN
- **Concept**: Returns **all** records from the left table, and matched records from the right table (returns `NULL` for unmatched right columns).
- **Realistic Enterprise Example**: Finding all customers, including those who have placed 0 orders.
```sql
SELECT Customers.customer_name, Orders.order_id
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

#### 3. RIGHT (OUTER) JOIN
- **Concept**: Returns **all** records from the right table, and matched records from the left table.

#### 4. FULL (OUTER) JOIN
- **Concept**: Returns all records when there is a match in either left or right table.

---

### Part C: ACID Properties of Transactions
- **Atomicity**: "All or Nothing". Either all steps of a transaction complete successfully, or the entire transaction is rolled back (e.g., money deducted from Account A MUST be credited to Account B, or both steps abort).
- **Consistency**: Database transitions strictly from one valid state to another valid state, preserving all integrity constraints.
- **Isolation**: Concurrent transactions execute without interfering with each other (prevents dirty reads).
- **Durability**: Once a transaction is committed, changes persist permanently in disk storage even if a power outage occurs immediately after.

---

## 8. Practical use case
**Banking Money Transfer System**:
When transferring ₹5,000 from Ravi to Priya:
1. `Atomicity` ensures if network drops halfway, Ravi's account isn't debited without Priya being credited.
2. `3NF Normalization` ensures accounts, customers, and branch details are stored without redundancy.
3. `SQL INNER JOIN` combines Account and Customer details to generate monthly bank statements instantly.

---

## 9. Common mistakes

### Concept 1: Normalization Mistakes
- *Mistake*: Keeping comma-separated lists in a single text column (e.g., `skills = "Java, Python, C++"`).
- *Why it happens*: Looks simple, but violates **1NF**, making SQL queries like `WHERE skill = 'Python'` extremely slow and impossible to index.

### Concept 2: SQL Join Mistakes
- *Mistake*: Confusing `INNER JOIN` with `LEFT JOIN`.
- *Why it happens*: Using `INNER JOIN` when you need to display all records (e.g., listing all students even if they haven't been assigned a department yet) accidentally filters out unassigned students!

### Concept 3: Transaction Isolation Mistakes
- *Mistake*: Forgetting to execute database transactions inside `BEGIN TRANSACTION` and `COMMIT` blocks.
- *Why it happens*: Without explicit transaction boundaries, intermediate database queries execute auto-commit mode, risking incomplete data updates during system crashes.

---

## 10. Tips & tricks

### Shortcut 1: The LEFT JOIN Survival Rule
- **Rule**: In `TableA LEFT JOIN TableB`, **TableA is guaranteed to survive completely**. Every row in TableA will appear in the output. Unmatched TableB columns will simply show as `NULL`.

### Shortcut 2: 3NF Transitive Arrow Test
- **Rule**: Look at every non-key column. Ask: *"Does Attribute B depend on Attribute A, which is NOT the Primary Key?"* If YES $\implies$ Transitive dependency exists! Split B into a new lookup table.

### Shortcut 3: Normalization Hierarchy Quick Check
- **Rule**: Remember the sequence: $1NF ightarrow 2NF ightarrow 3NF ightarrow BCNF$.
  - 1NF = Atomic values.
  - 2NF = No partial dependency.
  - 3NF = No transitive dependency.

---

## 11. Practice exercises

1. **(Easy - Recall)** What does PK and FK stand for in relational databases?
2. **(Easy - Recall)** Which SQL Join returns only matching records present in both tables?
3. **(Easy - Concept)** What requirement must be satisfied for a table to be in First Normal Form (1NF)?
4. **(Medium - Why)** Why is storing comma-separated values in a single database column considered bad database design?
5. **(Medium - Scenario)** A table has a composite primary key `{Course_ID, Student_ID}`. If `Instructor_Name` depends only on `Course_ID`, which Normal Form is violated?
6. **(Medium - Applied)** Given `Employees` (10 rows) and `Departments` (5 rows). If 2 employees have no department assigned (`dept_id = NULL`), how many rows will be returned by:
   - a) `INNER JOIN`
   - b) `LEFT JOIN` (Employees on left)
7. **(Medium - Scenario)** Explain the "Atomicity" property in ACID using an ATM cash withdrawal example.
8. **(Hard - Applied)** Write an SQL query to retrieve `student_name` and `dept_name` for all students, including those who do not belong to any department.
9. **(Hard - Scenario)** Consider functional dependencies $A ightarrow B$ and $B ightarrow C$ in a table with Primary Key $A$. Which normal form does this violate, and how do you fix it?
10. **(Hard - Architecture)** Explain how Database Indexing speeds up `SELECT` queries while slightly slowing down `INSERT` operations.

---

## 12. Q&A with explanations

1. **Answer**: **PK** = Primary Key (unique row identifier); **FK** = Foreign Key (refers to PK of another table).
2. **Answer**: `INNER JOIN`.
3. **Answer**: Every column must hold atomic (single, indivisible) values, with no repeating groups/arrays.
4. **Answer**: It violates 1NF, prevents database indexing, makes searching/filtering specific elements inefficient, and prevents foreign key constraints.
5. **Answer**: It violates **2NF** due to a **partial dependency** (`Instructor_Name` depends on part of the composite primary key `Course_ID`).
6. **Answer**:
   - a) `INNER JOIN`: **8 rows** (filters out the 2 employees with `NULL` department IDs).
   - b) `LEFT JOIN`: **10 rows** (all 10 employees survive; the 2 unassigned show `NULL` for department info).
7. **Answer**: Atomicity ensures that if the ATM dispenses cash, your account balance IS debited. If cash dispenser fails halfway, money deduction is rolled back completely.
8. **Answer**:
   ```sql
   SELECT S.student_name, D.dept_name
   FROM Students S
   LEFT JOIN Departments D ON S.dept_id = D.dept_id;
   ```
9. **Answer**: Violates **3NF** due to transitive dependency ($A ightarrow B ightarrow C$). Fix by splitting into two tables: `Table1(A, B)` and `Table2(B, C)`.
10. **Answer**: Indexes create B-Tree/B+Tree lookup structures that allow $O(\log N)$ binary-style search instead of $O(N)$ full table scans. However, every `INSERT` forces the database engine to update both the data table and the B-Tree index structures.

---

## 13. Quick revision

> [!TIP]
> ### 🚀 DBMS & SQL Cheat-Sheet
> - **Primary Key**: Unique identifier, non-null.
> - **Foreign Key**: Refers to Primary Key in another table.
> - **1NF**: Atomic values only (no arrays/commas).
> - **2NF**: 1NF + No partial dependencies.
> - **3NF**: 2NF + No transitive dependencies.
> - **INNER JOIN**: Only matching records from both tables.
> - **LEFT JOIN**: All left table rows + matching right table rows.
> - **ACID**: Atomicity (All/Nothing), Consistency (Valid state), Isolation (Independent), Durability (Persistent).

---

## 14. Connection to next topic
Now that you understand how relational database engines organize structured data, let's explore how the underlying Operating System manages hardware CPU scheduling, RAM memory, and processes to run these databases! Continue to **[os-basics.md](os-basics.md)**.
