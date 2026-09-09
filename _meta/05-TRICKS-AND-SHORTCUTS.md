# 05-TRICKS-AND-SHORTCUTS.md — Inject These Into the Matching Topic Files

Each entry: the shortcut + why it works (Antigravity should explain the "why," not just state the rule, per 03-REQUIREMENTS.md).

## Gamified round
- **Memory Maze**: Don't try to memorize the full grid. Lock onto three reference points only — start cell, key cell, door cell — and trace the shortest wall-free route between them during the memorize phase. Why: working memory holds ~3-4 chunks reliably under time pressure; a full grid is too many.
- **Path Finder**: Solve from the End tile backward. Why: end tiles usually have fewer valid rotations than start tiles, so backward search prunes the possibility space faster.
- **Quick-Fire Math (bubble ordering)**: Round each expression to the nearest 10/100 first to eliminate 1-2 obviously smaller/larger bubbles before doing exact math on the remaining close ones. Why: full precision is only needed for the tie-breaking pair, not all bubbles.

## Quantitative Aptitude
- Percentage↔fraction lookup table (12.5%=1/8, 16.67%=1/6, 20%=1/5, 25%=1/4, 33.33%=1/3, 37.5%=3/8, 66.67%=2/3, 62.5%=5/8) — convert percentage problems to fraction arithmetic, which is faster mentally than decimal multiplication.
- Successive percentage change: combine as a + b + ab/100 instead of computing sequentially — one formula instead of two multiplication steps.
- Time-Speed-Distance: convert km/h to m/s by multiplying by 5/18 as a single reflex step, not a separate unit-conversion detour.

## Logical Reasoning
- Blood relations: draw a genogram (family tree) as you read, don't hold relations in your head — reduces error rate on multi-step relation chains.
- Coding-Decoding: check letter-shift patterns first (each letter +/-N), then check reversal patterns, then check position-based patterns — in that fixed order, so you don't waste time guessing randomly.
- Seating arrangement: mark fixed positions first, then place conditional ("X is not next to Y") constraints last, since fixed clues eliminate more possibilities per clue than negative/conditional clues.

## Abstract / Visual Reasoning
- Series completion: check for one transformation rule at a time in this order — rotation, then reflection, then element addition/deletion, then shading change. Why: most series use exactly one transformation type; checking in a fixed order avoids overthinking multiple rules simultaneously.

## Data Interpretation
- For "what % more/less" questions, compute the raw difference first, then divide by the smaller/base value — don't compute both percentages separately and subtract, which is slower and error-prone.
- For pie charts, memorize common angle-to-percentage anchors (90°=25%, 180°=50%, 36°=10%) to eyeball-estimate before calculating exactly.

## Pseudocode
- Always build a trace table (columns = variable names, rows = each loop iteration) before choosing an answer — never trace pseudocode "in your head" under time pressure, it's the single biggest source of silly mistakes.
- For nested loops, trace the outer loop's variable value in the margin first, then trace the inner loop fully for just that one outer value — don't try to track both loops simultaneously.

## Coding Round
- For array/string problems, always state brute force first (even mentally) — it confirms you understand the problem correctly before you optimize, and partial credit often exists for a correct-but-unoptimized solution.
- For SQL, write the FROM/JOIN clause first and confirm the resulting row set in your head before adding WHERE/GROUP BY — most SQL mistakes come from filtering before you've confirmed the join is correct.

## Communication Assessment
- Reading section: use punctuation as your pause map — comma = short pause, full stop = longer pause + pitch drop. This is literally what the AI grader scores on pacing, so treat punctuation as stage directions, not decoration.
- Repeat Sentence: don't try to memorize word-for-word while still listening — instead, extract the sentence's "shape" (subject–verb–object + key numbers/nouns) as you hear it, then reconstruct. Why: verbatim rote memory fails past ~7-9 words, but structural reconstruction scales to longer sentences.
- Story Retelling: mentally tag 4 anchors while listening — who, what happened, where/when, outcome — then speak from those four anchors rather than trying to recall exact phrasing.
- Open/Spontaneous Speech: use a 3-sentence structure under time pressure — (1) direct answer, (2) one supporting reason/example, (3) one-line wrap-up. Why: this guarantees a complete, well-paced answer within the 20-30s window without rambling or running out of time mid-thought.
