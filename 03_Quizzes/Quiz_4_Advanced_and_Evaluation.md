# Quiz 4: Advanced RAG & Evaluation Metrics
**After: Advanced Topics + Demo 4 & 5 (85 minutes into session)**

**Time Limit**: 6 minutes
**Questions**: 15 (Mix of Multiple Choice + Scenario-based)
**Difficulty**: 🔥 Challenge Level!

---

## PART A: Embedding Models vs LLMs

### Question 1
**What is the PRIMARY purpose of embedding models?**

A) Generate text responses
B) Convert text into vector representations for search
C) Train other models
D) Store documents

**Correct Answer**: B

---

### Question 2
**What is the PRIMARY purpose of LLMs in RAG?**

A) Create embeddings
B) Store documents
C) Generate answers using retrieved context
D) Search the vector database

**Correct Answer**: C

---

### Question 3
**Why use embedding models instead of LLMs for search?**

A) Embeddings are smarter
B) Embeddings are cheaper, faster, and designed for similarity search
C) LLMs can't do math
D) No particular reason

**Correct Answer**: B

---

### Question 4
**In a production RAG system with 1 million documents, where do you use embeddings and where do you use the LLM?**

A) Embed all 1M docs for search (cheap), use LLM only on top-k retrieved docs (expensive)
B) Use LLM for everything (expensive and slow)
C) Don't use embeddings, LLM can handle it all
D) Use embeddings for everything, no LLM needed

**Correct Answer**: A (This is the key efficiency insight!)

---

## PART B: Retrieval Evaluation Metrics

### Question 5
**MRR (Mean Reciprocal Rank) measures:**

A) How many relevant docs were retrieved
B) The position of the FIRST relevant document in results
C) The total number of documents
D) The embedding dimension

**Correct Answer**: B

---

### Question 6
**If the first relevant document appears at position 3, what is the MRR?**

A) 3
B) 0.3
C) 1/3 = 0.333...
D) 3.0

**Correct Answer**: C (MRR = 1 / rank of first relevant doc)

---

### Question 7
**Why is MRR important for RAG?**

A) It measures LLM quality
B) Early results matter most - users look at top results first!
C) It's the only metric that matters
D) It's not important

**Correct Answer**: B

---

### Question 8
**NDCG (Normalized Discounted Cumulative Gain) is best for:**

A) Binary relevance (relevant or not)
B) Ranked results where position matters (early results weighted more)
C) Measuring generation quality
D) Counting tokens

**Correct Answer**: B

---

### Question 9
**Scenario: Your RAG retrieves 5 docs. 2 are relevant (at positions 1 and 5). What's wrong and how to improve?**

A) Nothing wrong, 2 is good enough
B) Low NDCG because relevant doc at position 5 is too late - improve ranking/chunking
C) Too few documents retrieved
D) Need bigger database

**Correct Answer**: B

---

## PART C: Generation Evaluation Metrics

### Question 10
**Faithfulness measures:**

A) How fast the LLM responds
B) Whether the answer only includes info from retrieved documents (no hallucinations)
C) User satisfaction
D) Token count

**Correct Answer**: B

---

### Question 11
**Why is Faithfulness the MOST CRITICAL metric in production RAG?**

A) It's easy to calculate
B) Hallucinations can cause serious harm (wrong medical/legal advice, etc.)
C) It's the only metric
D) It makes responses faster

**Correct Answer**: B

---

### Question 12
**Answer Relevance measures:**

A) Whether documents are relevant
B) Whether the answer actually addresses the question asked
C) How long the answer is
D) User clicks

**Correct Answer**: B

---

### Question 13
**Context Relevance measures:**

A) Whether the LLM is working
B) Whether the retrieved documents are actually relevant to the question
C) Database size
D) Embedding quality

**Correct Answer**: B

---

### Question 14
**RAGAS Score combines:**

A) Only retrieval metrics
B) Only generation metrics
C) Both retrieval and generation metrics (end-to-end quality)
D) Only speed metrics

**Correct Answer**: C

---

### Question 15 (HARD - Scenario-Based)
**You're evaluating your RAG system:**
- Precision: 0.4 (40% of retrieved docs are relevant)
- Recall: 0.9 (found 90% of all relevant docs)
- Faithfulness: 0.95 (very few hallucinations)
- Answer Relevance: 0.85 (answers are on-topic)

**What should you optimize FIRST?**

A) Recall (it's already high)
B) Precision (too many irrelevant docs getting through - confusing the LLM)
C) Faithfulness (it's already great)
D) Don't change anything

**Correct Answer**: B

**Reasoning**: Low precision means you're retrieving lots of junk, which:
- Wastes LLM context window
- Increases cost (more tokens)
- Can confuse the LLM
- Increases latency

Solution: Increase similarity threshold, improve chunking, use MMR, or add metadata filters.

---

## BONUS QUESTIONS (No points, but learn!)

**B1: When to use which metrics?**

| Phase | Metrics | Purpose |
|-------|---------|---------|
| Development | Precision, Recall, MRR, NDCG | Tune retrieval strategy |
| Pre-Launch | Faithfulness, RAGAS | Ensure quality & safety |
| Production | All + Latency + Cost | Monitor & improve continuously |

**B2: Metric Trade-offs**

- **High Recall, Low Precision**: Casting a wide net (find everything but include junk)
  - Fix: Increase threshold, better chunking
- **High Precision, Low Recall**: Very picky (miss relevant docs)
  - Fix: Lower threshold, retrieve more docs (higher k)
- **High Faithfulness, Low Relevance**: Accurate but off-topic
  - Fix: Improve retrieval, better query understanding

**B3: Red Flags in Production**

- 🚨 Faithfulness < 0.7 → Hallucination risk, don't deploy!
- 🚨 MRR < 0.5 → First relevant doc too far down, user won't see it
- 🚨 RAGAS < 0.6 → Overall quality too low
- 🚨 High variance in metrics → Inconsistent quality, need more testing

---

## Scoring Guide
- **14-15 correct**: 🥇👑 RAG Grandmaster! You're production-ready!
- **12-13 correct**: 🥇 Excellent! Deep understanding!
- **10-11 correct**: 🥈 Very good! Minor gaps to fill!
- **8-9 correct**: 🥉 Good foundation, review metrics section
- **6-7 correct**: 📚 Promising start, need more practice
- **0-5 correct**: 📚 Review Demo 4 carefully - metrics are crucial!

---

## 🎁 Prize Distribution
**Top 3 teams** win GRAND PRIZES! 🏆🎁

This is the hardest quiz - celebrate if you do well!

---

## Key Concepts Tested
✅ Embedding models vs LLMs (roles & efficiency)
✅ Retrieval metrics (Precision, Recall, MRR, NDCG)
✅ Generation metrics (Faithfulness, Answer Relevance, Context Relevance)
✅ RAGAS score (combined metric)
✅ Metric interpretation
✅ Production considerations
✅ Trade-off analysis
✅ Problem diagnosis and solutions
✅ Real-world scenario-based decisions

---

## 🎓 If You Master This Quiz...

**You can:**
- Build production RAG systems with confidence
- Evaluate and improve RAG quality systematically
- Make data-driven decisions about chunking, retrieval, generation
- Debug quality issues in production
- Talk intelligently about RAG in interviews/projects

**You understand:**
- RAG is not magic, it's measurable engineering
- Multiple metrics are needed (no silver bullet)
- Trade-offs exist and must be managed
- Continuous evaluation and improvement is essential

**Congratulations! You're now a RAG practitioner! 🚀**
