"""
Demo 4: RAG Evaluation Metrics - Measuring Quality
==================================================

This is the MOST IMPORTANT demo! 📊

You can't improve what you don't measure. This demo shows how to evaluate:
1. RETRIEVAL QUALITY: Did we find the right documents?
2. GENERATION QUALITY: Is the answer good?

CRITICAL METRICS COVERED:
=======================

RETRIEVAL METRICS:
- Precision: Of retrieved docs, how many are relevant?
- Recall: Of all relevant docs, how many did we retrieve?
- MRR (Mean Reciprocal Rank): Where's the first relevant doc?
- NDCG (Normalized Discounted Cumulative Gain): Quality of ranking
- Hit Rate: Did we find at least one relevant doc?

GENERATION METRICS:
- Faithfulness: Does answer match retrieved documents?
- Answer Relevance: Does answer address the question?
- Context Relevance: Are retrieved docs actually relevant?
- Answer Similarity: How close to ground truth answer?
- RAGAS Score: Combined metric (end-to-end quality)
"""

import os
import sys
import numpy as np
from typing import List, Dict

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("❌ ERROR: GOOGLE_API_KEY not found!")
    print("📝 Create a .env file with: GOOGLE_API_KEY=your-key-here")
    print("🔑 Get key at: https://makersuite.google.com/app/apikey")
    exit(1)

print("✅ API Key loaded\n")

# ========================================
# SAMPLE KNOWLEDGE BASE (Larger for better evaluation)
# ========================================
print("📚 Creating knowledge base...")

documents = [
    # RAG Basics
    """RAG (Retrieval Augmented Generation) is a technique that combines information
    retrieval with Large Language Model generation. It helps LLMs access external
    knowledge and reduces hallucinations. RAG has three phases: Indexing, Retrieval,
    and Generation.""",

    """RAG was introduced in 2020 by Facebook AI (now Meta). It's now used in
    production systems at Google, Microsoft, and many startups. RAG is essential
    for enterprise AI applications.""",

    # Chunking
    """Chunking splits documents into smaller pieces. Optimal chunk size depends on
    your use case. Typical range: 200-500 tokens. Too small loses context, too large
    includes irrelevant information.""",

    """Advanced chunking strategies include: semantic chunking (split by meaning),
    recursive chunking (try multiple methods), and document-aware chunking
    (respect headers, code blocks). Overlap of 10-20% helps preserve context.""",

    # Embeddings
    """Embeddings convert text to vectors. Similar meanings → similar vectors.
    Gemini's text-embedding-004 creates 768-dimensional embeddings. These capture
    semantic meaning.""",

    """Embedding models are different from LLMs. Embeddings are for search (cheap, fast),
    LLMs are for generation (expensive, slow). Use embeddings for millions of docs,
    LLMs for answering with top-k docs.""",

    # Vector Databases
    """Vector databases optimize similarity search. Popular options: ChromaDB (simple),
    FAISS (fast), Pinecone (cloud), Weaviate (feature-rich). They use algorithms
    like HNSW, IVF for approximate nearest neighbors.""",

    """FAISS (Facebook AI Similarity Search) can handle billions of vectors. It supports
    GPU acceleration. ChromaDB is easier to start with for prototyping.""",

    # Evaluation
    """RAG evaluation has two parts: retrieval quality and generation quality.
    Retrieval metrics: Precision, Recall, MRR, NDCG. Generation metrics: Faithfulness,
    Relevance, Answer Similarity.""",

    """RAGAS (RAG Assessment) framework automates evaluation. It measures: faithfulness
    (no hallucinations), answer relevance (addresses question), context relevance
    (retrieved docs are useful). RAGAS score ranges 0-1, higher is better.""",

    # Production Tips
    """Production RAG systems need: caching (embeddings + LLM calls), monitoring
    (track latency, cost), A/B testing (compare chunking strategies), user feedback
    (thumbs up/down).""",

    """Cost optimization: Use smaller embedding models (text-embedding-004), cache
    embeddings, use Gemini Flash for speed. Monitor token usage.""",
]

# Create chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=30,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = text_splitter.create_documents(documents)
print(f"✅ Created {len(chunks)} chunks\n")

# Create vector DB
print("🧮 Creating embeddings and vector DB...")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)
vectorstore = Chroma.from_documents(chunks, embeddings)
print("✅ Vector DB ready\n")

# Initialize LLM
llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)

# ========================================
# PART 1: RETRIEVAL METRICS
# ========================================
print("\n" + "="*70)
print("📊 PART 1: RETRIEVAL METRICS")
print("="*70)

# Test query
query = "How should I evaluate the quality of my RAG system?"

print(f"\n❓ Query: '{query}'")

# Retrieve documents
k = 4  # Retrieve top 4 chunks
retrieved_docs = vectorstore.similarity_search(query, k=k)

print(f"\n🔍 Retrieved Top {k} Documents:")

# Check which retrieved docs are relevant (based on content keywords)
# Relevant = mentions evaluation, metrics, precision, recall, RAGAS, etc.
evaluation_keywords = ['evaluat', 'metric', 'precision', 'recall', 'ragas', 'faithfulness', 'ndcg']

retrieved_ids = []
for i, doc in enumerate(retrieved_docs):
    content_lower = doc.page_content.lower()
    is_relevant = any(keyword in content_lower for keyword in evaluation_keywords)
    retrieved_ids.append(1 if is_relevant else 0)  # 1 = relevant, 0 = not relevant

    relevance_marker = "✅ RELEVANT" if is_relevant else "❌ Not relevant"
    print(f"\n  [{i+1}] {relevance_marker}")
    print(f"      {doc.page_content[:100]}...")

# For this demo, ground truth = documents that mention evaluation
# Count how many relevant docs exist in our knowledge base
total_relevant_in_db = sum([1 for d in documents if any(kw in d.lower() for kw in evaluation_keywords)])
print(f"\n✅ Ground Truth: ~{total_relevant_in_db} evaluation-related docs in knowledge base")

# Calculate Retrieval Metrics
print("\n" + "-"*70)
print("📈 RETRIEVAL METRICS:")
print("-"*70)

# 1. Precision: Of retrieved docs, how many are relevant?
num_relevant_retrieved = sum(retrieved_ids)  # Count 1s in retrieved_ids
precision = num_relevant_retrieved / k if k > 0 else 0

print(f"\n1️⃣ PRECISION = {num_relevant_retrieved}/{k} = {precision:.2f}")
print(f"   📖 Meaning: {precision*100:.0f}% of retrieved docs are actually relevant")
print(f"   💡 Higher is better (1.0 = perfect)")

# 2. Recall: Of all relevant docs, how many did we retrieve?
recall = num_relevant_retrieved / total_relevant_in_db if total_relevant_in_db > 0 else 0

print(f"\n2️⃣ RECALL = {num_relevant_retrieved}/{total_relevant_in_db} = {recall:.2f}")
print(f"   📖 Meaning: We found {recall*100:.0f}% of all relevant docs")
print(f"   💡 Higher is better (1.0 = found everything)")

# 3. F1 Score: Harmonic mean of Precision and Recall
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f"\n3️⃣ F1 SCORE = 2 * (P * R) / (P + R) = {f1:.2f}")
print(f"   📖 Meaning: Balanced metric combining precision and recall")
print(f"   💡 Good for comparing retrieval strategies")

# 4. Mean Reciprocal Rank (MRR): Where's the first relevant doc?
first_relevant_rank = None
for rank, is_relevant in enumerate(retrieved_ids, start=1):
    if is_relevant == 1:
        first_relevant_rank = rank
        break

mrr = 1 / first_relevant_rank if first_relevant_rank else 0

print(f"\n4️⃣ MRR (Mean Reciprocal Rank) = 1/{first_relevant_rank if first_relevant_rank else '∞'} = {mrr:.2f}")
print(f"   📖 Meaning: First relevant doc appeared at rank {first_relevant_rank}")
print(f"   💡 Higher is better (1.0 = relevant doc is #1)")
print(f"   🎯 Critical for RAG: Early results matter most!")

# 5. Hit Rate: Did we find at least one relevant doc?
hit_rate = 1.0 if num_relevant_retrieved > 0 else 0.0

print(f"\n5️⃣ HIT RATE = {hit_rate:.2f}")
print(f"   📖 Meaning: {'✅ YES' if hit_rate > 0 else '❌ NO'}, we found at least one relevant doc")
print(f"   💡 Binary metric: 1 (success) or 0 (failure)")

# 6. NDCG (Normalized Discounted Cumulative Gain)
# More relevant docs at top positions are rewarded more
relevance_scores = retrieved_ids  # Already contains 0s and 1s
dcg = sum([rel / np.log2(idx + 2) for idx, rel in enumerate(relevance_scores)])
ideal_relevance = sorted(relevance_scores, reverse=True)
idcg = sum([rel / np.log2(idx + 2) for idx, rel in enumerate(ideal_relevance)])
ndcg = dcg / idcg if idcg > 0 else 0

print(f"\n6️⃣ NDCG (Normalized Discounted Cumulative Gain) = {ndcg:.3f}")
print(f"   📖 Meaning: Quality of ranking (early results weighted more)")
print(f"   💡 1.0 = perfect ranking, 0.0 = worst ranking")
print(f"   🎯 Best metric for ranked retrieval!")

# Helper function for interpretation
def _interpret_score(score):
    """Helper to interpret scores"""
    if score >= 0.8:
        return "🟢 Excellent"
    elif score >= 0.6:
        return "🟡 Good"
    elif score >= 0.4:
        return "🟠 Needs Improvement"
    else:
        return "🔴 Poor"

# Summary table
print("\n" + "-"*70)
print("📊 RETRIEVAL METRICS SUMMARY:")
print("-"*70)
print(f"{'Metric':<25} {'Score':<10} {'Interpretation'}")
print("-"*70)
print(f"{'Precision':<25} {precision:>8.2f}   {_interpret_score(precision)}")
print(f"{'Recall':<25} {recall:>8.2f}   {_interpret_score(recall)}")
print(f"{'F1 Score':<25} {f1:>8.2f}   {_interpret_score(f1)}")
print(f"{'MRR':<25} {mrr:>8.2f}   {_interpret_score(mrr)}")
print(f"{'Hit Rate':<25} {hit_rate:>8.2f}   {'✅ Success' if hit_rate > 0 else '❌ Failure'}")
print(f"{'NDCG':<25} {ndcg:>8.3f}   {_interpret_score(ndcg)}")
print("-"*70)


# ========================================
# PART 2: GENERATION METRICS
# ========================================
print("\n\n" + "="*70)
print("📊 PART 2: GENERATION METRICS")
print("="*70)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# Test question
question = "What metrics should I use to evaluate RAG systems?"
print(f"\n❓ Question: '{question}'")

# Get answer
result = qa_chain.invoke({"query": question})
generated_answer = result['result']
source_docs = result['source_documents']

print(f"\n💬 Generated Answer:")
print(f"   {generated_answer}")

print(f"\n📄 Source Documents Used:")
for i, doc in enumerate(source_docs, 1):
    print(f"\n   [{i}] {doc.page_content[:120]}...")

# Ground truth answer (what a perfect answer would be)
ground_truth = """RAG systems should be evaluated using both retrieval and generation metrics.
Retrieval metrics include Precision, Recall, MRR, and NDCG to measure search quality.
Generation metrics include Faithfulness (no hallucinations), Answer Relevance (addresses question),
and Context Relevance. The RAGAS framework provides comprehensive evaluation."""

print(f"\n✅ Ground Truth (Expected Answer):")
print(f"   {ground_truth}")

# Calculate Generation Metrics
print("\n" + "-"*70)
print("📈 GENERATION METRICS:")
print("-"*70)

# 1. Faithfulness: Does answer match source documents?
print(f"\n1️⃣ FAITHFULNESS")
print(f"   📖 Definition: Does the answer only include info from retrieved docs?")
print(f"   🎯 Goal: Prevent hallucinations")

# Simple heuristic: Check if key facts from answer appear in source docs
source_text = " ".join([doc.page_content for doc in source_docs])
key_terms = ["precision", "recall", "MRR", "NDCG", "faithfulness", "relevance", "RAGAS"]
terms_in_sources = sum([1 for term in key_terms if term.lower() in source_text.lower()])
faithfulness_score = terms_in_sources / len(key_terms)

print(f"   📊 Score: {faithfulness_score:.2f} ({terms_in_sources}/{len(key_terms)} key terms found in sources)")
print(f"   💡 {_interpret_score(faithfulness_score)}")

# 2. Answer Relevance: Does answer address the question?
print(f"\n2️⃣ ANSWER RELEVANCE")
print(f"   📖 Definition: Does the answer actually address what was asked?")
print(f"   🎯 Goal: Ensure answer is on-topic")

# Heuristic: Check if answer mentions "metrics" and "evaluation" (from question)
question_keywords = ["metrics", "evaluate", "quality"]
keywords_in_answer = sum([1 for kw in question_keywords if kw.lower() in generated_answer.lower()])
answer_relevance_score = keywords_in_answer / len(question_keywords)

print(f"   📊 Score: {answer_relevance_score:.2f} ({keywords_in_answer}/{len(question_keywords)} question keywords in answer)")
print(f"   💡 {_interpret_score(answer_relevance_score)}")

# 3. Context Relevance: Are retrieved docs actually useful?
print(f"\n3️⃣ CONTEXT RELEVANCE")
print(f"   📖 Definition: Are the retrieved documents relevant to the question?")
print(f"   🎯 Goal: Measure retrieval quality from generation perspective")

# Check if source docs mention evaluation-related terms
evaluation_terms = ["evaluate", "metric", "precision", "recall", "quality"]
relevant_docs = sum([
    1 for doc in source_docs
    if any(term in doc.page_content.lower() for term in evaluation_terms)
])
context_relevance_score = relevant_docs / len(source_docs)

print(f"   📊 Score: {context_relevance_score:.2f} ({relevant_docs}/{len(source_docs)} docs are relevant)")
print(f"   💡 {_interpret_score(context_relevance_score)}")

# 4. Answer Similarity: How close to ground truth?
print(f"\n4️⃣ ANSWER SIMILARITY")
print(f"   📖 Definition: How similar is the answer to expected ground truth?")
print(f"   🎯 Goal: Measure answer quality against reference")

# Simple word overlap (in production, use embeddings or BLEU/ROUGE scores)
answer_words = set(generated_answer.lower().split())
truth_words = set(ground_truth.lower().split())
overlap = len(answer_words.intersection(truth_words))
similarity_score = overlap / len(truth_words) if truth_words else 0

print(f"   📊 Score: {similarity_score:.2f} (word overlap with ground truth)")
print(f"   💡 {_interpret_score(similarity_score)}")
print(f"   ⚠️  Note: In production, use cosine similarity of embeddings (more accurate)")

# 5. RAGAS Score: Combined metric
print(f"\n5️⃣ RAGAS SCORE (Combined)")
print(f"   📖 Definition: Harmonic mean of all metrics")
print(f"   🎯 Goal: Single number for overall RAG quality")

ragas_score = (
    4 * faithfulness_score * answer_relevance_score * context_relevance_score * similarity_score /
    (faithfulness_score + answer_relevance_score + context_relevance_score + similarity_score)
) if (faithfulness_score + answer_relevance_score + context_relevance_score + similarity_score) > 0 else 0

print(f"   📊 Score: {ragas_score:.2f}")
print(f"   💡 {_interpret_score(ragas_score)}")
print(f"   Formula: Harmonic mean of Faithfulness, Answer Relevance, Context Relevance, Similarity")

# Summary table
print("\n" + "-"*70)
print("📊 GENERATION METRICS SUMMARY:")
print("-"*70)
print(f"{'Metric':<25} {'Score':<10} {'Interpretation'}")
print("-"*70)
print(f"{'Faithfulness':<25} {faithfulness_score:>8.2f}   {_interpret_score(faithfulness_score)}")
print(f"{'Answer Relevance':<25} {answer_relevance_score:>8.2f}   {_interpret_score(answer_relevance_score)}")
print(f"{'Context Relevance':<25} {context_relevance_score:>8.2f}   {_interpret_score(context_relevance_score)}")
print(f"{'Answer Similarity':<25} {similarity_score:>8.2f}   {_interpret_score(similarity_score)}")
print(f"{'RAGAS Score (Overall)':<25} {ragas_score:>8.2f}   {_interpret_score(ragas_score)}")
print("-"*70)

# ========================================
# PART 3: WHY METRICS MATTER
# ========================================
print("\n\n" + "="*70)
print("🎓 WHY THESE METRICS MATTER")
print("="*70)

print("""
🔍 RETRIEVAL METRICS tell you:
   • Are you finding the right documents? (Precision)
   • Are you missing relevant documents? (Recall)
   • Are the best results appearing first? (MRR, NDCG)
   • Is your retrieval strategy working at all? (Hit Rate)

💬 GENERATION METRICS tell you:
   • Is the LLM hallucinating? (Faithfulness)
   • Is the answer on-topic? (Answer Relevance)
   • Did retrieval give good context? (Context Relevance)
   • Is the answer high-quality? (Answer Similarity, RAGAS)

🚀 IN PRODUCTION:
   1. Track these metrics over time → Detect regressions
   2. A/B test chunking strategies → Measure which is better
   3. Set thresholds → Alert if quality drops
   4. Use user feedback → "Was this helpful?" → Validate metrics

⚠️  COMMON MISTAKE:
   Building RAG without evaluation = Flying blind!
   You MUST measure to improve.

💡 PRO TIP:
   Start with high recall (find all relevant docs), then optimize precision.
   For generation, faithfulness is most critical (no hallucinations!).
""")

print("\n" + "="*70)
print("✨ Demo Complete!")
print("="*70)

print("\n🎯 KEY TAKEAWAYS:")
print("1. Evaluate BOTH retrieval (finding docs) and generation (answering)")
print("2. No single metric is perfect - use multiple metrics")
print("3. MRR and NDCG are crucial for ranked retrieval")
print("4. Faithfulness prevents hallucinations (most important!)")
print("5. RAGAS gives you an overall quality score")

print("\n📊 NEXT STEPS:")
print("• Use the 'ragas' library for automated evaluation")
print("• Build evaluation datasets with questions + ground truth")
print("• Track metrics in production with monitoring dashboards")
print("• A/B test different RAG configurations")

print("\n💪 YOU NOW KNOW HOW TO EVALUATE RAG SYSTEMS!")
