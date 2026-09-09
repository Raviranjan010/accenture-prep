# Full Timed Mock Test Paper #1

> **Duration**: 90 Minutes  
> **Total Questions**: 40 Questions  
> **Sections Included**: Aptitude (Quant/Logical/Verbal), CS Fundamentals, Pseudocode, Cloud/Security, MS Office  
> **Instructions**: Set a timer for 90 minutes. Answer all questions without checking the answer key. Compare your choices against [mock-test-1-answers.md](mock-test-1-answers.md) upon completion and log your score in [score-tracker.md](score-tracker.md).

---

## Section 1: Quantitative Aptitude & DI (Questions 1–8)

Q1. A laptop bought for ₹40,000 is sold for ₹48,000. What is the profit percentage?  
a) 15%  
b) 20%  
c) 25%  
d) 18%  

Q2. If $A:B = 3:5$ and $B:C = 10:11$, find $A:C$.  
a) 6:11  
b) 3:11  
c) 5:11  
d) 1:2  

Q3. A train 200m long running at 72 km/h passes a pole. Time taken is:  
a) 8 seconds  
b) 10 seconds  
c) 12 seconds  
d) 15 seconds  

Q4. Convert $16.67\%$ into a simplified fraction.  
a) 1/5  
b) 1/6  
c) 1/8  
d) 1/7  

Q5. Average marks of 5 subjects is 70. If one mark of 90 is excluded, what is the new average?  
a) 65  
b) 66  
c) 68  
d) 64  

Q6. Pie chart question: A company budget allocates $90^\circ$ sector angle to R&D out of a total budget of ₹80 Lakhs. How much is spent on R&D?  
a) ₹20 Lakhs  
b) ₹15 Lakhs  
c) ₹25 Lakhs  
d) ₹18 Lakhs  

Q7. Salary increases by 20% and then decreases by 10%. Net % change is:  
a) +10%  
b) +8%  
c) +12%  
d) -2%  

Q8. In a 3x3 grid, Start is at (1,1) and End is at (3,3). How many minimum cardinal grid steps are required?  
a) 3 steps  
b) 4 steps  
c) 5 steps  
d) 6 steps  

---

## Section 2: Logical Reasoning & Gamified Concepts (Questions 9–16)

Q9. Pointing to a photo, Anand said, "Her mother is the only daughter of my mother." How is Anand related to the girl?  
a) Brother  
b) Father  
c) Uncle  
d) Cousin  

Q10. In a code language, `LIGHT` is written as `MJHIU`. How is `FRAME` written?  
a) GSBNF  
b) GSCNF  
c) EQZLD  
d) HSBNF  

Q11. 5 friends sit in a row facing North. A is at extreme left, C is in middle, B is to immediate right of C. D is between A and C. Who sits at extreme right?  
a) E  
b) B  
c) D  
d) C  

Q12. Complete series: 2, 6, 12, 20, 30, ?  
a) 40  
b) 42  
c) 44  
d) 48  

Q13. In Path Finder, why should you start solving backward from the End tile?  
a) End tiles usually have fewer rotation possibilities than Start tiles  
b) Timer stops  
c) Tile turns blue  

Q14. In Memory Maze, what is the recommended chunking target?  
a) 16 cells  
b) 3-4 reference point coordinates (Start, Key, Door)  
c) All walls  

Q15. Find odd one out: 27, 64, 125, 144, 216.  
a) 27  
b) 144 (it is $12^2$, others are perfect cubes)  
c) 125  
d) 216  

Q16. Rank in ascending order: $A = 15 \times 3 (45)$, $B = 100 / 4 (25)$, $C = 20\% \text{ of } 200 (40)$.  
a) B, C, A  
b) A, B, C  
c) C, B, A  
d) B, A, C  

---

## Section 3: Core CS Fundamentals (Questions 17–24)

Q17. Which OOP principle restricts direct access to member variables using `private` modifiers?  
a) Encapsulation  
b) Inheritance  
c) Polymorphism  
d) Abstraction  

Q18. Which normal form eliminates transitive dependencies?  
a) 1NF  
b) 2NF  
c) 3NF  
d) BCNF  

Q19. What protocol translates domain names into IP addresses?  
a) DHCP  
b) ARP  
c) DNS  
d) ICMP  

Q20. What is the standard port for HTTPS?  
a) 80  
b) 443  
c) 22  
d) 25  

Q21. What component translates virtual addresses to physical addresses in hardware?  
a) ALU  
b) MMU / TLB  
c) GPU  
d) ROM  

Q22. Which JOIN returns all rows from the left table regardless of matches in the right table?  
a) INNER JOIN  
b) LEFT JOIN  
c) RIGHT JOIN  
d) CROSS JOIN  

Q23. What property of ACID ensures that all operations in a transaction complete or none do?  
a) Atomicity  
b) Isolation  
c) Durability  
d) Consistency  

Q24. In C++, which keyword enables dynamic runtime method dispatch?  
a) `static`  
b) `virtual`  
c) `friend`  
d) `inline`  

---

## Section 4: Pseudocode Tracing (Questions 25–32)

Q25. Trace output:
```text
Integer a, b
Set a = 5, b = 3
a = a ^ b
b = a ^ b
a = a ^ b
Print a
```
a) 5  
b) 3  
c) 8  
d) 0  

Q26. Trace output:
```text
Integer i, sum = 0
For (each i from 1 to 4)
    sum = sum + i * i
End For
Print sum
```
a) 30  
b) 20  
c) 16  
d) 10  

Q27. Trace recursive `f(3)`:
```text
Function f(Integer n)
    If (n <= 1) Return 1
    Return n * f(n - 1)
End Function
```
a) 6  
b) 3  
c) 9  
d) 1  

Q28. Trace output:
```text
Integer A[3] = {10, 20, 30}
Print A[0] + A[2]
```
a) 40  
b) 30  
c) 50  
d) 20  

Q29. What symbol in a flowchart represents an Input/Output operation?  
a) Rectangle  
b) Parallelogram  
c) Diamond  
d) Oval  

Q30. Trace loop:
```text
Integer count = 0, i
For (each i from 1 to 10)
    If (i mod 2 == 0)
        count = count + 1
    End If
End For
Print count
```
a) 4  
b) 5  
c) 6  
d) 10  

Q31. Trace bitwise AND:
```text
Integer x = 6, y = 3
Print (x & y)
```
(Binary: `110 & 011`)  
a) 2  
b) 3  
c) 7  
d) 0  

Q32. Trace loop:
```text
Integer a = 10
While (a > 4)
    a = a - 3
End While
Print a
```
a) 4  
b) 1  
c) 3  
d) 7  

---

## Section 5: Cloud, Security & MS Office (Questions 33–40)

Q33. Which cloud model provides raw virtual machines and storage?  
a) SaaS  
b) PaaS  
c) IaaS  
d) FaaS  

Q34. What type of encryption uses a single shared secret key?  
a) Asymmetric  
b) Symmetric  
c) Hashing  
d) PKI  

Q35. What is the Excel formula function for looking up values in a table's first column?  
a) `COUNTIF`  
b) `VLOOKUP`  
c) `SUMIF`  
d) `AVERAGE`  

Q36. What does `$A$1` mean in Excel?  
a) Currency  
b) Absolute Cell Reference  
c) Text  
d) Function  

Q37. Which cyber attack floods a server with traffic from a botnet?  
a) Phishing  
b) DDoS  
c) SQL Injection  
d) Trojan  

Q38. In MS Word, what feature allows generating multiple personalized letters from an Excel list?  
a) Track Changes  
b) Mail Merge  
c) Slide Master  
d) Watermark  

Q39. What is the process of verifying a user's password called?  
a) Authorization  
b) Authentication  
c) Encryption  
d) Hashing  

Q40. In MS PowerPoint, what master view sets default fonts and layouts across all slides?  
a) Slide Master  
b) Animation Pane  
c) Outline View  
d) Notes Master  
