"""
Demo 3: Vector Storage & Retrieval Strategies
==============================================

This demo covers TWO critical concepts:
1. VECTOR DATABASES: ChromaDB vs FAISS (when to use what?)
2. RETRIEVAL STRATEGIES: Different ways to search & when to use them

RETRIEVAL STRATEGIES COVERED:
==============================
1. Cosine Similarity (default) - Most common, measures angle between vectors
2. Euclidean Distance - Measures actual distance in vector space
3. MMR (Maximal Marginal Relevance) - Balances relevance + diversity
4. Similarity Score Threshold - Only return results above threshold
5. Metadata Filtering - Filter before searching

Each strategy has different use cases! 🎯
"""

import os
import sys
import numpy as np

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma, FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

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
# CREATE KNOWLEDGE BASE FROM FILE
# ========================================
print("📚 Loading knowledge base from file...")

knowledge_file = "knowledge_base.txt"
if not os.path.exists(knowledge_file):
    print(f"❌ ERROR: {knowledge_file} not found!")
    exit(1)

with open(knowledge_file, 'r', encoding='utf-8') as f:
    full_text = f.read()

print(f"✅ Loaded knowledge base ({len(full_text)} characters)\n")

# Split into sections (by double newlines)
sections = [s.strip() for s in full_text.split('\n\n') if s.strip() and len(s.strip()) > 50]

# Take first 10 substantial sections
documents = sections[:10]

# Add metadata based on content
doc_metadata = []
for doc in documents:
    doc_lower = doc.lower()

    # Determine category based on keywords
    if any(word in doc_lower for word in ['product', 'autoflow', 'features', 'pricing']):
        category = "product_info"
        topic = "products"
    elif any(word in doc_lower for word in ['customer', 'techmart', 'healthcare', 'finserve']):
        category = "customer_stories"
        topic = "customers"
    elif any(word in doc_lower for word in ['training', 'certification', 'course']):
        category = "training"
        topic = "education"
    elif any(word in doc_lower for word in ['support', 'contact', 'phone', 'email']):
        category = "support"
        topic = "contact"
    elif any(word in doc_lower for word in ['company', 'acme', 'overview', 'headquarters']):
        category = "company_info"
        topic = "about"
    else:
        category = "general"
        topic = "info"

    doc_metadata.append({
        "topic": topic,
        "category": category,
        "source": "knowledge_base.txt"
    })

# Create chunks with metadata
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = []
metadatas = []

for doc, meta in zip(documents, doc_metadata):
    doc_chunks = text_splitter.split_text(doc)
    chunks.extend(doc_chunks)
    metadatas.extend([meta] * len(doc_chunks))

print(f"✅ Created {len(chunks)} chunks with metadata\n")

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# ========================================
# PART 1: VECTOR DATABASES COMPARISON
# ========================================
print("\n" + "="*70)
print("📊 PART 1: VECTOR DATABASES - ChromaDB vs FAISS")
print("="*70)

# Create ChromaDB
print("\n🔹 Creating ChromaDB...")
chroma_db = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    metadatas=metadatas,
    collection_name="demo_chroma"
)
print("✅ ChromaDB created (persistent, supports metadata filtering)")

# Create FAISS
print("\n🔹 Creating FAISS...")
faiss_db = FAISS.from_texts(
    texts=chunks,
    embedding=embeddings,
    metadatas=metadatas
)
print("✅ FAISS created (in-memory, ultra-fast)")

print("\n📊 COMPARISON:")
print("-" * 70)
print(f"{'Feature':<30} {'ChromaDB':<20} {'FAISS'}")
print("-" * 70)
print(f"{'Speed':<30} {'Good':<20} {'Excellent (10x faster)'}")
print(f"{'Metadata Filtering':<30} {'Yes ✅':<20} {'Limited'}")
print(f"{'Persistence':<30} {'Built-in ✅':<20} {'Manual save/load'}")
print(f"{'Scalability':<30} {'Millions of docs':<20} {'Billions of docs'}")
print(f"{'Setup Complexity':<30} {'Easy':<20} {'Easy'}")
print(f"{'Production Ready':<30} {'Yes':<20} {'Yes (with wrappers)'}")
print(f"{'Best For':<30} {'Prototyping, SMB':<20} {'High-scale, speed-critical'}")
print("-" * 70)

# ========================================
# PART 2: RETRIEVAL STRATEGIES
# ========================================
print("\n\n" + "="*70)
print("🎯 PART 2: RETRIEVAL STRATEGIES - How to Search")
print("="*70)

query = "What is AutoFlow AI and what are its key features?"
print(f"\n❓ Test Query: '{query}'\n")

# ----------------------------------------
# STRATEGY 1: Cosine Similarity (Default)
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 1: Cosine Similarity (Default)")
print("-"*70)
print("📖 How it works: Measures the angle between query and document vectors")
print("📐 Formula: similarity = (A · B) / (||A|| × ||B||)")
print("📊 Range: -1 to 1 (1 = identical direction, 0 = orthogonal, -1 = opposite)")
print("\n🎯 Use when: General-purpose semantic search (MOST COMMON)")

results = chroma_db.similarity_search(query, k=3)

print("\n✅ Top 3 Results:")
for i, doc in enumerate(results, 1):
    print(f"\n  [{i}] (topic: {doc.metadata.get('topic', 'N/A')})")
    print(f"      {doc.page_content[:100]}...")

print("\n💡 Pros: Fast, works well for semantic similarity, standard approach")
print("⚠️  Cons: May return similar but redundant results")

# ----------------------------------------
# STRATEGY 2: Euclidean Distance
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 2: Euclidean Distance")
print("-"*70)
print("📖 How it works: Measures straight-line distance in vector space")
print("📐 Formula: distance = sqrt(Σ(A_i - B_i)²)")
print("📊 Range: 0 to ∞ (0 = identical, larger = more different)")
print("\n🎯 Use when: You care about magnitude differences, not just direction")

# For FAISS, we can specify distance metric
# Note: Lower distance = more similar (opposite of cosine)
results_with_scores = chroma_db.similarity_search_with_score(query, k=3)

print("\n✅ Top 3 Results with Scores:")
for i, (doc, score) in enumerate(results_with_scores, 1):
    print(f"\n  [{i}] Score: {score:.4f} (lower = more similar)")
    print(f"      Topic: {doc.metadata.get('topic', 'N/A')}")
    print(f"      {doc.page_content[:80]}...")

print("\n💡 Pros: Intuitive (actual distance), good for normalized vectors")
print("⚠️  Cons: Sensitive to vector magnitudes")

# ----------------------------------------
# STRATEGY 3: MMR (Maximal Marginal Relevance)
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 3: MMR (Maximal Marginal Relevance)")
print("-"*70)
print("📖 How it works: Balances relevance to query AND diversity among results")
print("📐 Formula: MMR = λ × similarity(query, doc) - (1-λ) × max_similarity(doc, selected_docs)")
print("🎚️  λ (lambda): 0 = max diversity, 1 = max relevance (typical: 0.5-0.7)")
print("\n🎯 Use when: You want diverse results, not just the most similar")

# MMR retrieval
mmr_results = chroma_db.max_marginal_relevance_search(
    query,
    k=3,
    fetch_k=10,  # Fetch top 10, then select diverse 3
    lambda_mult=0.5  # Balance: 50% relevance, 50% diversity
)

print("\n✅ Top 3 MMR Results (Diverse):")
for i, doc in enumerate(mmr_results, 1):
    print(f"\n  [{i}] Topic: {doc.metadata.get('topic', 'N/A')}")
    print(f"      {doc.page_content[:100]}...")

print("\n💡 Pros: Reduces redundancy, covers more topics")
print("⚠️  Cons: Might miss some highly relevant docs, slower than similarity search")

print("\n🔬 COMPARISON: Cosine vs MMR")
print("   Cosine: Might return 3 Python docs (all similar)")
print("   MMR: Returns Python + RAG + Data Science docs (diverse topics)")

# ----------------------------------------
# STRATEGY 4: Similarity Score Threshold
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 4: Similarity Score Threshold")
print("-"*70)
print("📖 How it works: Only return documents above a similarity threshold")
print("🎯 Use when: You want high confidence, willing to return fewer results")

threshold = 0.7  # Only docs with similarity > 0.7
results_with_scores = chroma_db.similarity_search_with_relevance_scores(query, k=5)
filtered_results = [(doc, score) for doc, score in results_with_scores if score >= threshold]

print(f"\n✅ Results above threshold ({threshold}):")
print(f"   Found {len(filtered_results)} out of {len(results_with_scores)} total results\n")

for i, (doc, score) in enumerate(filtered_results, 1):
    print(f"  [{i}] Score: {score:.3f} ✅")
    print(f"      {doc.page_content[:80]}...")

print("\n💡 Pros: Quality control, prevents bad results")
print("⚠️  Cons: Might return 0 results if nothing is relevant enough")

print("\n📊 Typical Thresholds:")
print("   0.8-1.0: Very strict (high precision, low recall)")
print("   0.6-0.8: Balanced (recommended)")
print("   0.4-0.6: Permissive (high recall, lower precision)")

# ----------------------------------------
# STRATEGY 5: Metadata Filtering
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 5: Metadata Filtering")
print("-"*70)
print("📖 How it works: Filter documents by metadata BEFORE vector search")
print("🎯 Use when: You want results from specific categories, time periods, sources")

# Filter: Only search in "ai" category documents
filter_query = {"category": "product_info"}
filtered_results = chroma_db.similarity_search(
    query,
    k=3,
    filter=filter_query
)

print(f"\n✅ Results filtered by: {filter_query}")
print(f"   (Only showing AI-related documents)\n")

for i, doc in enumerate(filtered_results, 1):
    print(f"  [{i}] Category: {doc.metadata.get('category')} ✅")
    print(f"      Topic: {doc.metadata.get('topic')}")
    print(f"      {doc.page_content[:80]}...")

print("\n💡 Pros: Precise targeting, can combine multiple filters")
print("⚠️  Cons: Requires metadata, reduces search space")

print("\n📦 Common Metadata Filters:")
print("   • source: 'company_docs' (vs external)")
print("   • date: > '2024-01-01' (recent only)")
print("   • author: 'engineering_team'")
print("   • classification: 'public' (vs confidential)")
print("   • version: 'latest'")

# ----------------------------------------
# STRATEGY 6: Hybrid Search (Vector + Keyword)
# ----------------------------------------
print("\n" + "-"*70)
print("🔹 STRATEGY 6: Hybrid Search (Vector + Keyword)")
print("-"*70)
print("📖 How it works: Combine vector search (semantic) + keyword search (exact match)")
print("🎯 Use when: You need both semantic understanding AND exact term matches")

print("\n🔬 Example:")
print("   Query: 'Python pandas library'")
print("   Vector Search: Finds docs about data manipulation (semantic)")
print("   Keyword Search: Finds docs mentioning 'pandas' exactly")
print("   Hybrid: Combines both → Better results!")

print("\n📊 Typical Hybrid Weights:")
print("   70% vector + 30% keyword (semantic-focused)")
print("   50% vector + 50% keyword (balanced)")
print("   30% vector + 70% keyword (keyword-focused)")

print("\n💡 Pros: Best of both worlds, handles ambiguous queries better")
print("⚠️  Cons: More complex, requires keyword index + vector index")

# ========================================
# PART 3: WHEN TO USE WHAT?
# ========================================
print("\n\n" + "="*70)
print("🎯 DECISION GUIDE: When to Use Each Strategy")
print("="*70)

decision_table = """
┌─────────────────────────────┬──────────────────────────────────────────┐
│ YOUR NEED                   │ RECOMMENDED STRATEGY                     │
├─────────────────────────────┼──────────────────────────────────────────┤
│ General Q&A                 │ ✅ Cosine Similarity (default)          │
│ Fast prototyping            │ ✅ ChromaDB + Cosine Similarity         │
│ High-scale production       │ ✅ FAISS + Cosine Similarity            │
│ Diverse results needed      │ ✅ MMR (lambda=0.5-0.7)                 │
│ Quality over quantity       │ ✅ Similarity Threshold (>0.7)          │
│ Category-specific search    │ ✅ Metadata Filtering                   │
│ Exact term + semantic       │ ✅ Hybrid Search                        │
│ Legal/medical (precision)   │ ✅ Threshold + Metadata Filtering       │
│ Chatbot (varied topics)     │ ✅ MMR + Metadata Filtering             │
│ Code search                 │ ✅ Hybrid (keywords important)          │
└─────────────────────────────┴──────────────────────────────────────────┘
"""

print(decision_table)

# ========================================
# PART 4: PERFORMANCE COMPARISON
# ========================================
print("\n" + "="*70)
print("⚡ PERFORMANCE COMPARISON")
print("="*70)

import time

query = "Tell me about ACME's customer success stories"

strategies = [
    ("Cosine Similarity", lambda: chroma_db.similarity_search(query, k=3)),
    ("MMR", lambda: chroma_db.max_marginal_relevance_search(query, k=3, fetch_k=10)),
    ("Metadata Filter", lambda: chroma_db.similarity_search(query, k=3, filter={"category": "ai"})),
]

print(f"\n🔍 Query: '{query}'")
print(f"📊 Timing each strategy (3 runs each):\n")

for strategy_name, search_func in strategies:
    times = []
    for _ in range(3):
        start = time.time()
        results = search_func()
        times.append(time.time() - start)

    avg_time = np.mean(times) * 1000  # Convert to milliseconds
    print(f"  {strategy_name:<25} {avg_time:>6.2f} ms (avg)")

print("\n💡 Observations:")
print("   • Cosine is fastest (simple vector comparison)")
print("   • MMR is slower (needs to compute diversity)")
print("   • Metadata filter can be faster (smaller search space)")

# ========================================
# KEY TAKEAWAYS
# ========================================
print("\n\n" + "="*70)
print("🎓 KEY TAKEAWAYS")
print("="*70)

print("""
1. VECTOR DATABASES:
   • ChromaDB: Easy to use, good for prototyping, has persistence
   • FAISS: Blazing fast, scales to billions, used in production

2. RETRIEVAL STRATEGIES:
   • Cosine Similarity: Your default choice (90% of cases)
   • MMR: When you need diverse results
   • Threshold: When you need high confidence
   • Metadata Filtering: When you have specific categories
   • Hybrid: When semantic + keyword both matter

3. SIMILARITY METRICS:
   • Cosine: Measures angle (direction), best for semantic similarity
   • Euclidean: Measures distance (magnitude), good for normalized vectors
   • Use cosine for text, Euclidean for specific numerical features

4. TRADE-OFFS:
   • Speed vs Diversity: Cosine faster, MMR more diverse
   • Precision vs Recall: Threshold increases precision, decreases recall
   • Flexibility vs Performance: Metadata adds flexibility, slight overhead

5. PRODUCTION TIPS:
   • Start with Cosine Similarity + ChromaDB
   • Add MMR if results are too redundant
   • Add Metadata Filtering for multi-tenant systems
   • Switch to FAISS when you need speed at scale
   • Always measure: log retrieval times and relevance!

6. ALWAYS ADD METADATA:
   • Source, category, timestamp, author, version
   • Enables powerful filtering and attribution
   • Critical for production systems!
""")

print("\n🚀 YOU NOW UNDERSTAND VECTOR STORAGE & RETRIEVAL STRATEGIES!")
print("\n💪 Next: Combine this with good chunking and evaluation metrics")
print("   → You'll have a production-ready RAG system!")
