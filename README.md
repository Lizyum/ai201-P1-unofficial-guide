# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
Domain: FGLI Student Experiences and Resources at Northwestern University 

Relevance: FGLI students face challenges that extend beyond academics, including financial barriers, limited access to professional networks, feelings of imposter syndrome, and difficulty navigating university resources. While Northwestern offers numerous support services, information about these resources is distributed across multiple platforms and often lacks the lived experiences that help students understand how to use them effectively. This RAG system aims to aggregate official Northwestern resources alongside alumni and current student experiences to provide personalized, context-rich answers. By combining institutional knowledge with peer insights, the system can help FGLI students quickly identify proven strategies, discover relevant opportunities, and navigate Northwestern with greater confidence and belonging.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Reddit |Thread| [Link to Post](https://www.reddit.com/r/evanston/comments/1min35y/where_to_go_to_get_the_northwestern_experience/)|
| 2 | The Daily Northwestern | News Source | [Link to Page](https://dailynorthwestern.com/2022/11/16/audio/digital-diaries-episode-7-life-as-a-first-generation-and-or-low-income-student/) |
| 3 | Office of Undergraduate Admission| Blog Post | [Link to Post](https://admissionblog.northwestern.edu/2022/11/08/advice-for-fgli-students-northwestern/)|
| 4 | Office of Undergraduate Admission| Blog Post|[Link to Post](https://admissionblog.northwestern.edu/2019/10/22/carter-finding-home-at-northwestern-as-a-first-gen-low-income-student/) |
| 5 | Northwestern Website | Web Page | [Link to Page](https://www.northwestern.edu/studentaffairs/sass/)|
| 6 | Reddit | Thread | [Link to Post](https://www.reddit.com/r/Northwestern/comments/1th3sjt/isolating_firstgen_experience/) |
| 7 | Northwestern Searle Center | Web Page | [Link to Page](https://searle.northwestern.edu/resources/learning-teaching-guides/first-generation-college-student-page.html)|
| 8 | North By Northwestern | Newsletter | [Link to Page](https://northbynorthwestern.com/discountedu-ep-6-intersectionality-latine-fgli/)|
| 9 | Youtube | FGLI Alumni Panel Transcript | [Link to Page](https://www.youtube.com/watch?v=rhX9eEovYug)|
| 10 | Youtube | FGLI Narratives | [Link to Page](https://www.youtube.com/watch?v=jWWHa5XdvDQ)|

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
