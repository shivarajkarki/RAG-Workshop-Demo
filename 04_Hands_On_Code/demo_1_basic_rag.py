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
# PART 1: LLM WITHOUT RAG (Baseline)
# ========================================
print("="*70)
print("⚡ PART 1: LLM WITHOUT RAG - Showing the Problem")
print("="*70 + "\n")

# Initialize LLM first (without any knowledge base)
print("🤖 Initializing Gemini LLM...")
llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)
print("✅ LLM ready!\n")

# Ask about ACME Corporation (LLM won't know this)
test_question = "What is ACME Corporation's flagship product and what are its pricing plans?"

print(f"❓ Question: {test_question}\n")
print("🤔 Asking LLM directly (WITHOUT RAG)...\n")

try:
    direct_answer = llm.invoke(test_question)
    print("💬 LLM Response (without RAG):")
    print(f"{direct_answer}\n")
    print("❌ PROBLEM: LLM doesn't know ACME! It either:")
    print("   - Makes up information (hallucination)")
    print("   - Gives generic answer")
    print("   - Says 'I don't know'\n")
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
print("📚 STEP 1: Loading Knowledge Base from file...")

# Read the knowledge base document
knowledge_file = "knowledge_base.txt"
if not os.path.exists(knowledge_file):
    print(f"❌ ERROR: {knowledge_file} not found!")
    exit(1)

with open(knowledge_file, 'r', encoding='utf-8') as f:
    document_text = f.read()

print(f"✅ Loaded knowledge base ({len(document_text)} characters)\n")
print(f"📄 Knowledge Base Preview:")
print(f"{document_text[:200]}...\n")

# ========================================
# STEP 2: Split document into chunks
# ========================================
print("✂️ STEP 2: Chunking document...")

text_splitter = CharacterTextSplitter(
    chunk_size=500,      # Larger chunks for detailed content
    chunk_overlap=50,    # Overlap between chunks for context
    separator="\n\n"     # Split on paragraph breaks
)

chunks = text_splitter.create_documents([document_text])
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
# STEP 4: Create RAG chain
# ========================================
print("🔗 STEP 4: Building RAG chain...")

# This creates a question-answering chain with retrieval
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" means: stuff all retrieved docs into prompt
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),  # Retrieve top 2 chunks
    return_source_documents=True  # Show which documents were used
)

print("✅ RAG chain ready!\n")

# ========================================
# STEP 5: Ask the SAME question WITH RAG!
# ========================================
print("="*70)
print("🎯 NOW ASKING WITH RAG!")
print("="*70 + "\n")

# Ask the SAME question again (but with RAG this time)
print(f"❓ Question: {test_question}\n")

result = qa_chain.invoke({"query": test_question})

print(f"💬 RAG Answer:")
print(f"{result['result']}\n")

print(f"📄 Sources Used:")
for j, doc in enumerate(result['source_documents'], 1):
    print(f"\nSource {j}:")
    print(f"{doc.page_content[:150]}...")  # Show first 150 chars

print("\n✅ SUCCESS! With RAG, the LLM now has accurate, up-to-date information!\n")

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
