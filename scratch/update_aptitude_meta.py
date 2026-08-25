import os

additions = {
    '01-aptitude/quantitative/percentages-profit-loss.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Percentages, Profit & Loss Cheat-Sheet
> - **Percentage Value**: $\\text{Part} / \\text{Whole} \\times 100$.
> - **Multiplier Method**: 20% gain $\\rightarrow \\times 1.20$; 15% loss $\\rightarrow \\times 0.85$.
> - **Net Successive Change**: $a + b + \\frac{ab}{100}\\%$.
> - **Profit / Loss %**: Calculated strictly on **Cost Price (CP)** unless specified otherwise.
> - **Discount %**: Calculated strictly on **Marked Price (MP)**.
> - **Same SP, Same Profit% & Loss%**: Always net loss of $\\frac{x^2}{100}\\%$.
> - **False Weight Profit %**: $\\frac{\\text{Error}}{\\text{True Weight} - \\text{Error}} \\times 100$.

---

## 9. Connection to Next Topic
Now that you have mastered percentages, markup, and discount multipliers, the next logical step is using ratios to compare quantities and analyze weighted averages. Continue to **[Ratios & Averages](ratios-averages.md)**!
""",

    '01-aptitude/quantitative/ratios-averages.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Ratios & Averages Cheat-Sheet
> - **Average**: $\\text{Sum of items} / N$.
> - **Weighted Average**: $(n_1 a_1 + n_2 a_2) / (n_1 + n_2)$.
> - **Deviation Method**: $\\text{Assumed Mean } A_0 + (\\sum \\text{Deviations} / N)$.
> - **Ratio Combining ($A:B$ & $B:C$)**: Scale $B$ to a common multiple baseline.
> - **Rule of Alligation**: $\\text{Cheaper Qty} / \\text{Dearer Qty} = (D - M) / (M - C)$.
> - **Repeated Replacement**: $Q_{\\text{final}} = Q_{\\text{initial}} \\left(1 - \\frac{x}{V}\\right)^n$.

---

## 9. Connection to Next Topic
With ratios and weighted averages mastered, apply these proportional reasoning techniques to solve speed, time, and distance problems. Continue to **[Time, Speed & Distance](time-speed-distance.md)**!
""",

    '01-aptitude/quantitative/time-speed-distance.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Time, Speed & Distance Cheat-Sheet
> - **Formula**: $D = S \\times T$.
> - **Unit Conversion**: $\\text{km/h} \\rightarrow \\text{m/s}$ (multiply by $5/18$); $\\text{m/s} \\rightarrow \\text{km/h}$ (multiply by $18/5$).
> - **Fixed Distance**: Speed ratio $S_1 : S_2$ is inversely proportional to time ratio $T_2 : T_1$.
> - **Average Speed (Equal Distances)**: $S_{\\text{avg}} = \\frac{2xy}{x + y}$.
> - **Relative Speed**: Opposite directions $\\rightarrow S_1 + S_2$; Same direction $\\rightarrow |S_1 - S_2|$.
> - **Train Crossing Platform**: Total distance = Length of train + Length of platform.
> - **Boats**: Downstream $D_s = u + v$; Upstream $U_s = u - v$.

---

## 9. Connection to Next Topic
Great job completing Quantitative Aptitude! Next, transition to Logical Reasoning starting with letter patterns and positional coding. Continue to **[Coding & Decoding](../logical-reasoning/coding-decoding.md)**!
""",

    '01-aptitude/logical-reasoning/coding-decoding.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Coding & Decoding Cheat-Sheet
> - **EJOTY Anchors**: $E=5, J=10, O=15, T=20, Y=25$.
> - **CFILORUX Anchors**: Multiples of 3 ($3, 6, 9, 12, 15, 18, 21, 24$).
> - **Opposite Letters**: Positional sum $= 27$ (e.g., $A(1) + Z(26) = 27, B(2) + Y(25) = 27$).
> - **Shifting**: Track $+N / -N$ patterns above each letter.
> - **Option Elimination**: Check code of 1st and last letter first to eliminate options instantly.
> - **Coded Messages**: Find overlapping common words across 2+ statements.

---

## 9. Connection to Next Topic
Having mastered letter patterns and positional logic, apply tree structures and logical deduction to family relations. Continue to **[Blood Relations](blood-relations.md)**!
""",

    '01-aptitude/logical-reasoning/blood-relations.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Blood Relations Cheat-Sheet
> - **Notations**: Square/Plus $[+]$ = Male; Circle/Minus $(-)$ = Female; $=$ Married; $-$ Siblings; $\\mid$ Parent-Child.
> - **Generation Gaps**: Grandparent $= +2$, Parent/Uncle $= +1$, Self/Sibling $= 0$, Child $= -1$.
> - **Self-Substitution**: Read quotes from "my/his/her" outwards to deduce relations mentally.
> - **Rule**: Never assume gender from names; establish gender strictly via relationship terms or pronouns.

---

## 9. Connection to Next Topic
Now that you can trace family tree structures logically, build spatial orientation skills for linear and circular setups. Continue to **[Seating Arrangement](seating-arrangement.md)**!
""",

    '01-aptitude/logical-reasoning/seating-arrangement.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Seating Arrangement Cheat-Sheet
> - **North Facing**: Left $= \\leftarrow$, Right $= \\rightarrow$.
> - **South Facing**: Left $= \\rightarrow$, Right $= \\leftarrow$.
> - **Center Facing Circle**: Left = Clockwise; Right = Counter-Clockwise (Anticlockwise).
> - **Outward Facing Circle**: Left = Counter-Clockwise; Right = Clockwise.
> - **Opposite Seat in Circle ($N=8$)**: Opposite position of seat $k$ is seat $k + 4$.
> - **Strategy**: Start strictly with definite clues; draw 2 parallel case diagrams for ambiguous statements.

---

## 9. Connection to Next Topic
Logical Reasoning complete! Next, move to Verbal Ability to practice reading comprehension, speed skimming, and tone detection. Continue to **[Reading Comprehension](../verbal/reading-comprehension.md)**!
""",

    '01-aptitude/verbal/reading-comprehension.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Reading Comprehension Cheat-Sheet
> - **Question-First Strategy**: Read question stems first to pre-program keyword targets.
> - **Paragraph Anchors**: 80% of core ideas reside in the 1st and last sentences of each paragraph.
> - **Tone Filter**: Classify tone as Positive (+), Negative (-), or Neutral (0).
> - **Extreme Word Trap**: Options with *always, never, completely, impossible, all* are wrong 90% of the time.
> - **Inference Rule**: Infer strictly from facts inside the text—do NOT bring outside knowledge.

---

## 9. Connection to Next Topic
Now that you can skim passages and extract main themes, learn how to reorder jumbled sentences using transition words and mandatory pairs. Continue to **[Para Jumbles](para-jumbles.md)**!
""",

    '01-aptitude/verbal/para-jumbles.md': """

---

## 8. Quick Revision

> [!TIP]
> ### 🚀 Para Jumbles Cheat-Sheet
> - **Opening Sentence**: Standalone noun introduction; never starts with pronouns (*He, She, They, This*) or conjunctions (*However, Therefore*).
> - **Noun-Pronoun Precedence**: Full name/Noun MUST precede its Pronoun.
> - **Acronym Precedence**: Full title comes before acronym (e.g., NASA).
> - **Mandatory Pairs**: Linked by transition words (*However, Consequently, In addition*).
> - **Option Elimination**: Test mandatory pairs directly against the given 4 options.

---

## 9. Connection to Next Topic
Congratulations on completing the entire 01-Aptitude Module! You are ready to move to **Track 2: Technical & Coding Preparation**. Start with **[OOP Concepts](../../02-technical-coding/cs-fundamentals/oop-concepts.md)**!
"""
}

for path, addition in additions.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '## 8. Quick Revision' not in content:
        content += addition
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {path}')
    else:
        print(f'Already has Quick Revision: {path}')
