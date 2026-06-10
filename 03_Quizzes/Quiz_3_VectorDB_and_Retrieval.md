# Quiz 3: Vector Databases & Retrieval Strategies
**After: Vector DB & Retrieval + Demo 3 (65 minutes into session)**

**Time Limit**: 5 minutes
**Questions**: 12
**Format**: Multiple choice + Scenario-based

---

## Question 1
**What are embeddings?**

A) Pictures of text
B) Numerical vector representations of text that capture semantic meaning
C) Compressed text files
D) Database indexes

**Correct Answer**: B

---

## Question 2
**Similar meanings result in:**

A) Completely random vectors
B) Similar/close vectors in embedding space
C) Longer vectors
D) Empty vectors

**Correct Answer**: B

---

## Question 3
**What is the purpose of a vector database?**

A) Store text files
B) Train LLMs
C) Store embeddings and perform fast similarity search
D) Generate responses

**Correct Answer**: C

---

## Question 4
**Compare: ChromaDB vs FAISS**

A) ChromaDB is faster, FAISS has more features
B) FAISS is faster, ChromaDB is easier and has better metadata support
C) They are identical
D) ChromaDB is for images, FAISS is for text

**Correct Answer**: B

---

## Question 5
**Cosine similarity measures:**

A) The actual distance between vectors
B) The angle between vectors (direction similarity)
C) The length of vectors
D) The number of dimensions

**Correct Answer**: B

---

## Question 6
**What does MMR (Maximal Marginal Relevance) do?**

A) Makes retrieval faster
B) Balances relevance to query AND diversity among results
C) Increases accuracy always
D) Compresses vectors

**Correct Answer**: B

---

## Question 7
**When should you use MMR instead of regular cosine similarity?**

A) Always, it's always better
B) Never, it's slower
C) When you want diverse results instead of all similar documents
D) Only for images

**Correct Answer**: C

---

## Question 8
**Scenario: You're building a chatbot that should answer from multiple topics. What retrieval strategy?**

A) Cosine similarity (all top results might be from same topic)
B) MMR with lambda=0.6 (diverse results from different topics)
C) Random retrieval
D) No retrieval needed

**Correct Answer**: B

---

## Question 9
**What is a similarity threshold in retrieval?**

A) Maximum number of results
B) Minimum similarity score required to return a document
C) Database size limit
D) Token count limit

**Correct Answer**: B

---

## Question 10
**Why use metadata filtering?**

A) To make search slower
B) To search only within specific categories (e.g., only "engineering" docs)
C) To delete documents
D) To compress the database

**Correct Answer**: B

---

## Question 11
**What is Precision in retrieval?**

A) How fast the search is
B) Of all retrieved documents, how many are actually relevant?
C) Of all relevant documents, how many did we retrieve?
D) The embedding dimension size

**Correct Answer**: B

---

## Question 12
**What is Recall in retrieval?**

A) How fast the search is
B) Of all retrieved documents, how many are actually relevant?
C) Of all relevant documents in the database, how many did we retrieve?
D) The database size

**Correct Answer**: C

---

## Bonus Concept Questions (No points, just learning!)

**Q: High Precision, Low Recall means?**
Answer: We're very accurate (what we find is relevant) but missing many relevant docs.
Example: Returning 2 perfect results but missing 8 other relevant ones.

**Q: Low Precision, High Recall means?**
Answer: We find most relevant docs but also include many irrelevant ones.
Example: Returning 20 docs including all 10 relevant ones + 10 junk.

**Q: Which is better?**
Answer: Depends on use case!
- Legal/Medical: Need high precision (no wrong info)
- Research: Need high recall (don't miss anything)
- RAG: Balance both!

---

## Scoring Guide
- **11-12 correct**: 🥇 Vector Search Expert!
- **9-10 correct**: 🥈 Excellent grasp of concepts!
- **7-8 correct**: 🥉 Good foundation!
- **5-6 correct**: 📚 Review retrieval strategies
- **0-4 correct**: 📚 Go through Demo 3 again carefully

---

## 🎁 Prize Distribution
**Top 3 teams** win goodies! 🎁

---

## Key Concepts Tested
✅ Embeddings fundamentals
✅ Vector database purpose
✅ ChromaDB vs FAISS trade-offs
✅ Cosine similarity
✅ MMR for diversity
✅ Similarity thresholds
✅ Metadata filtering
✅ Precision vs Recall (intro to metrics!)
✅ Scenario-based strategy selection
