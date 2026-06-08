# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Domain: FGLI Student Experiences and Resources at Northwestern University 

Relevance: FGLI students face challenges that extend beyond academics, including financial barriers, limited access to professional networks, feelings of imposter syndrome, and difficulty navigating university resources. While Northwestern offers some official channels for support, information about these resources is distributed across multiple platforms and often lacks the lived experiences that help students understand how to use them effectively. This RAG system aims to aggregate official Northwestern resources alongside alumni and current student experiences to provide personalized, context-rich answers. By combining institutional knowledge with peer insights, the system can help FGLI students quickly identify proven strategies, discover relevant opportunities, and navigate Northwestern with greater confidence and belonging.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What are some common experiences as a FGLI at Northwestern University?| Some students reflect on challenges during the first year of college as they acclimate to their new environment. Some students struggle to find their community or may feel like they are not meant for the heavy courseload at the school.|
| 2 | Where can I find my community at Northwestern as a FGLI student?| Affinity-based clubs are a great place to start to connect with people with similar interests and backgrounds. Specific clubs: Society of Hispanic Professional Engineers, QuestBridge, etc.|
| 3 | How can I tackle my imposter syndrome at Northwestern University?| You are not the only one that experiences imposter syndrome during their schooling at Northwestern University. Previous student experiences consist of acknowledging the culture and environment shock that you may experience when you start at Northwestern. Tips for tackling that feeling: reaching out for support (through official channels or through the community you find at Northwestern). Some official sources of support include: Student Enrichment Services, Financial Aid Office, etc. |
| 4 | What resources exist specifically for FGLI students at Northwestern University?| Cited sources of recommended official resources and student recommended resources as shared from panels and blogs.|
| 5 | How can I learn more about the FGLI experience at Northwestern University?| Actionable suggestions, like: reach out to the SES office, attend club fairs to find the right club for you, connect with your advisor to point you in the direction of other resources|

* All responses should cite sources
---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
