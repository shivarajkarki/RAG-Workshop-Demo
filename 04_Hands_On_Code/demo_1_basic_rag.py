"""
Demo 1: Basic RAG - See the Power of RAG!
========================================================

This demo shows the DRAMATIC difference RAG makes! 🚀

PART 1: LLM WITHOUT RAG
- Ask about company info → LLM doesn't know (hallucination or generic answer)

PART 2: LLM WITH RAG
- Add knowledge base → LLM gives EXACT, accurate answers!

This is why RAG is essential for real-world AI applications!
"""

import os
import sys

# ========================================
# WINDOWS FIX: Handle UTF-8 encoding for emojis and special characters
# ========================================
# Without this, Windows console may show garbled text
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ========================================
# IMPORTS: All the RAG components we need
# ========================================
from dotenv import load_dotenv  # To load API key from .env file
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
# GoogleGenerativeAI = The LLM (for answering questions)
# GoogleGenerativeAIEmbeddings = For converting text to vectors

from langchain_community.vectorstores import Chroma  # Vector database (stores embeddings)
from langchain.text_splitter import CharacterTextSplitter  # Splits documents into chunks
from langchain.chains import RetrievalQA  # The RAG chain (combines retrieval + generation)

# ========================================
# SETUP: Load API key from .env file
# ========================================
# Security Best Practice: Never hardcode API keys in source code!
# Instead, store them in .env file (which is in .gitignore)

load_dotenv()  # Reads .env file and loads variables

# Get API key from environment
# This will be None if .env file doesn't exist or key is not set
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
# PART 1: LLM WITHOUT RAG (Baseline)
# ========================================
# TEACHING POINT: Show what happens when LLM doesn't have context
# This demonstrates the "knowledge cutoff" problem
print("="*70)
print("⚡ PART 1: LLM WITHOUT RAG - Showing the Problem")
print("="*70 + "\n")

# Initialize LLM first (without any knowledge base)
print("🤖 Initializing Gemini LLM...")
llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",  # Fast, efficient model
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3  # Low temperature = more focused, less creative
    # Temperature range: 0.0 (deterministic) to 1.0 (very creative)
)
print("✅ LLM ready!\n")

# ========================================
# THE TEST: Ask about information LLM doesn't know
# ========================================
# ACME Corporation was "founded in 2024" - after Gemini's training cutoff
# So the LLM has never seen this information during training
test_question = "What is ACME Corporation's flagship product and what are its pricing plans?"

print(f"❓ Question: {test_question}\n")
print("🤔 Asking LLM directly (WITHOUT RAG)...\n")

try:
    # Call the LLM directly (no retrieval, no context)
    direct_answer = llm.invoke(test_question)

    print("💬 LLM Response (without RAG):")
    print(f"{direct_answer}\n")

    # EXPECTED: LLM will talk about the Looney Tunes ACME company
    # or say it doesn't know, or make up information
    print("❌ PROBLEM: LLM doesn't know ACME! It either:")
    print("   - Makes up information (hallucination)")
    print("   - Gives generic answer (talks about cartoon ACME)")
    print("   - Says 'I don't know'\n")
    print("💡 This is WHY we need RAG - to give LLMs access to real knowledge!\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

print("⏸️  Now let's add RAG and see the magic! ✨\n")
# input("Press Enter to continue...")  # Commented for automated testing
import time
time.sleep(2)  # Brief pause for dramatic effect

# ========================================
# PART 2: LLM WITH RAG - The Solution!
# ========================================
print("\n" + "="*70)
print("🚀 PART 2: LLM WITH RAG - The Solution!")
print("="*70 + "\n")

# ========================================
# STEP 1: Load knowledge base from file
# ========================================
# TEACHING POINT: In production, this could be:
# - Company documentation
# - Product manuals
# - Customer support articles
# - Legal documents
# - Research papers
# Anything you want the LLM to know about!

print("📚 STEP 1: Loading Knowledge Base from file...")

# Read the external knowledge file
knowledge_file = "knowledge_base.txt"

# Safety check: Make sure file exists
if not os.path.exists(knowledge_file):
    print(f"❌ ERROR: {knowledge_file} not found!")
    exit(1)

# Read the entire document
# In production: Could load from database, API, or multiple files
with open(knowledge_file, 'r', encoding='utf-8') as f:
    document_text = f.read()

print(f"✅ Loaded knowledge base ({len(document_text)} characters)\n")
print(f"📄 Knowledge Base Preview:")
print(f"{document_text[:200]}...\n")  # Show first 200 characters

# ========================================
# STEP 2: Split document into chunks
# ========================================
# TEACHING POINT: Why chunk?
# - LLMs have context limits (can't process huge documents)
# - Smaller chunks = more precise retrieval
# - We only retrieve relevant chunks (not entire document)
# - Saves tokens and improves accuracy

print("✂️ STEP 2: Chunking document...")

text_splitter = CharacterTextSplitter(
    chunk_size=500,      # Maximum 500 characters per chunk
    # Rule of thumb: 200-500 tokens (roughly 4 chars = 1 token)

    chunk_overlap=50,    # 50 characters overlap between chunks
    # Why overlap? Preserves context at chunk boundaries
    # Example: If a sentence is split, overlap helps maintain meaning

    separator="\n\n"     # Split on paragraph breaks (natural boundaries)
    # Try to respect document structure, don't split mid-sentence
)

# Create chunk objects from the text
chunks = text_splitter.create_documents([document_text])
print(f"✅ Split into {len(chunks)} chunks\n")
print(f"💡 Each chunk is ~500 characters with 50-char overlap for context\n")

# ========================================
# STEP 3: Create embeddings and store in vector database
# ========================================
# TEACHING POINT: What are embeddings?
# - Convert text to numbers (vectors)
# - Similar meanings → similar vectors
# - Example: "cat" and "kitten" will have similar vectors
# - Enables semantic search (search by meaning, not keywords)

print("🧮 STEP 3: Creating embeddings and vector database...")

# Initialize Gemini embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",  # Gemini's embedding model
    # This model converts text to 768-dimensional vectors
    google_api_key=GOOGLE_API_KEY
)

# Create vector database using ChromaDB
# TEACHING POINT: Vector DB vs Regular DB
# - Regular DB: Exact match (WHERE name = 'ACME')
# - Vector DB: Similarity search (find docs similar to query)
vectorstore = Chroma.from_documents(
    documents=chunks,  # All our document chunks
    embedding=embeddings,  # The embedding model to use
    collection_name="rag_demo"  # Name for this collection
    # Note: This runs in memory (data lost when program ends)
    # For production: Add persist_directory="./chroma_db" to save to disk
)

print("✅ Vector database created with embeddings!\n")
print(f"💡 All {len(chunks)} chunks converted to vectors and stored\n")

# ========================================
# STEP 4: Create RAG chain
# ========================================
# TEACHING POINT: The RAG chain combines everything:
# 1. User asks question
# 2. Question → embedding (vector)
# 3. Find similar chunks in vector DB
# 4. Retrieved chunks + question → LLM
# 5. LLM generates answer based on retrieved context

print("🔗 STEP 4: Building RAG chain...")

# Create the RAG question-answering chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,  # The language model (for generating answers)

    chain_type="stuff",  # How to pass context to LLM
    # "stuff" = put all retrieved chunks into one prompt
    # Other options: "map_reduce", "refine" (for longer contexts)

    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 2}  # Retrieve top 2 most similar chunks
        # k = number of chunks to retrieve
        # Higher k = more context but also more noise
        # Typical range: 2-5 for most use cases
    ),

    return_source_documents=True  # Return which chunks were used
    # Important for transparency and debugging!
)

print("✅ RAG chain ready!\n")
print("💡 Now when we ask questions, the chain will:\n")
print("   1. Find relevant chunks from knowledge base")
print("   2. Pass them as context to the LLM")
print("   3. LLM generates answer based on that context\n")

# ========================================
# STEP 5: Ask the SAME question WITH RAG!
# ========================================
# TEACHING POINT: This is the "WOW" moment!
# Same question, but now the LLM has access to knowledge base
print("="*70)
print("🎯 NOW ASKING WITH RAG!")
print("="*70 + "\n")

# Ask the SAME question again (but with RAG this time)
print(f"❓ Question: {test_question}\n")

# What happens inside this call:
# 1. Question converted to embedding (vector)
# 2. Vector DB finds top 2 most similar chunks
# 3. Retrieved chunks + question combined into prompt
# 4. LLM generates answer using the context
result = qa_chain.invoke({"query": test_question})

print(f"💬 RAG Answer:")
print(f"{result['result']}\n")

# Show which chunks were used (transparency!)
print(f"📄 Sources Used:")
for j, doc in enumerate(result['source_documents'], 1):
    print(f"\nSource {j}:")
    print(f"{doc.page_content[:150]}...")  # Show first 150 chars
    # In production: Also show metadata (file name, page number, etc.)

print("\n✅ SUCCESS! With RAG, the LLM now has accurate, up-to-date information!")
print("💡 Compare this to Part 1 - HUGE difference!\n")

# ========================================
# STEP 6: Ask more questions!
# ========================================
print("="*70)
print("🎯 Let's ask MORE questions!")
print("="*70 + "\n")

# More ACME-specific questions
questions = [
    "What are ACME Corporation's customer success stories?",
    "What training programs does ACME offer and what are the prices?",
    "What is AutoFlow AI's pricing for the Professional plan?",
]

for i, question in enumerate(questions, 1):
    print(f"\n{'='*70}")
    print(f"❓ Question {i}: {question}")
    print('='*70)

    # Get answer from RAG system
    result = qa_chain.invoke({"query": question})

    print(f"\n💬 RAG Answer:")
    print(f"{result['result']}")

    print(f"\n📄 Sources Used:")
    for j, doc in enumerate(result['source_documents'], 1):
        print(f"\n  Source {j}:")
        print(f"  {doc.page_content[:120]}...")  # Show first 120 chars

print("\n" + "="*70)
print("✨ Demo Complete!")
print("="*70)

# ========================================
# KEY TAKEAWAYS
# ========================================
print("\n🎓 KEY TAKEAWAYS:")
print("\n1. WITHOUT RAG:")
print("   ❌ LLM has knowledge cutoff (training data ends at certain date)")
print("   ❌ Doesn't know company-specific or recent information")
print("   ❌ May hallucinate or give generic answers")

print("\n2. WITH RAG:")
print("   ✅ LLM gets access to external knowledge base")
print("   ✅ Answers are grounded in actual documents")
print("   ✅ Can answer about ANY domain (company docs, recent events, etc.)")

print("\n3. HOW RAG WORKS:")
print("   • Load documents → Split into chunks → Create embeddings")
print("   • Store in vector database → Retrieve relevant chunks → Generate answer")

print("\n4. WHY RAG IS ESSENTIAL:")
print("   • Up-to-date information (knowledge base can be updated daily)")
print("   • Domain-specific knowledge (your company, products, policies)")
print("   • Reduces hallucinations (answers based on retrieved facts)")
print("   • Transparency (shows which documents were used)")

print("\n🚀 This is RAG's superpower! Next demos will explore advanced concepts.")
print("\n💡 Try modifying:")
print("   - Edit knowledge_base.txt with your own content")
print("   - Change chunk_size and chunk_overlap")
print("   - Adjust 'k' (number of chunks retrieved)")
print("   - Ask your own questions")
