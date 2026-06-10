# Quiz 2: Chunking Strategies
**After: Chunking Deep Dive + Demo 2 (45 minutes into session)**

**Time Limit**: 4 minutes
**Questions**: 10
**Format**: Multiple choice + Scenario-based

---

## Question 1
**Why is chunking necessary for RAG?**

A) LLMs can't read entire documents at once
B) Makes documents look prettier
C) Reduces storage costs
D) Speeds up internet connection

**Correct Answer**: A

---

## Question 2
**What happens if chunks are TOO SMALL?**

A) Nothing wrong, smaller is always better
B) Lose context and meaning
C) Vector database crashes
D) LLM generates longer answers

**Correct Answer**: B

---

## Question 3
**What happens if chunks are TOO LARGE?**

A) Better results always
B) Irrelevant information gets included, confuses the LLM
C) Faster retrieval
D) More accurate embeddings

**Correct Answer**: B

---

## Question 4
**Recommended chunk size for general text:**

A) 10-20 tokens
B) 50-100 tokens
C) 200-500 tokens
D) 5000+ tokens

**Correct Answer**: C

---

## Question 5
**What is chunk overlap and why is it useful?**

A) Error in chunking algorithm
B) Duplicate text between chunks to preserve context across boundaries
C) Compression technique
D) Method to save storage

**Correct Answer**: B

---

## Question 6
**Which chunking strategy is BEST for most scenarios?**

A) Fixed-size chunking
B) Random chunking
C) Recursive chunking
D) No chunking, use full documents

**Correct Answer**: C (Smart fallbacks, respects structure)

---

## Question 7
**Scenario: You're building RAG for a legal document system where accuracy is CRITICAL. What should you prioritize?**

A) Speed - use largest chunks possible
B) Precision - use semantic chunking + metadata for attribution
C) Cost - use smallest chunks to save money
D) Simplicity - no chunking needed

**Correct Answer**: B

---

## Question 8
**What is metadata in the context of RAG chunks?**

A) Data about data (e.g., source, page number, date)
B) Secret information
C) Embedding dimensions
D) LLM temperature setting

**Correct Answer**: A

---

## Question 9
**Why add metadata like source filename and page number to chunks?**

A) Makes chunks bigger
B) Improves visualization
C) Enables filtering and attribution (know where answer came from)
D) Required by law

**Correct Answer**: C

---

## Question 10
**True or False: The same chunking strategy works perfectly for all document types (code, legal, chat logs, etc.).**

A) True
B) False

**Correct Answer**: B (False - different docs need different strategies!)

---

## Scoring Guide
- **9-10 correct**: 🥇 Chunking Master!
- **7-8 correct**: 🥈 Strong understanding!
- **5-6 correct**: 🥉 Good, but review edge cases
- **0-4 correct**: 📚 Practice with Demo 2 again

---

## 🎁 Prize Distribution
**Top 3 teams** win goodies! 🎉

---

## Key Concepts Tested
✅ Purpose of chunking
✅ Chunk size trade-offs
✅ Chunk overlap importance
✅ Recursive chunking advantages
✅ Metadata utility
✅ Domain-specific considerations
✅ Scenario-based decision making
