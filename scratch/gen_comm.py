import os

os.makedirs('03-communication', exist_ok=True)

# 1. README.md
readme_content = """# Communication & Verbal Assessment Index

Mastering spoken English, grammar rules, vocabulary, and confident articulation is critical for both the automated **Accenture Communication Assessment** (Versant format) and the **HR / Technical Interview round**.

## Recommended Daily 15-Minute Practice Routine

To build natural fluency, vocal clarity, and error-free grammar, dedicate **15 minutes daily** following this structured split:

1. **Minutes 0–5 (Spoken Fluency & Recorders)**:
   - Pick one script from `self-intro-script.md` or `project-summary-script.md`.
   - Record yourself on your phone or computer.
   - Listen back immediately and check against the self-recording review checklist.
2. **Minutes 5–10 (Grammar & Sentence Construction)**:
   - Review 1 rule section in `grammar-vocab-notes.md` (Tenses, Subject-Verb Agreement, Prepositions, or Vocab).
   - Solve the 3 inline practice questions to reinforce usage rules.
3. **Minutes 10–15 (Log & Refine)**:
   - Note down filler words, pacing errors, or pronunciation stumbles in `recorded-practice-log.md`.
   - Re-record the same 60-second snippet once to fix the identified issue.

---

## Communication Folder Checklist

- [ ] [Grammar & Vocabulary Notes](grammar-vocab-notes.md) — Placement English rules, definitions, examples, and practice questions.
- [ ] [Self-Introduction Script Template](self-intro-script.md) — 60–90 second natural intro template with delivery tips and self-recording checklist.
- [ ] [Project Summary Script Framework](project-summary-script.md) — 5-stage framework (Problem → Role → Tech Stack → Challenge → Result) with a fully written example.
- [ ] [Recorded Practice Log](recorded-practice-log.md) — Ready-to-use tracking table for vocal practice sessions.
"""

with open('03-communication/README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

# 2. grammar-vocab-notes.md
grammar_content = """# Grammar & Vocabulary Notes — Accenture Placement Special

This guide covers the core grammar rules, prepositions, subject-verb agreement principles, and high-frequency vocabulary sets tested in Accenture placement English tests and HR interviews.

---

## 1. Tenses (Core Placement Rules)

### Rule 1: Present Perfect vs. Simple Past
- **Definition**: Use **Simple Past** for actions completed at a specific time in the past (e.g., *yesterday, in 2022, last week*). Use **Present Perfect** for actions completed at an unspecified time or past actions that have a direct connection/impact on the present moment.
- **Example 1 (Correct)**: *I submitted the project yesterday.* (Specific past time: 'yesterday' $\implies$ Simple Past).
- **Example 2 (Correct)**: *I have already submitted three pull requests this week.* (Unspecified time / ongoing relevance $\implies$ Present Perfect).
- **Practice Questions**:
  1. *Choose the correct option*: "She (has completed / completed) her graduation in 2024 from LPU."
  2. *Identify the error*: "I have seen that movie yesterday evening."
  3. *Fill in the blank*: "We __________ (work) on this full-stack application since last month."
- **Answers**:
  1. **completed** (because "in 2024" specifies exact past time).
  2. Change "have seen" to **saw** ("yesterday evening" specifies past time).
  3. **have been working** (action started in past and continues into present).

### Rule 2: Past Perfect Usage (Two Past Actions)
- **Definition**: When two actions happened in the past, the action that occurred **FIRST** takes the **Past Perfect** tense (*had + V3*), while the action that occurred **SECOND** takes the **Simple Past** tense (*V2*).
- **Example 1 (Correct)**: *The meeting had already started before I joined the call.* (First: meeting started; Second: I joined).
- **Example 2 (Correct)**: *By the time the server crashed, the database administrator had backed up all files.*
- **Practice Questions**:
  1. *Choose the correct option*: "When the interviewer arrived, Ravi (already reviewed / had already reviewed) the system design concepts."
  2. *Fill in the blank*: "The train __________ (leave) the station before we reached the platform."
  3. *Correct the sentence*: "I had finished my assignment when my friend came to meet me."
- **Answers**:
  1. **had already reviewed** (First action).
  2. **had left** (First action).
  3. Correct as written (First action: had finished; Second action: came).

---

## 2. Prepositions (Placement High-Frequency Rules)

### Rule 3: Fixed Prepositions with Key Verbs/Adjectives
- **Definition**: Certain verbs and adjectives must be followed by specific prepositions regardless of general translation rules.
  - *Discuss* / *Describe* / *Emphasize* $\rightarrow$ **No preposition** (Do NOT say "discuss about").
  - *Congratulate* $\rightarrow$ **on** (not "for").
  - *Comply* $\rightarrow$ **with** (not "to").
  - *Prevent* / *Abstain* / *Refrain* $\rightarrow$ **from**.
  - *Proficient* / *Adept* $\rightarrow$ **in**.
- **Example 1 (Correct)**: *We discussed the database architecture for two hours.* (Not "discussed about").
- **Example 2 (Correct)**: *The manager congratulated Ravi on winning the hackathon.* (Not "for winning").
- **Practice Questions**:
  1. *Spot the error*: "The team lead emphasized on the importance of code reviews."
  2. *Fill in the blank*: "Developers must comply __________ the security standards specified in the guidelines."
  3. *Choose the correct option*: "Ravi is highly proficient (in / at / with) developing RESTful APIs using Node.js."
- **Answers**:
  1. Remove "on" (Emphasize takes no preposition: "emphasized the importance").
  2. **with** ("comply with").
  3. **in** ("proficient in").

### Rule 4: Prepositions of Time and Location (In, On, At)
- **Definition**:
  - **At**: Specific precise time (*at 5:00 PM, at noon*) or specific point location (*at the entrance, at the desk*).
  - **On**: Specific days/dates (*on Monday, on 15th August*) or surface (*on the table, on the screen*).
  - **In**: Enclosed spaces (*in the room, in India*), months, years, seasons (*in August, in 2026, in summer*).
- **Example 1 (Correct)**: *The technical interview is scheduled at 10:30 AM on Tuesday.*
- **Example 2 (Correct)**: *The campus drive will take place in September at the main auditorium.*
- **Practice Questions**:
  1. *Fill in the blank*: "The online coding test starts __________ 3:00 PM __________ Sunday."
  2. *Spot the error*: "I will complete my B.Tech graduation on 2026."
  3. *Choose the correct option*: "The speaker was standing (at / on / in) the stage during the seminar."
- **Answers**:
  1. **at** 3:00 PM **on** Sunday.
  2. Change "on 2026" to **in 2026** (Years take 'in').
  3. **on** the stage.

---

## 3. Subject-Verb Agreement

### Rule 5: Singular vs. Plural Subject Connectors
- **Definition**:
  - When subjects are joined by *and*, use a **plural verb**.
  - When subjects are joined by *either...or*, *neither...nor*, or *not only...but also*, the verb agrees with the **closest subject** (the subject nearest to the verb).
- **Example 1 (Correct)**: *Neither the team lead nor the developers were aware of the bug.* ("developers" is closest $\implies$ plural verb 'were').
- **Example 2 (Correct)**: *Neither the developers nor the team lead was present at the standup.* ("team lead" is closest $\implies$ singular verb 'was').
- **Practice Questions**:
  1. *Choose the correct option*: "Either the project manager or the software engineers (is / are) responsible for updating the backlog."
  2. *Spot the error*: "Neither the server logs nor the database error report were generated."
  3. *Fill in the blank*: "Not only the students but also the professor __________ (be) present at the workshop."
- **Answers**:
  1. **are** (closest subject "software engineers" is plural).
  2. Change "were" to **was** ("database error report" is singular).
  3. **was** (closest subject "the professor" is singular).

### Rule 6: Indefinite Pronouns & Collective Nouns
- **Definition**: Indefinite pronouns such as *Each, Every, Everyone, Someone, Nobody, Either of, Neither of* take a **singular verb**. Collective nouns (*team, committee, jury*) take a **singular verb** when acting as a unified unit.
- **Example 1 (Correct)**: *Each of the applicants has received an interview invite.* (Not "have received").
- **Example 2 (Correct)**: *The development team is working on the new release.* (Unified unit $\implies$ singular).
- **Practice Questions**:
  1. *Choose the correct option*: "Every student and teacher (was / were) asked to submit feedback."
  2. *Fill in the blank*: "Neither of the two solutions __________ (be) optimal in terms of space complexity."
  3. *Spot the error*: "Each of the candidate have 15 minutes for the self-introduction."
- **Answers**:
  1. **was** ("Every" makes the subject singular).
  2. **is** ("Neither of" takes a singular verb).
  3. Change "have" to **has** and "candidate" to **candidates** ("Each of the candidate**s** **has**").

---

## 4. Placement High-Frequency Synonym & Antonym Sets

Master these top 5 word sets frequently appearing in Accenture verbal ability tests:

### Set 1: Meticulous
- **Definition**: Showing great attention to detail; careful and precise.
- **Synonyms**: Scrupulous, Fastidious, Painstaking, Thorough.
- **Antonyms**: Careless, Sloppy, Negligent, Hasty.
- **Usage Example**: *As a full-stack developer, Ravi is meticulous about writing clean, modular code.*
- **Practice Questions**:
  1. *Synonym of Meticulous*: (a) Lazy (b) Painstaking (c) Arrogant (d) Swift $\implies$ **(b)**
  2. *Antonym of Meticulous*: (a) Detailed (b) Precise (c) Negligent (d) Accurate $\implies$ **(c)**
  3. *Fill in*: "He performed a __________ review of the API security protocols." $\implies$ **meticulous**

### Set 2: Candid
- **Definition**: Truthful, straightforward, and frank in speech or expression.
- **Synonyms**: Frank, Forthright, Honest, Direct.
- **Antonyms**: Deceitful, Evasive, Disingenuous, Guarded.
- **Usage Example**: *The candidate gave a candid answer about his mistake during the internship.*
- **Practice Questions**:
  1. *Synonym of Candid*: (a) Secretive (b) Frank (c) Complex (d) Rude $\implies$ **(b)**
  2. *Antonym of Candid*: (a) Evasive (b) Sincere (c) Open (d) Blunt $\implies$ **(a)**
  3. *Fill in*: "The team lead appreciated his __________ feedback during the retrospective." $\implies$ **candid**

### Set 3: Pragmatic
- **Definition**: Dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.
- **Synonyms**: Practical, Realistic, Utilitarian, Sensible.
- **Antonyms**: Idealistic, Impractical, Theoretical, Visionary.
- **Usage Example**: *Taking a pragmatic approach, the team chose PostgreSQL over a complex graph database to meet the tight deadline.*
- **Practice Questions**:
  1. *Synonym of Pragmatic*: (a) Emotional (b) Practical (c) Theoretical (d) Slow $\implies$ **(b)**
  2. *Antonym of Pragmatic*: (a) Sensible (b) Functional (c) Impractical (d) Grounded $\implies$ **(c)**
  3. *Fill in*: "Instead of over-engineering, we took a __________ decision to use built-in libraries." $\implies$ **pragmatic**

### Set 4: Mitigate
- **Definition**: To make less severe, serious, or painful; to lessen the impact of a problem.
- **Synonyms**: Alleviate, Reduce, Diminish, Attenuate, Ease.
- **Antonyms**: Aggravate, Exacerbate, Intensify, Increase.
- **Usage Example**: *Implementing caching helped mitigate database latency during peak traffic.*
- **Practice Questions**:
  1. *Synonym of Mitigate*: (a) Intensify (b) Alleviate (c) Ignore (d) Delay $\implies$ **(b)**
  2. *Antonym of Mitigate*: (a) Exacerbate (b) Lessen (c) Soothe (d) Moderate $\implies$ **(a)**
  3. *Fill in*: "We used rate limiting to __________ the risk of DDoS attacks." $\implies$ **mitigate**

### Set 5: Eloquent
- **Definition**: Fluent, persuasive, and expressive in speaking or writing.
- **Synonyms**: Articulate, Fluent, Expressive, Persuasive.
- **Antonyms**: Inarticulate, Tongue-tied, Hesitant, Unpersuasive.
- **Usage Example**: *Her eloquent presentation of the project architecture impressed the interview panel.*
- **Practice Questions**:
  1. *Synonym of Eloquent*: (a) Silent (b) Articulate (c) Confused (d) Harsh $\implies$ **(b)**
  2. *Antonym of Eloquent*: (a) Persuasive (b) Fluent (c) Inarticulate (d) Vivid $\implies$ **(c)**
  3. *Fill in*: "He gave an __________ explanation of how the microservices communicate." $\implies$ **eloquent**
"""

with open('03-communication/grammar-vocab-notes.md', 'w', encoding='utf-8') as f:
    f.write(grammar_content)

# 3. self-intro-script.md
self_intro_content = """# Self-Introduction Script & Delivery Guide

A structured, natural, and confident self-introduction creates an immediate strong first impression during HR and technical interviews.

---

## 1. Complete Self-Introduction Template (60–90 Seconds)

*(Personalize the text inside the square brackets `[ ]` before practicing)*

> "Good morning/afternoon, Sir/Ma'am. Thank you for giving me this opportunity to introduce myself.
>
> My name is **[Ravi Ranjan]**, and I am currently pursuing my final year B.Tech in Computer Science and Engineering at **[Lovely Professional University (LPU)]** with a CGPA of **[8.X / Current CGPA]**.
>
> Over the course of my degree, I have developed a strong foundation in core CS fundamentals—including Data Structures, Algorithms, OOPs, and DBMS—with a primary specialization in **[Full-Stack Web Development and AI-ML integration]**.
>
> To apply my learning practically, I have built impactful projects such as **[Bhookly, a real-time food ordering platform]** and **[PrepGenius, an AI-powered interview preparation assistant]**. These experiences allowed me to work with modern technologies like **[React, Node.js, Express, MongoDB, and Python]** while implementing robust RESTful APIs and clean architecture.
>
> Beyond technical skills, I actively participate in coding hackathons and technical clubs at college, which has enhanced my problem-solving speed, teamwork, and adaptability under pressure.
>
> I am particularly drawn to **[Accenture]** because of its strong innovation culture, commitment to digital transformation, and emphasis on continuous learning. I am eager to start my career as a Software Engineer where I can contribute to real-world client solutions while continuing to grow professionally.
>
> Thank you!"

---

## 2. 3 Key Delivery Tips for Placement Interviews

### Tip 1: Pacing (Target 120–140 Words Per Minute)
- **Why it matters**: Speaking too fast makes you sound anxious and difficult to follow; speaking too slowly sounds unprepared or disinterested.
- **Actionable Technique**: Insert intentional 1-second pauses after major sentences (e.g., after your name, after your university, and after your project overview). Pauses give your words weight and allow the panelist to absorb information.

### Tip 2: Vocal Tone & Energy (Warm, Confident, Professional)
- **Why it matters**: Monotone delivery kills engagement even if your script is perfect.
- **Actionable Technique**: Smile slightly at the beginning ("Good morning...") to naturally warm up your voice. Modulate your pitch upwards slightly when mentioning your projects and key skills to show genuine enthusiasm.

### Tip 3: Eliminating Filler Words ("Um", "Ah", "Like", "Basically")
- **Why it matters**: Overusing filler words interrupts speech flow and reduces perceived technical confidence.
- **Actionable Technique**: Replace filler words with **silent pauses**. When your brain needs time to recall the next point, pause silently for 1 second instead of making an "ummm" sound. Silent pauses sound deliberate and authoritative.

---

## 3. Self-Recording Review Checklist

Record your self-introduction video/audio on your phone and evaluate it against these 6 parameters before your actual mock interviews:

| # | Check Parameter | Target Standard | Self-Pass? (YES/NO) |
| :--- | :--- | :--- | :--- |
| 1 | **Total Duration** | Strictly between 60 to 90 seconds. | [ ] |
| 2 | **Filler Word Count** | Less than 2 filler words ("um", "uh", "basically") per 60 seconds. | [ ] |
| 3 | **Eye Contact / Camera Position** | Looking directly at camera lens (or interviewer's eyes), not reading from a screen. | [ ] |
| 4 | **Pacing & Clarity** | Clear pronunciation of technical terms (e.g., "Node.js", "Algorithms", "MongoDB"). | [ ] |
| 5 | **Posture & Body Language** | Upright spine, shoulders relaxed, slight natural head gestures, open posture. | [ ] |
| 6 | **Closing Statement** | Clear, courteous closing ("Thank you!") with a professional smile. | [ ] |
"""

with open('03-communication/self-intro-script.md', 'w', encoding='utf-8') as f:
    f.write(self_intro_content)

# 4. project-summary-script.md
project_script_content = """# Project Summary Script Framework

A structured, 90-second elevator pitch framework to explain any technical project clearly to both technical leads and HR panelists without getting bogged down in unnecessary implementation details.

---

## 1. The 5-Stage Framework (Problem $\rightarrow$ Role $\rightarrow$ Tech Stack $\rightarrow$ Challenge $\rightarrow$ Result)

Use this exact 5-step sequence whenever an interviewer asks: *"Tell me about your project"* or *"Explain your major project"*:

```
1. Problem Statement (15-20s)  → What real-world problem does this project solve?
2. My Role & Responsibility (10-15s) → What was your exact contribution (Solo / Lead / Backend)?
3. Tech Stack Used (10-15s)    → Which frontend, backend, database, and tools were chosen and why?
4. Key Challenge Overcome (20-25s) → What technical hurdle or bug did you encounter & solve?
5. Results & Impact (15-20s)   → What metrics, accuracy, user feedback, or learning was achieved?
```

---

## 2. Fully Written Example Project Pitch

Below is a complete, fully written 90-second example using a generic web application project (**"PrepGenius — AI Mock Interview System"**) demonstrating the 5-stage framework in action:

> **[1. Problem Statement — 20s]**
> "During campus placement prep, students often struggle to get personalized, instant feedback on their technical answers and communication skills without paying high fees for private mock interviewers. To solve this, I developed **PrepGenius**, a web-based AI mock interview platform that conducts automated technical rounds and evaluates answer quality."
>
> **[2. My Role — 10s]**
> "I served as the **Lead Full-Stack Developer** in a 3-member team, taking ownership of system architecture, REST API design, and OpenAI API integration."
>
> **[3. Tech Stack — 15s]**
> "We built the frontend using **React** and **Tailwind CSS** for a responsive user interface, the backend using **Node.js** and **Express**, **MongoDB** for database storage, and integrated the **OpenAI API** for automated speech-to-text evaluation."
>
> **[4. Key Challenge Overcome — 25s]**
> "A major technical challenge we faced was API latency: getting speech evaluations from LLM endpoints took upwards of 4 to 5 seconds per question, which disrupted the flow of a live interview. To overcome this, I implemented an asynchronous queue using **Redis** and optimistic UI updates on the frontend. This reduced user-perceived waiting time from 5 seconds to under 800 milliseconds."
>
> **[5. Results & Impact — 20s]**
> "As a result, PrepGenius was successfully deployed and tested by over 150 students in our college, completing 400+ automated mock interviews. It achieved an average user satisfaction rating of 4.6/5 and gave students immediate, actionable feedback to fix their weak technical areas."

---

## 3. Quick Customization Template for Your Projects

Fill out this outline for your own key projects (e.g., *Bhookly*, *Scrutin*) to ensure instant readiness during interview rounds:

- **Project Title**: `[Insert Name]`
- **Problem Statement (1-2 lines)**: `[What problem did it solve?]`
- **My Role**: `[Full-Stack Developer / Backend Lead / Solo Developer]`
- **Tech Stack**: `[Frontend / Backend / Database / APIs]`
- **Key Technical Challenge**: `[What broke or was slow? How did you fix it?]`
- **Measurable Result / Impact**: `[Users, accuracy %, response time reduction, or test coverage]`
"""

with open('03-communication/project-summary-script.md', 'w', encoding='utf-8') as f:
    f.write(project_script_content)

# 5. recorded-practice-log.md
log_content = """# Recorded Practice Log

Use this log to track your spoken English practice sessions (Self-Introduction, Project Summaries, Behavioral STAR answers). Regular self-recording and honest self-critique are the fastest ways to eliminate filler words, regulate speech tempo, and build interview confidence.

---

## Practice Log Table

| Date | What I Practiced | Self-Rating (1-5) | Issue Noticed | Fix for Next Time |
| :--- | :--- | :--- | :--- | :--- |
| 2026-08-21 | Self-Introduction (First Attempt) | ⭐⭐⭐ (3/5) | Spoke too fast (165 WPM); used "um" 6 times when describing tech stack. | Insert 1-second silent pause after mentioning university and skills; slow down pace. |
| 2026-08-24 | Project Summary — PrepGenius Pitch | ⭐⭐⭐⭐ (4/5) | Pronounced "asynchronous" unclearly; forgot to state specific user metric at the end. | Practice pronouncing technical terms clearly; end with explicit metric (150+ students). |
| YYYY-MM-DD | [Insert Script / Topic] | ⭐⭐⭐⭐⭐ (_/5) | [Note pacing, fillers, eye contact] | [Actionable correction for next recording] |
| YYYY-MM-DD | [Insert Script / Topic] | ⭐⭐⭐⭐⭐ (_/5) | [Note pacing, fillers, eye contact] | [Actionable correction for next recording] |
| YYYY-MM-DD | [Insert Script / Topic] | ⭐⭐⭐⭐⭐ (_/5) | [Note pacing, fillers, eye contact] | [Actionable correction for next recording] |
| YYYY-MM-DD | [Insert Script / Topic] | ⭐⭐⭐⭐⭐ (_/5) | [Note pacing, fillers, eye contact] | [Actionable correction for next recording] |
"""

with open('03-communication/recorded-practice-log.md', 'w', encoding='utf-8') as f:
    f.write(log_content)

print("All 03-communication files written successfully.")
