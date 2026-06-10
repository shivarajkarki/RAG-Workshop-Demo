# RAG Workshop - Hands-On Learning Materials

Welcome to the **Retrieval Augmented Generation (RAG)** workshop! This repository contains everything you need to learn and build RAG systems from scratch.

## What You'll Learn

- **RAG Fundamentals**: How RAG combines retrieval with LLM generation
- **Chunking Strategies**: Best practices for splitting documents
- **Vector Databases**: Store and search embeddings efficiently
- **Retrieval Techniques**: Multiple strategies for finding relevant content
- **Evaluation Metrics**: Measure and improve RAG quality
- **Production Systems**: Build real-world RAG applications

## Prerequisites

- **Python 3.8+** installed on your system
- **Google Gemini API Key** (free) - See detailed setup instructions below ⬇️
- Basic Python knowledge (functions, loops, imports)
- Text editor or IDE (VS Code, PyCharm, etc.)

> 💡 **New to Gemini API?** Don't worry! Step-by-step instructions for getting your free API key are in the [Quick Start section](#3-get-your-free-gemini-api-key) below.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/shivarajkarki/RAG-Workshop-Demo.git
cd RAG-Workshop-Demo
```

### 2. Install Dependencies

```bash
cd 04_Hands_On_Code
pip install -r requirements.txt
```

**Required packages:**
- `langchain` - RAG framework
- `langchain-google-genai` - Google Gemini integration
- `langchain-community` - Community integrations
- `chromadb` - Vector database
- `python-dotenv` - Environment variable management

### 3. Get Your Free Gemini API Key

**Step-by-step instructions:**

#### Step 1: Go to Google AI Studio
Visit: https://makersuite.google.com/app/apikey

OR

Visit: https://aistudio.google.com/app/apikey

#### Step 2: Sign In
- Click "Sign in" (top right)
- Use your Google account (Gmail)
- If you don't have one, create a free Google account

#### Step 3: Create API Key
1. Click **"Get API key"** button
2. You'll see two options:
   - **"Create API key in new project"** (recommended for first-time)
   - **"Create API key in existing project"** (if you already have Google Cloud projects)
3. Click **"Create API key in new project"**
4. Wait 2-3 seconds...
5. Your API key will appear! It looks like: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX`

#### Step 4: Copy Your API Key
- Click the **"Copy"** icon next to your key
- **IMPORTANT:** Save it somewhere safe! You can always come back to see it again.

#### Step 5: Set Up Environment File
Create a `.env` file in the `04_Hands_On_Code` directory:

**Option A: Using Command Line**
```bash
# Copy the example file
cp .env.example .env

# Open .env in a text editor and add your key
# Windows: notepad .env
# Mac/Linux: nano .env
```

**Option B: Manually**
1. Open `04_Hands_On_Code` folder
2. Create new file named `.env` (notice the dot at the start!)
3. Add this line:
```
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXX
```
4. Replace with your actual key
5. Save the file

**Important:**
- ✅ Never share your API key publicly
- ✅ Never commit `.env` to git (already in `.gitignore`)
- ✅ If key is compromised, delete it and create a new one

#### Free Tier Limits:
- **60 requests per minute**
- **1,500 requests per day**
- Perfect for learning and small projects!
- Upgrade to paid tier if needed: https://ai.google.dev/pricing

### 4. Run Your First Demo

```bash
python demo_1_basic_rag.py
```

If you see output without errors, you're all set!

## Repository Structure

```
RAGDemo/
├── 01_Paper_Exercise/          # Start here: Paper-based RAG exercise
│   ├── Instructions.md         # Exercise instructions
│   ├── Sheet_A_Unorganized.md  # Unorganized document
│   └── Sheet_B_Chunked.md      # Organized chunks
│
├── 02_Slides/                  # Complete slide deck (51 slides)
│   └── RAG_Complete_Slide_Deck.md
│
├── 03_Quizzes/                 # 4 interactive quizzes
│   ├── Quiz_1_RAG_Basics.md
│   ├── Quiz_2_Chunking.md
│   ├── Quiz_3_VectorDB_and_Retrieval.md
│   └── Quiz_4_Advanced_and_Evaluation.md
│
└── 04_Hands_On_Code/           # 5 Python demos
    ├── demo_1_basic_rag.py                      # Start here
    ├── demo_2_chunking_strategies.py            # Compare chunking methods
    ├── demo_3_vector_storage_and_retrieval.py   # Vector DB & retrieval
    ├── demo_4_evaluation_metrics.py             # Measure quality
    ├── demo_5_complete_rag_system.py            # Production template
    ├── requirements.txt
    └── .env.example
```

## Demos Overview

### Demo 1: Basic RAG
**File:** `demo_1_basic_rag.py`

Learn the RAG workflow:
- Load documents
- Create embeddings
- Store in vector database
- Retrieve relevant chunks
- Generate answers with LLM

**Run time:** ~5 minutes

---

### Demo 2: Chunking Strategies
**File:** `demo_2_chunking_strategies.py`

Compare 4 chunking approaches:
1. Fixed-size chunking
2. Sentence-based chunking
3. Recursive chunking (recommended)
4. Token-based chunking

**Run time:** ~8 minutes

---

### Demo 3: Vector Storage & Retrieval
**File:** `demo_3_vector_storage_and_retrieval.py`

Explore retrieval strategies:
- Cosine Similarity (default)
- Euclidean Distance
- MMR (diverse results)
- Similarity Threshold (quality control)
- Metadata Filtering
- Hybrid Search

**Run time:** ~10 minutes

---

### Demo 4: Evaluation Metrics
**File:** `demo_4_evaluation_metrics.py`

Measure RAG quality:

**Retrieval Metrics:**
- Precision, Recall, F1 Score
- Mean Reciprocal Rank (MRR)
- Hit Rate
- NDCG

**Generation Metrics:**
- Faithfulness
- Answer Relevance
- Context Relevance
- RAGAS Score

**Run time:** ~7 minutes

---

### Demo 5: Production RAG System
**File:** `demo_5_complete_rag_system.py`

Complete production template:
- Configuration management
- Document processing with metadata
- Multiple retrieval strategies
- Comprehensive logging
- Timing metrics
- User feedback collection

**Run time:** ~12 minutes

Use this as a template for your own projects!

## Learning Path

### For Beginners (3-4 hours)
1. Read the slides in `02_Slides/`
2. Try the paper exercise in `01_Paper_Exercise/`
3. Run `demo_1_basic_rag.py`
4. Take Quiz 1 in `03_Quizzes/`
5. Run `demo_2_chunking_strategies.py`
6. Take Quiz 2

### For Intermediate Learners (2-3 hours)
1. Run all 5 demos in order
2. Modify demo parameters (chunk size, top_k, etc.)
3. Complete all 4 quizzes
4. Experiment with your own documents

### For Advanced Learners (4+ hours)
1. Use `demo_5_complete_rag_system.py` as a template
2. Build a RAG system for your use case
3. Add your own documents
4. Implement caching and monitoring
5. Deploy with FastAPI or Streamlit

## Common Issues & Solutions

### Issue 1: API Key Error
```
❌ ERROR: GOOGLE_API_KEY not found!
```
**Solution:** Create `.env` file with your API key (see Quick Start #3)

**Common API Key Problems:**

**Problem:** "API key not found"
- ✅ Check `.env` file exists in `04_Hands_On_Code` folder
- ✅ Check `.env` has: `GOOGLE_API_KEY=your-key-here` (no spaces!)
- ✅ Check no quotes around key: `GOOGLE_API_KEY=AIza...` (not `"AIza..."`)

**Problem:** "Invalid API key"
- ✅ Copy key again from https://aistudio.google.com/app/apikey
- ✅ Make sure you copied the entire key (starts with `AIza`)
- ✅ No extra spaces before or after key

**Problem:** "API key quota exceeded" (429 error)
- ✅ Free tier: 60 requests/min, 1500 requests/day
- ✅ Wait 24 hours for daily quota reset
- ✅ Or upgrade to paid tier: https://ai.google.dev/pricing

**Problem:** "API key not enabled for Gemini"
- ✅ Make sure you created key at https://aistudio.google.com/app/apikey
- ✅ Not Google Cloud Console (different API keys!)
- ✅ Wait 1-2 minutes after creating key (activation time)

---

### Issue 2: Import Errors
```
ModuleNotFoundError: No module named 'langchain'
```
**Solution:**
```bash
pip install -r requirements.txt
```

---

### Issue 3: ChromaDB Warnings
```
Failed to send telemetry event
```
**Solution:** This is just a warning - demos still work fine! ChromaDB tries to send usage stats but it's not required.

---

### Issue 4: UTF-8 Encoding (Windows)
```
UnicodeEncodeError: 'charmap' codec can't encode character
```
**Solution:** Already fixed in all demos with:
```python
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
```

---

### Issue 5: Slow First Run
**Symptom:** First demo takes 2-3 minutes to start

**Solution:** This is normal! The embedding model downloads on first use (~100MB). Subsequent runs are much faster.

## Best Practices

### When Learning
- Run demos in order (1 → 2 → 3 → 4 → 5)
- Read the comments in each file
- Experiment by changing parameters
- Compare outputs with different settings

### When Building Your Own RAG
- Start with `demo_5_complete_rag_system.py` as a template
- Use RecursiveCharacterTextSplitter (most versatile)
- Chunk size: 200-500 tokens with 10-20% overlap
- Always add metadata (source, page, section)
- Measure quality with evaluation metrics
- Log all queries in production

## Resources

### Official Documentation
- **LangChain:** https://python.langchain.com/docs/
- **Google Gemini:** https://ai.google.dev/docs
- **ChromaDB:** https://docs.trychroma.com/

### Further Learning
- **RAG Paper (2020):** https://arxiv.org/abs/2005.11401
- **RAGAS Framework:** https://docs.ragas.io/
- **Vector Database Comparison:** https://benchmark.vectorview.ai/

### Getting Help
- Check the slides in `02_Slides/`
- Review quiz answers after attempting
- Ask your instructor during the workshop
- GitHub Issues: https://github.com/shivarajkarki/RAG-Workshop-Demo/issues

## Project Ideas

Build your own RAG system for:
- **Personal knowledge base** - Index your notes, documents, PDFs
- **Customer support** - Answer questions from product docs
- **Research assistant** - Search academic papers
- **Code documentation** - Query your codebase
- **Study buddy** - Learn from textbooks

## Tips for Success

1. **Don't skip the paper exercise** - It builds intuition before code
2. **Run demos multiple times** - Try different parameters
3. **Read the code comments** - They explain the "why" not just "what"
4. **Complete the quizzes** - They reinforce key concepts
5. **Build something** - Apply what you learned to a real problem

## Contributing

Found a bug? Have a suggestion? Open an issue or submit a pull request!

## License

This workshop material is provided for educational purposes. Feel free to use and modify for learning.

## Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- Vector database by [ChromaDB](https://github.com/chroma-core/chroma)

---

**Happy Learning!** If you complete all 5 demos, you'll have the skills to build production RAG systems. Good luck!
