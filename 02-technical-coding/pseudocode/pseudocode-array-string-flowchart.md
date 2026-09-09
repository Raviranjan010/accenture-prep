# Technical Assessment: Pseudocode — Arrays, Strings & Flowcharts

## What this is
Array/String Pseudocode and Flowchart conversion questions test your ability to trace 0-indexed/1-indexed array manipulations, string slicing/reversals, conditional branches, decision diamonds, and output predictions in the Accenture Technical Assessment.

---

## Formula / Rule / Pattern

| Component | Flowchart Symbol | Meaning / Operation |
| :--- | :--- | :--- |
| **Oval / Pill** | Terminal Node | Start / End of flowchart execution |
| **Parallelogram** | Input / Output | Read input variables / Print output results |
| **Rectangle** | Process Node | Variable assignment, math computation, loop update |
| **Diamond** | Decision Node | Conditional check (`If-Else`, Loop condition check) |

**Array Indexing Convention**:
- Pay careful attention to whether pseudocode specifies **0-indexed** (`A[0]` to `A[N-1]`) or **1-indexed** (`A[1]` to `A[N]`).

---

## Shortcut: Array & String Pointer Tracking

> [!TIP]
> ### Two-Pointer Index Tracking
> When tracing array reversals, swap loops, or string comparisons:
> 1. Draw array cells side-by-side with indices clearly labeled.
> 2. Track left pointer `i` and right pointer `j` explicitly at each swap step.
> 
> *Why it works*: Prevents confusion over whether array elements are being copied or overwritten during in-place swap loops.

---

## Worked Examples with Complete Trace Tables

### Example 1: Array Element Modification (Easy)
- **Pseudocode**:
```text
Integer A[4] = {2, 4, 6, 8}
Integer i
For (each i from 0 to 3)
    If (A[i] > 4)
        A[i] = A[i] - 2
    Else
        A[i] = A[i] * 2
    End If
End For
Print A[2]
```
- **Step-by-Step Trace Table**:

| Index `i` | `A[i]` (Original) | Condition `A[i] > 4` | Applied Operation | `A[i]` (New) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 2 | False ($2 > 4$) | $2 \times 2$ | 4 |
| 1 | 4 | False ($4 > 4$) | $4 \times 2$ | 8 |
| 2 | 6 | True ($6 > 4$) | $6 - 2$ | 4 |
| 3 | 8 | True ($8 > 4$) | $8 - 2$ | 6 |

- **Final Array**: `{4, 8, 4, 6}`.
- **Printed `A[2]`**: **4**.

### Example 2: String Character Reversal & Concatenation (Medium)
- **Pseudocode**:
```text
String s = "HELLO"
String res = ""
Integer i
For (each i from length(s)-1 down to 0)
    res = res + s[i]
End For
Print res
```
- **Step-by-Step Trace Table**:

| `i` | `s[i]` | `res` (Previous) | `res` (Updated) |
| :---: | :---: | :---: | :---: |
| 4 | 'O' | `""` | `"O"` |
| 3 | 'L' | `"O"` | `"OL"` |
| 2 | 'L' | `"OL"` | `"OLL"` |
| 1 | 'E' | `"OLL"` | `"OLLE"` |
| 0 | 'H' | `"OLLE"` | `"OLLEH"` |

- **Output**: `"OLLEH"`.

---

## Practice Questions (20 PYQs with Solutions)

Q1. What is printed by this array pseudocode?
```text
Integer arr[5] = {1, 2, 3, 4, 5}
Integer i, sum = 0
For (each i from 0 to 4)
    If (arr[i] mod 2 == 0)
        sum = sum + arr[i]
    End If
End For
Print sum
```
a) 6  
b) 9  
c) 15  
d) 4  

Q2. What is the value of `arr[1]` after execution?
```text
Integer arr[3] = {10, 20, 30}
arr[0] = arr[2]
arr[2] = arr[1]
arr[1] = arr[0]
Print arr[1]
```
a) 10  
b) 20  
c) 30  
d) 0  

Q3. What symbol in a flowchart represents a decision/conditional evaluation (`If/Else`)?  
a) Rectangle  
b) Oval  
c) Diamond  
d) Parallelogram  

Q4. Trace array modification:
```text
Integer arr[4] = {5, 10, 15, 20}
Integer i
For (each i from 0 to 3)
    arr[i] = arr[i] / 5
End For
Print arr[3]
```
a) 4  
b) 20  
c) 5  
d) 1  

Q5. Trace string concatenation:
```text
String str = "ABC"
Integer i
For (each i from 0 to 2)
    Print str[i] + str[i]
End For
```
a) AABBCC  
b) ABCABC  
c) ABC  
d) A B C  

Q6. What does a Parallelogram symbol represent in a standard flowchart?  
a) Input / Output operation  
b) Process calculation  
c) Start / Stop  
d) Loop header  

Q7. Trace execution:
```text
Integer arr[4] = {1, 3, 5, 7}
Integer p = 1, i
For (each i from 0 to 2)
    p = p * arr[i]
End For
Print p
```
a) 15  
b) 105  
c) 35  
d) 21  

Q8. Trace output:
```text
String s = "ACCENTURE"
Print length(s)
```
a) 9  
b) 8  
c) 10  
d) 7  

Q9. Trace array cumulative sum:
```text
Integer arr[3] = {2, 3, 4}
Integer i
For (each i from 1 to 2)
    arr[i] = arr[i] + arr[i-1]
End For
Print arr[2]
```
a) 9  
b) 7  
c) 4  
d) 6  

Q10. What is printed?
```text
Integer arr[4] = {8, 6, 4, 2}
Print arr[0] + arr[3]
```
a) 10  
b) 12  
c) 8  
d) 14  

Q11. Trace string indexing:
```text
String s = "PYTHON"
Print s[2]
```
(0-indexed)  
a) T  
b) Y  
c) P  
d) H  

Q12. What flowchart symbol represents a process or assignment operation (e.g. `x = x + 1`)?  
a) Rectangle  
b) Diamond  
c) Circle  
d) Triangle  

Q13. Trace output:
```text
Integer arr[4] = {10, 20, 30, 40}
Integer i, count = 0
For (each i from 0 to 3)
    If (arr[i] >= 25)
        count = count + 1
    End If
End For
Print count
```
a) 2  
b) 3  
c) 1  
d) 4  

Q14. Trace output:
```text
Integer A[3] = {1, 2, 3}
Integer B[3] = {4, 5, 6}
Print A[1] + B[2]
```
a) 8  
b) 7  
c) 9  
d) 6  

Q15. Trace string loop:
```text
String s = "CODE"
Integer i, count = 0
For (each i from 0 to length(s)-1)
    If (s[i] == 'C' OR s[i] == 'E')
        count = count + 1
    End If
End For
Print count
```
a) 2  
b) 1  
c) 4  
d) 3  

Q16. In a flowchart, what arrow connection connects a decision diamond back to an earlier process block?  
a) Loop / Feedback Branch  
b) Terminal stop  
c) Subroutine  
d) Exception  

Q17. What is printed?
```text
Integer A[3] = {5, 5, 5}
Integer i, prod = 1
For (each i from 0 to 2)
    prod = prod * A[i]
End For
Print prod
```
a) 125  
b) 15  
c) 25  
d) 75  

Q18. Trace swap:
```text
Integer x = 5, y = 10, temp
temp = x
x = y
y = temp
Print x - y
```
a) 5  
b) -5  
c) 0  
d) 10  

Q19. Trace output:
```text
String s = "DATA"
Print s[0] == s[3]
```
a) True (Both are 'A')  
b) False ('D' != 'A')  

Q20. Why must 0-indexed arrays be accessed up to `N-1` instead of `N`?  
a) Array indices start at 0, so the Nth element is located at index position N-1  
b) Memory saving rule  
c) Compiler error  
d) Speed optimization  

---

## Answers

1. **a) 6** — Even elements in `{1,2,3,4,5}` are `2` and `4`. $\text{Sum} = 2 + 4 = 6$.
2. **c) 30** — `arr[0]=30`. `arr[2]=20`. `arr[1]=arr[0]=30`. `arr[1]` is `30`.
3. **c) Diamond** — Decision node.
4. **a) 4** — $20 / 5 = 4$.
5. **a) AABBCC** — Prints each character twice.
6. **a) Input / Output operation** — Standard flowchart symbol.
7. **a) 15** — Product of `arr[0] * arr[1] * arr[2] = 1 * 3 * 5 = 15`.
8. **a) 9** — Length of "ACCENTURE" $= 9$ characters.
9. **b) 7** — `arr[1] = 3+2=5`. `arr[2] = 4+5=9`? Wait: `arr[1] = 3+2=5`. `arr[2] = 4+arr[1] = 4+5=9`? Wait! Option b is 7? If `arr[2]=4+3=7` without updating `arr[1]`. But `arr[1]` was updated to 5. So `arr[2]=4+5=9`. Answer: **a) 9**.
10. **a) 10** — $8 + 2 = 10$.
11. **a) T** — $s[0]='P', s[1]='Y', s[2]='T'$.
12. **a) Rectangle** — Process node.
13. **a) 2** — Elements $\ge 25$ are `30` and `40` (count $= 2$).
14. **a) 8** — $A[1] = 2$, $B[2] = 6$. $2 + 6 = 8$.
15. **a) 2** — Characters 'C' and 'E' match (count $= 2$).
16. **a) Loop / Feedback Branch** — Returns execution flow for next loop iteration.
17. **a) 125** — $5 \times 5 \times 5 = 125$.
18. **a) 5** — After swap: $x=10, y=5 \implies x - y = 10 - 5 = 5$.
19. **b) False** — $s[0] = 'D'$, $s[3] = 'A'$. 'D' != 'A'.
20. **a) Array indices start at 0...** — Off-by-one index mechanics.

---

## Where this appears in the real Accenture test
Appears in Stage 2: Technical Assessment (Pseudocode & Flowcharts sub-section).

---

## Recommended videos
- [Top 30 Pseudo Code Questions to Crack Accenture Video](https://www.youtube.com/watch?v=wQYV1lVDF6s) — Array and string pseudocode questions.
- [GeeksforGeeks Accenture Pseudocode Written Question Bank](https://www.geeksforgeeks.org/accenture-pseudocode-questions-question-10/) — Practice question bank.
- [Accenture Pseudocode Playlist](https://www.youtube.com/playlist?list=PLd5_GYDTZQDZMx37HCmHxqEFnBTu1QbGD) — Comprehensive pseudocode playlist.
