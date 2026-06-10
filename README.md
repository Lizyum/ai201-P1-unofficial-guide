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

See planning.md

**Overlap:**

See planning.md

**Why these choices fit your documents:**

Before chunking, webpages were processed to remove HTML elements such as scripts, navigation menus, footers, and styling information. Reddit threads and YouTube transcripts were converted into structured markdown files with metadata headers describing the source, organization, URL, and topics. Documents were then split along markdown section boundaries before token-based chunking was applied. This approach helped preserve semantic coherence while reducing the likelihood that stories, discussions, or resource descriptions would be fragmented across unrelated chunks. The chunk sizes and overlaps were also selected to accommodate the embedding model's token limit while maintaining sufficient context for retrieval.

**Final chunk count:**

350 chunks

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
Look at planning.md

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

The system enforces grounding through a system prompt that instructs the model to answer using only the retrieved documents. The prompt explicitly states: "You must answer using ONLY the provided retrieved documents. Do not use outside knowledge. Do not invent resources, policies, offices, deadlines, or experiences." Additionally, the prompt instructs the model to respond with "I don't have enough information on that from the provided documents" whenever the retrieved context is insufficient. Retrieved chunks are formatted into labeled source blocks and passed directly into the prompt, ensuring that the model has access only to information returned by the retrieval stage.

**How source attribution is surfaced in the response:**
Source attribution is generated programmatically rather than relying on the model to cite sources correctly. After retrieval, metadata associated with each chunk—including the document title, organization, and URL—is extracted and formatted into a source list. This list is appended to every generated answer, allowing users to see which documents informed the response. Because the sources are attached outside of the model's generated text, attribution remains accurate even if the model fails to reference sources explicitly in its answer.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What are some common experiences as a FGLI at Northwestern University?| Discusses common challenges such as belonging, financial concerns, academic adjustment, and finding community.| The system accurately identified common FGLI experiences at Northwestern, including financial challenges, feelings of isolation, and difficulty relating to peers from different socioeconomic backgrounds. It also surfaced relevant support resources and communities, such as SES, FGLI Friday, and QUEST+, demonstrating its ability to combine personal experiences with actionable campus resources.| Relevant | Accurate |
| 2 | Where can I find my community at Northwestern as a FGLI student?| Recommends FGLI-focused organizations, affinity groups, and campus communities where students can build connections.| The system successfully identified multiple avenues for building community as an FGLI student, including SES, FGLI Friday, and QUEST+. It also incorporated advice from student experiences, emphasizing involvement in clubs and organizations, demonstrating its ability to retrieve both official resources and peer perspectives relevant to the user's question.| Relevant | Accurate |
| 3 | How can I tackle my imposter syndrome at Northwestern University?| Acknowledges imposter syndrome as a common experience and points students toward supportive communities and campus resources.| The system partially answered the question by identifying imposter syndrome as a common experience among FGLI students and retrieving relevant anecdotes about belonging and self-doubt. However, because the knowledge base contained limited information on concrete strategies for overcoming imposter syndrome, the response relied heavily on inference and generalized advice rather than providing actionable guidance. This highlights the system's ability to recognize when supporting evidence is sparse, but also reveals a gap in the current document collection for mental health and personal development topics.| Relevant | Partially Accurate |
| 4 | What resources exist specifically for FGLI students at Northwestern University?| Identifies relevant FGLI-focused programs, offices, organizations, and support services available to students.| The system accurately identified several FGLI-specific resources, including Student Enrichment Services (SES), FGLI Friday, and QUEST+, and correctly described the types of support they provide. The response was highly relevant to the query and demonstrated the system's ability to retrieve concrete, actionable resources from multiple sources. However, it could be improved by surfacing a broader range of university services if additional resource-focused documents were included in the knowledge base. | Relevant | Accurate|
| 5 | How can I learn more about the FGLI experience at Northwestern University?| Provides actionable ways to learn from current students, campus organizations, and university resources.| The system provided a comprehensive answer by combining multiple source types, including student blogs, resource pages, and student organizations. It successfully directed users to both informational resources and opportunities to engage with the FGLI community, demonstrating strong retrieval across diverse document formats. | Relevant | Accurate |

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

How can I tackle my imposter syndrome at Northwestern University?

**What the system returned:**

The system retrieved relevant anecdotes about FGLI students experiencing imposter syndrome, self-doubt, and difficulty feeling like they belong at Northwestern. However, the final answer did not provide many concrete strategies for addressing imposter syndrome. Instead, it gave general suggestions such as seeking community support, acknowledging feelings, and focusing on strengths.

**Root cause (tied to a specific pipeline stage):**

This issue appears to come from the **document collection and retrieval stages**. The knowledge base includes personal stories that mention imposter syndrome, but it does not contain enough documents with actionable guidance on how students can manage it. As a result, retrieval returned emotionally relevant chunks but not strategy-focused chunks. The generation step then had to infer possible advice from limited context, which made the response only partially accurate and less actionable.

**What you would change to fix it:**

I would add more source documents focused on mental health, belonging, and coping strategies for FGLI students, such as Counseling and Psychological Services resources, peer mentorship materials, or student reflections that specifically discuss how they handled imposter syndrome. I would also add topic metadata like `imposter_syndrome`, `mental_health`, and `belonging` so retrieval can better surface chunks that contain both the experience and concrete advice.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The specification helped me visualize the role and importance of each stage of the RAG pipeline before I began coding. Because I understood how data should flow through ingestion, chunking, embedding, retrieval, and generation, I was able to better evaluate the code produced by AI tools and identify when functionality was missing or implemented incorrectly. It also helped me understand where specific logic should reside within the pipeline, making debugging and iteration much more efficient.

**One way your implementation diverged from the spec, and why:**
My implementation diverged from the spec primarily in the organization of the project's folder structure and scripts. As I built the system, I learned the value of separating responsibilities across ingestion, processing, chunking, embedding, retrieval, and generation modules rather than grouping functionality together. This evolved structure made the pipeline easier to maintain, test, and extend as I added support for multiple source types such as websites, Reddit threads, and YouTube transcripts.

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

- *What I gave the AI:* I provided my planned chunking strategy, including the different chunk sizes and overlap values for long-form transcripts, official Northwestern resource pages, and Reddit threads. I also explained that I was using the all-MiniLM-L6-v2 embedding model, which has a 256-token input limit.

- *What it produced:* The AI generated a chunk_documents.py script that extracted metadata from processed markdown files, split documents into sections, applied token-based chunking, and generated chunk objects with metadata for later embedding.

- *What I changed or overrode:* I modified the chunking configuration to use source-specific chunk sizes and overlap values rather than a single chunk size for all documents. I also adjusted the strategy to preserve semantic sections before chunking and ensured chunk sizes stayed below the embedding model's token limit to avoid truncation.

**Instance 2**

- *What I gave the AI:* I provided the structure of my document sources, including websites, YouTube transcripts, and Reddit threads, along with my desired raw and processed document directories. I asked the AI to help implement reusable ingestion and processing functions for each source type.

- *What it produced:* The AI generated ingestion scripts for downloading webpages, processing HTML into markdown, extracting YouTube transcripts, and converting Reddit JSON data into structured markdown documents with metadata.

- *What I changed or overrode:* I redesigned the file organization to separate raw documents from processed documents and ensured metadata was transferred during the processing stage rather than stored directly in raw files. I also refined the HTML cleaning logic to remove residual website elements and improve the quality of the text that would later be chunked and embedded.
