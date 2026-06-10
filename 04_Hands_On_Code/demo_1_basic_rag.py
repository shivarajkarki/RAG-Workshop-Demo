"""
Demo 1: Basic RAG - The Simplest Possible Implementation
========================================================

This is RAG in ~15 lines of code! 🚀

CONCEPT: Retrieval Augmented Generation
- Store documents (knowledge base)
- When user asks a question:
  1. RETRIEVE: Find relevant documents
  2. AUGMENT: Add them to the question as context
  3. GENERATE: LLM answers using that context

Run this demo to see RAG in action!
"""

import os
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# ========================================
# SETUP: Load API key from .env file
# ========================================
# Load environment variables from .env file (if it exists)
load_dotenv()

# Get API key (from .env file or environment variable)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("❌ ERROR: GOOGLE_API_KEY not found!")
    print("\n📝 To fix, choose ONE option:")
    print("\n   Option 1 (Recommended): Create .env file")
    print("   ------------------------")
    print("   1. Create a file named '.env' in this folder")
    print("   2. Add this line: GOOGLE_API_KEY=your-key-here")
    print("   3. Save and run again")
    print("\n   Option 2: Set environment variable")
    print("   ----------------------------------")
    print("   Windows: setx GOOGLE_API_KEY \"your-key-here\"")
    print("   Linux/Mac: export GOOGLE_API_KEY=\"your-key-here\"")
    print("\n🔑 Get your key from: https://makersuite.google.com/app/apikey")
    exit(1)

print("✅ API Key loaded successfully!\n")

# ========================================
# STEP 1: Create sample documents (knowledge base)
# ========================================
print("📚 STEP 1: Creating Knowledge Base...")

documents = [
    """RAG (Retrieval Augmented Generation) is a technique that combines information
    retrieval with text generation. It helps Large Language Models answer questions
    using external knowledge, reducing hallucinations and providing up-to-date information.""",

    """Vector databases store embeddings (numerical representations of text) and enable
    fast similarity search. Popular vector databases include Chroma, FAISS, Pinecone,
    and Weaviate. They use algorithms like HNSW or IVF for approximate nearest neighbor search.""",

    """Chunking is the process of splitting large documents into smaller pieces.
    Good chunking strategies preserve meaning and context. Common chunk sizes are
    200-500 tokens with 20-50 token overlap between chunks.""",

    """Embeddings convert text into high-dimensional vectors. Similar meanings result
    in similar vectors. Gemini's text-embedding-004 model produces 768-dimensional
    embeddings. These vectors capture semantic meaning.""",

    """RAG evaluation uses metrics like Precision, Recall, NDCG for retrieval quality,
    and Faithfulness, Relevance, and Answer Similarity for generation quality.
    RAGAS framework provides end-to-end RAG evaluation."""
]

print(f"✅ Created {len(documents)} documents in our knowledge base\n")

# ========================================
# STEP 2: Split documents into chunks
# ========================================
print("✂️ STEP 2: Chunking documents...")

text_splitter = CharacterTextSplitter(
    chunk_size=200,      # Maximum characters per chunk
    chunk_overlap=20,    # Overlap between chunks for context
    separator="\n"       # Split on newlines when possible
)

chunks = text_splitter.create_documents(documents)
print(f"✅ Split into {len(chunks)} chunks\n")

# ========================================
# STEP 3: Create embeddings and store in vector database
# ========================================
print("🧮 STEP 3: Creating embeddings and vector database...")

# Initialize Gemini embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",  # Correct Gemini embedding model
    google_api_key=GOOGLE_API_KEY
)

# Create vector database using Chroma (stores in memory for this demo)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="rag_demo"
)

print("✅ Vector database created with embeddings!\n")

# ========================================
# STEP 4: Initialize the LLM (Gemini)
# ========================================
print("🤖 STEP 4: Initializing Gemini LLM...")

llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",  # Latest, fastest Gemini model
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3  # Lower temperature = more focused answers
)

print("✅ LLM initialized!\n")

# ========================================
# STEP 5: Create RAG chain
# ========================================
print("🔗 STEP 5: Building RAG chain...")

# This creates a question-answering chain with retrieval
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" means: stuff all retrieved docs into prompt
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),  # Retrieve top 2 chunks
    return_source_documents=True  # Show which documents were used
)

print("✅ RAG chain ready!\n")

# ========================================
# STEP 6: Ask questions!
# ========================================
print("="*60)
print("🎯 RAG SYSTEM IS READY! Let's test it!")
print("="*60 + "\n")

# Test questions
questions = [
    "What is RAG and why is it useful?",
    "What are some popular vector databases?",
    "How should I evaluate a RAG system?",
]

for i, question in enumerate(questions, 1):
    print(f"\n{'='*60}")
    print(f"❓ Question {i}: {question}")
    print('='*60)

    # Get answer from RAG system
    result = qa_chain.invoke({"query": question})

    print(f"\n💬 RAG Answer:")
    print(f"{result['result']}")

    print(f"\n📄 Sources Used:")
    for j, doc in enumerate(result['source_documents'], 1):
        print(f"\n  Source {j}:")
        print(f"  {doc.page_content[:100]}...")  # Show first 100 chars

print("\n" + "="*60)
print("✨ Demo Complete!")
print("="*60)

# ========================================
# KEY TAKEAWAYS
# ========================================
print("\n🎓 KEY TAKEAWAYS:")
print("1. RAG = Retrieval (search) + Augmented (add context) + Generation (LLM answers)")
print("2. Vector DB stores embeddings for fast similarity search")
print("3. Embeddings convert text → numbers that capture meaning")
print("4. Chain combines: Query → Retrieve → Add to prompt → Generate answer")
print("5. Source documents show transparency (which knowledge was used)")

print("\n🚀 This is RAG at its simplest! Next demos will explore advanced concepts.")
print("\n💡 Try modifying:")
print("   - Add your own documents")
print("   - Change chunk_size and chunk_overlap")
print("   - Adjust 'k' (number of chunks retrieved)")
print("   - Try different questions")
