"""
Demo 2: Chunking Strategies - The Art of Document Splitting
============================================================

Chunking is CRITICAL for RAG quality! 🔪

Bad chunking → Poor retrieval → Wrong answers → Sad users 😢
Good chunking → Great retrieval → Accurate answers → Happy users 😊

This demo compares 4 chunking strategies:
1. Fixed-size chunking (simple, but can split mid-sentence)
2. Sentence-based chunking (preserves meaning)
3. Recursive chunking (smart splitting with fallbacks)
4. Semantic chunking (AI-powered meaning-based splits)
"""

import os
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter
)

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
# Sample document (deliberately long)
# ========================================
document = """
Retrieval Augmented Generation (RAG) is a powerful technique for enhancing Large Language Models.
It works by combining information retrieval with text generation. This approach has several benefits.

First, RAG helps reduce hallucinations. LLMs sometimes make up facts that sound plausible but are incorrect.
By retrieving actual documents and using them as context, the model stays grounded in factual information.
This is especially important in domains like healthcare, legal, and finance where accuracy is critical.

Second, RAG provides up-to-date information. LLMs are trained on data up to a certain cutoff date.
They don't know about events or information after that date. RAG solves this by retrieving current documents.
Your knowledge base can be updated daily, and the LLM will use the latest information.

Third, RAG enables domain-specific knowledge. General-purpose LLMs don't know your company's internal docs,
your product specifications, or your customer data. RAG allows you to create a knowledge base from your own
documents and have the LLM answer questions using that specific knowledge.

The RAG pipeline has two main phases. The indexing phase happens once: you split documents into chunks,
create embeddings for each chunk, and store them in a vector database. The query phase happens every time
a user asks a question: you embed the question, find similar chunks, and pass them to the LLM as context.

Choosing the right chunk size is crucial. Too small, and you lose context. Too large, and irrelevant
information gets included. A good rule of thumb is 200-500 tokens per chunk with 10-20% overlap.
But the optimal size depends on your documents and use case. Always evaluate with real queries!
"""

print("📄 Original Document:")
print("-" * 70)
print(document)
print("-" * 70)
print(f"Length: {len(document)} characters, ~{len(document.split())} words\n")

# ========================================
# STRATEGY 1: Fixed-Size Chunking
# ========================================
print("\n" + "="*70)
print("🔪 STRATEGY 1: Fixed-Size Chunking")
print("="*70)
print("Split every N characters, regardless of sentence boundaries")

fixed_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separator=" ",  # Split on spaces
    length_function=len
)

fixed_chunks = fixed_splitter.split_text(document)

print(f"\n✅ Created {len(fixed_chunks)} chunks\n")
for i, chunk in enumerate(fixed_chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(f"'{chunk.strip()}'")
    print()

print("📊 ANALYSIS:")
print("✅ Pros: Simple, fast, uniform chunk sizes")
print("❌ Cons: Can split mid-sentence, loses meaning")
print("🎯 Use case: Simple documents, speed over quality")

# ========================================
# STRATEGY 2: Sentence-Based Chunking
# ========================================
print("\n" + "="*70)
print("🔪 STRATEGY 2: Sentence-Based Chunking")
print("="*70)
print("Split on sentence boundaries (periods, exclamations, questions)")

sentence_splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30,
    separator=". ",  # Split on periods
    length_function=len
)

sentence_chunks = sentence_splitter.split_text(document)

print(f"\n✅ Created {len(sentence_chunks)} chunks\n")
for i, chunk in enumerate(sentence_chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(f"'{chunk.strip()}'")
    print()

print("📊 ANALYSIS:")
print("✅ Pros: Preserves complete thoughts, natural breaks")
print("❌ Cons: Variable chunk sizes, might miss other boundaries")
print("🎯 Use case: Narrative text, articles, documentation")

# ========================================
# STRATEGY 3: Recursive Chunking (RECOMMENDED!)
# ========================================
print("\n" + "="*70)
print("🔪 STRATEGY 3: Recursive Chunking (RECOMMENDED!)")
print("="*70)
print("Try multiple separators in order: paragraphs → sentences → words")

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=25,
    separators=["\n\n", "\n", ". ", " ", ""],  # Priority order
    length_function=len
)

recursive_chunks = recursive_splitter.split_text(document)

print(f"\n✅ Created {len(recursive_chunks)} chunks\n")
for i, chunk in enumerate(recursive_chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(f"'{chunk.strip()}'")
    print()

print("📊 ANALYSIS:")
print("✅ Pros: Smart fallbacks, respects document structure, flexible")
print("✅ Pros: Best balance of meaning preservation and uniform sizes")
print("❌ Cons: Slightly more complex")
print("🎯 Use case: MOST SCENARIOS - this is the best default choice!")

# ========================================
# STRATEGY 4: Token-Based Chunking
# ========================================
print("\n" + "="*70)
print("🔪 STRATEGY 4: Token-Based Chunking")
print("="*70)
print("Split by tokens (not characters) - important for LLM context limits")

# Note: This uses sentence-transformers tokenizer
# For production, use tiktoken for OpenAI or gemini tokenizer
try:
    token_splitter = SentenceTransformersTokenTextSplitter(
        chunk_overlap=10,
        tokens_per_chunk=50  # ~50 tokens per chunk
    )

    token_chunks = token_splitter.split_text(document)

    print(f"\n✅ Created {len(token_chunks)} chunks\n")
    for i, chunk in enumerate(token_chunks, 1):
        # Estimate tokens (rough approximation: 1 token ≈ 4 characters)
        estimated_tokens = len(chunk) // 4
        print(f"Chunk {i} (~{estimated_tokens} tokens, {len(chunk)} chars):")
        print(f"'{chunk.strip()}'")
        print()

    print("📊 ANALYSIS:")
    print("✅ Pros: Respects LLM token limits, accurate counting")
    print("✅ Pros: Critical for models with strict context windows")
    print("❌ Cons: Requires tokenizer library, slightly slower")
    print("🎯 Use case: When you need precise token management")

except Exception as e:
    print(f"⚠️  Token splitter not available: {e}")
    print("Install with: pip install sentence-transformers")

# ========================================
# COMPARISON: Test Retrieval Quality
# ========================================
print("\n" + "="*70)
print("🎯 COMPARISON: Which Chunking Strategy Retrieves Best?")
print("="*70)

# Setup embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)

# Test query
test_query = "How does RAG reduce hallucinations?"
print(f"\n❓ Test Query: '{test_query}'\n")

strategies = [
    ("Fixed-Size", fixed_chunks),
    ("Sentence-Based", sentence_chunks),
    ("Recursive", recursive_chunks),
]

for strategy_name, chunks in strategies:
    print(f"\n{strategy_name} Chunking:")
    print("-" * 50)

    # Create vector store
    texts = [chunk for chunk in chunks if chunk.strip()]
    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        collection_name=f"demo_{strategy_name.lower()}"
    )

    # Retrieve top 2 chunks
    results = vectorstore.similarity_search(test_query, k=2)

    for i, doc in enumerate(results, 1):
        print(f"\n  Result {i}:")
        print(f"  {doc.page_content[:150]}...")

# ========================================
# KEY TAKEAWAYS
# ========================================
print("\n\n" + "="*70)
print("🎓 KEY TAKEAWAYS")
print("="*70)

print("""
1. CHUNKING MATTERS! It's not just splitting text randomly.

2. TRADE-OFFS:
   • Small chunks: More precise, but lose context
   • Large chunks: More context, but include irrelevant info
   • Overlap: Helps preserve context across boundaries

3. RECOMMENDED APPROACH:
   ✅ Start with RecursiveCharacterTextSplitter (Strategy 3)
   ✅ Chunk size: 200-500 tokens (not characters!)
   ✅ Overlap: 10-20% of chunk size
   ✅ Test with real queries and measure retrieval quality

4. DOCUMENT-SPECIFIC:
   • Code: Split on functions/classes (respect structure)
   • Tables: Keep rows together
   • Markdown: Split on headers (##, ###)
   • JSON: Keep objects intact

5. ALWAYS ADD METADATA:
   • Source filename
   • Page number (for PDFs)
   • Section heading
   • Timestamp (for time-sensitive docs)
   → Helps with filtering and attribution!

6. EVALUATE, DON'T GUESS:
   • Try multiple strategies
   • Measure retrieval precision/recall
   • A/B test in production
   • User feedback: "Was this helpful?"
""")

print("\n💡 PRO TIP:")
print("Different document types need different chunking!")
print("Code ≠ Legal docs ≠ Chat logs ≠ Scientific papers")
print("\nBuild a chunking strategy for YOUR data! 🚀")
