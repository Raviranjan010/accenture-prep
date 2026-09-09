# CS Fundamentals: MS Office & Common Applications

## What this is
MS Office and Common Productivity Applications (Excel, Word, PowerPoint) evaluate workplace digital literacy, data manipulation, formula usage, document formatting, and presentation design concepts tested in Accenture technical MCQs.

---

## Formula / Rule / Pattern

| Application | Core Feature | High-Frequency Functions / Concepts |
| :--- | :--- | :--- |
| **MS Excel** | Spreadsheet & Data Analysis | Formulas (`SUM`, `AVERAGE`, `IF`, `VLOOKUP`, `XLOOKUP`), Pivot Tables, Sorting/Filtering, Absolute (`$A$1`) vs Relative (`A1`) Referencing |
| **MS Word** | Document Formatting & Publishing | Mail Merge, Track Changes, Headers/Footers, Page Breaks, Styles |
| **MS PowerPoint** | Visual Slide Presentations | Slide Master (global layout consistency), Transitions, Animations, Presenter View |

---

## Shortcut: Excel Referencing & VLOOKUP Syntax

> [!TIP]
> ### The Excel VLOOKUP & Reference Lock Formula
> 1. **VLOOKUP Syntax**: `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`
>    - `lookup_value`: What you want to look up.
>    - `table_array`: The range containing the lookup column (MUST be 1st column) and target column.
>    - `col_index_num`: Column index (1-indexed) in the range containing the return value.
>    - `range_lookup`: Set to `FALSE` (or `0`) for exact match.
> 2. **Absolute Referencing (`$`)**: Putting `$` before column/row (e.g. `$B$4`) prevents cell reference shift when dragging/copying formulas.
> 
> *Why it works*: 70% of MS Office assessment questions test VLOOKUP arguments or absolute vs relative cell copy behavior.

---

## Worked Examples

### Example 1: Excel IF Condition (Easy)
- **Formula**: `=IF(A1 >= 60, "Pass", "Fail")`
- **Question**: What value is returned if cell `A1` contains `60`?
- **Step-by-step Solution**:
  1. Condition check: `60 >= 60` evaluates to `TRUE`.
  2. The `TRUE` branch value is `"Pass"`.
  3. **Output**: `"Pass"`.

### Example 2: Excel VLOOKUP Exact Match (Medium)
- **Data Table Range A1:B4**:
  - `A1: 101`, `B1: Alice`
  - `A2: 102`, `B2: Bob`
  - `A3: 103`, `B3: Charlie`
- **Formula**: `=VLOOKUP(102, A1:B3, 2, FALSE)`
- **Step-by-step Solution**:
  1. Searches 1st column (`Col A`) for exact match `102`. Found at row 2.
  2. `col_index_num = 2` $\implies$ returns value from 2nd column (`Col B`).
  3. Row 2, Col B is `"Bob"`.
  4. **Output**: `"Bob"`.

### Example 3: MS Word Mail Merge Concept (Hard)
- **Question**: Which feature in MS Word enables generating 500 personalized offer letters with distinct candidate names and addresses from an Excel spreadsheet recipient list automatically?
- **Step-by-step Solution**:
  1. Main Document template in Word + Data Source in Excel.
  2. Fields inserted: `<<First_Name>>`, `<<Address>>`.
  3. **Feature**: **Mail Merge**.

---

## Practice Questions (PYQ Bank)

Q1. Which Excel formula is used to look up a value in the first column of a table array and return a value in the same row from another column?  
a) `COUNTIF`  
b) `VLOOKUP`  
c) `SUMIF`  
d) `CONCATENATE`  

Q2. What does putting a dollar sign (`$`) before a column letter and row number (e.g. `$C$5`) do in Excel?  
a) Formats cell as US Dollars  
b) Creates an Absolute Cell Reference that does not change when copied to other cells  
c) Locks the worksheet with a password  
d) Deletes the cell  

Q3. In MS Word, which feature allows multiple reviewers to collaborate, edit, and highlight additions or deletions made to a document?  
a) Mail Merge  
b) Track Changes  
c) Slide Master  
d) Watermark  

Q4. Which tool in MS Excel allows summarizing, analyzing, exploring, and presenting large multidimensional datasets interactively?  
a) Pivot Table  
b) Mail Merge  
c) Macro Recorder  
d) Text to Columns  

Q5. In MS PowerPoint, what feature allows setting global formatting (font style, background, logo positioning) across all slides simultaneously?  
a) Slide Transition  
b) Slide Master  
c) Animation Pane  
d) Presenter View  

Q6. What Excel formula returns the count of non-empty cells in a range `A1:A10` that meet a specific condition (e.g. `>50`)?  
a) `COUNT`  
b) `COUNTA`  
c) `COUNTIF`  
d) `SUMIF`  

Q7. Which shortcut key in MS Office pastes copied content?  
a) Ctrl + C  
b) Ctrl + V  
c) Ctrl + X  
d) Ctrl + Z  

Q8. Which MS Office application would you select to create an interactive multi-table relational budget database with queries and entry forms?  
a) MS Word  
b) MS Access / Excel  
c) MS PowerPoint  
d) MS Publisher  

Q9. In Excel, what is the result of formula `=SUM(5, 10, 15)`?  
a) 30  
b) 15  
c) 51015  
d) 5  

Q10. What character must every Excel formula begin with?  
a) `#`  
b) `@`  
c) `=`  
d) `$`  

Q11. In MS Word, what is the default page orientation for a new blank document?  
a) Landscape  
b) Portrait  
c) Square  
d) Custom  

Q12. What does range lookup argument `FALSE` specify in `=VLOOKUP(val, table, col, FALSE)`?  
a) Approximate match  
b) Exact match  
c) Case sensitive match  
d) Reverse search  

Q13. In PowerPoint, what is the difference between Slide Transitions and Animations?  
a) Transitions apply to entire slide movements between slides; Animations apply to individual objects on a slide  
b) Animations move slides  
c) They are identical  
d) Transitions play audio  

Q14. In Excel, what does error `#DIV/0!` signify?  
a) Value missing  
b) Formula attempting to divide a number by zero  
c) Column width too narrow  
d) Text error  

Q15. Why is absolute referencing (`$`) critical when copying VLOOKUP formulas down a column of 100 rows?  
a) Prevents the `table_array` range from shifting down row-by-row during formula drag  
b) Speeds up computer RAM  
c) Adds dollar signs to numbers  
d) Enables macros  

---

## Answers

1. **b) `VLOOKUP`** — Vertical lookup function.
2. **b) Creates an Absolute Cell Reference...** — Prevents reference coordinate shifting.
3. **b) Track Changes** — Collaborative editing feature in Word.
4. **a) Pivot Table** — Data summarization tool in Excel.
5. **b) Slide Master** — Global template hierarchy manager in PPT.
6. **c) `COUNTIF`** — Conditional counting function.
7. **b) Ctrl + V** — Standard paste shortcut.
8. **b) MS Access / Excel** — Relational database / spreadsheet tool.
9. **a) 30** — $5 + 10 + 15 = 30$.
10. **c) `=`** — Mandatory formula starting token.
11. **b) Portrait** — Standard vertical page orientation.
12. **b) Exact match** — Requires exact string/number match.
13. **a) Transitions apply to entire slide movements...** — Key distinction.
14. **b) Formula attempting to divide a number by zero** — Division by zero error.
15. **a) Prevents the table_array range from shifting down...** — Reference locking mechanics.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Technical Assessment (MS Office & Common Applications sub-section).

---

## Recommended videos
- TODO: find video for MS Office / Common Applications MCQ practice specific to Accenture
