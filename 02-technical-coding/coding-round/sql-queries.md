# Coding Round: SQL Queries — Complete Practice Bank

## What this is
SQL Query writing is tested extensively in Accenture Technical & Coding Assessments. Questions require writing precise DML/DQL queries involving JOINs, GROUP BY aggregations, HAVING filters, subqueries, string functions, and window ranking functions.

---

## Formula & Shortcut

> [!TIP]
> ### SQL Query Order of Execution
> Write and debug SQL queries following the **logical order of execution**:
> 
> $$\text{1. FROM / JOIN} \rightarrow \text{2. WHERE} \rightarrow \text{3. GROUP BY} \rightarrow \text{4. HAVING} \rightarrow \text{5. SELECT} \rightarrow \text{6. ORDER BY}$$
> 
> *Why it works*: Most SQL syntax errors occur because candidates attempt to use alias names defined in `SELECT` inside `WHERE` or `GROUP BY` before those clauses execute.

---

## 10 Solved SQL Query Problems

### Database Schema Context
- `Employees(emp_id, emp_name, dept_id, salary, hire_date)`
- `Departments(dept_id, dept_name, location)`

---

### Problem 1: Second Highest Salary in Employees Table
- **Query**:
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);
```

---

### Problem 2: Department-wise Employee Count & Average Salary
- **Query**:
```sql
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees, AVG(e.salary) AS avg_salary
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

---

### Problem 3: Departments with Total Salary Expense > 1,00,000
- **Query**:
```sql
SELECT d.dept_name, SUM(e.salary) AS total_expense
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING SUM(e.salary) > 100000;
```

---

### Problem 4: Highest Paid Employee in Each Department
- **Query (Using Subquery / Window Function)**:
```sql
SELECT dept_id, emp_name, salary
FROM (
    SELECT dept_id, emp_name, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rnk
    FROM Employees
) t
WHERE rnk = 1;
```

---

### Problem 5: Employees Hired in the Year 2023
- **Query**:
```sql
SELECT emp_name, hire_date
FROM Employees
WHERE YEAR(hire_date) = 2023;
```

---

### Problem 6: Find Employees Without Any Assigned Department
- **Query**:
```sql
SELECT emp_id, emp_name
FROM Employees
WHERE dept_id IS NULL;
```

---

### Problem 7: Find Employees Earning Above Their Department Average
- **Query**:
```sql
SELECT e.emp_name, e.salary, e.dept_id
FROM Employees e
WHERE e.salary > (
    SELECT AVG(emp.salary)
    FROM Employees emp
    WHERE emp.dept_id = e.dept_id
);
```

---

### Problem 8: Duplicate Employee Name Finder
- **Query**:
```sql
SELECT emp_name, COUNT(*) AS count
FROM Employees
GROUP BY emp_name
HAVING COUNT(*) > 1;
```

---

### Problem 9: Second Employee Hired in Company
- **Query**:
```sql
SELECT emp_name, hire_date
FROM Employees
ORDER BY hire_date ASC
LIMIT 1 OFFSET 1;
```

---

### Problem 10: Department Name with Maximum Number of Employees
- **Query**:
```sql
SELECT d.dept_name
FROM Departments d
JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY COUNT(e.emp_id) DESC
LIMIT 1;
```

---

## Where this appears in the real Accenture test
Appears in Stage 3: Coding Round / Technical SQL assessment section.

---

## Recommended videos
- [Accenture Technical Assessment SQL & Coding Walkthrough](https://www.youtube.com/watch?v=DwZZNJxBAn0) — SQL query practice.
