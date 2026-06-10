"""
Create Kahoot-ready Excel files for all 4 quizzes
Format: Question | Answer 1 (Correct) | Answer 2 | Answer 3 | Answer 4 | Time | Points
"""

import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd

# Quiz 1: RAG Basics
quiz1_data = [
    {
        'Question': 'What does RAG stand for?',
        'Answer 1': 'Retrieval Augmented Generation',
        'Answer 2': 'Rapid AI Generation',
        'Answer 3': 'Random Access Generation',
        'Answer 4': 'Recursive Algorithm Generator',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Which problem does RAG primarily solve?',
        'Answer 1': 'Reducing hallucinations and providing up-to-date information',
        'Answer 2': 'Making LLMs run faster',
        'Answer 3': 'Making LLMs smaller',
        'Answer 4': 'Training LLMs from scratch',
        'Time (seconds)': 45,
        'Points': 1000
    },
    {
        'Question': 'RAG has two main phases. What are they?',
        'Answer 1': 'Indexing and Query',
        'Answer 2': 'Training and Testing',
        'Answer 3': 'Reading and Writing',
        'Answer 4': 'Input and Output',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'In the Indexing phase, what do we NOT do?',
        'Answer 1': 'Answer user questions',
        'Answer 2': 'Split documents into chunks',
        'Answer 3': 'Create embeddings',
        'Answer 4': 'Store in vector database',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'True or False: RAG requires retraining the LLM on new data',
        'Answer 1': 'False',
        'Answer 2': 'True',
        'Answer 3': 'Only sometimes',
        'Answer 4': 'Depends on the data',
        'Time (seconds)': 20,
        'Points': 1000
    },
    {
        'Question': 'Which analogy best describes RAG?',
        'Answer 1': 'Open book exam (can reference materials)',
        'Answer 2': 'Closed book exam (memory only)',
        'Answer 3': 'Pop quiz (unexpected)',
        'Answer 4': 'Group project (collaborate)',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'What is the role of the vector database in RAG?',
        'Answer 1': 'Store and search embeddings for relevant documents',
        'Answer 2': 'Store the LLM weights',
        'Answer 3': 'Train the embedding model',
        'Answer 4': 'Generate the final answer',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'In the paper exercise, Sheet B was easier because:',
        'Answer 1': 'Information was organized with metadata (like RAG!)',
        'Answer 2': 'It had fewer words',
        'Answer 3': 'It was printed in larger font',
        'Answer 4': 'The questions were different',
        'Time (seconds)': 30,
        'Points': 1000
    }
]

# Quiz 2: Chunking
quiz2_data = [
    {
        'Question': 'Why is chunking necessary for RAG?',
        'Answer 1': 'LLMs cannot read entire documents at once',
        'Answer 2': 'Makes documents look prettier',
        'Answer 3': 'Reduces storage costs',
        'Answer 4': 'Speeds up internet connection',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'What happens if chunks are TOO SMALL?',
        'Answer 1': 'Lose context and meaning',
        'Answer 2': 'Nothing wrong, smaller is always better',
        'Answer 3': 'Vector database crashes',
        'Answer 4': 'LLM generates longer answers',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'What happens if chunks are TOO LARGE?',
        'Answer 1': 'Irrelevant information gets included, confuses the LLM',
        'Answer 2': 'Better results always',
        'Answer 3': 'Faster retrieval',
        'Answer 4': 'More accurate embeddings',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Recommended chunk size for general text:',
        'Answer 1': '200-500 tokens',
        'Answer 2': '10-20 tokens',
        'Answer 3': '50-100 tokens',
        'Answer 4': '5000+ tokens',
        'Time (seconds)': 20,
        'Points': 1000
    },
    {
        'Question': 'What is chunk overlap and why is it useful?',
        'Answer 1': 'Duplicate text between chunks to preserve context across boundaries',
        'Answer 2': 'Error in chunking algorithm',
        'Answer 3': 'Compression technique',
        'Answer 4': 'Method to save storage',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Which chunking strategy is BEST for most scenarios?',
        'Answer 1': 'Recursive chunking',
        'Answer 2': 'Fixed-size chunking',
        'Answer 3': 'Random chunking',
        'Answer 4': 'No chunking, use full documents',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Legal documents where accuracy is CRITICAL - what to prioritize?',
        'Answer 1': 'Precision - use semantic chunking + metadata for attribution',
        'Answer 2': 'Speed - use largest chunks possible',
        'Answer 3': 'Cost - use smallest chunks to save money',
        'Answer 4': 'Simplicity - no chunking needed',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'What is metadata in the context of RAG chunks?',
        'Answer 1': 'Data about data (e.g., source, page number, date)',
        'Answer 2': 'Secret information',
        'Answer 3': 'Embedding dimensions',
        'Answer 4': 'LLM temperature settings',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'For code chunking, best practice is to:',
        'Answer 1': 'Split by function/class boundaries',
        'Answer 2': 'Split every 100 characters',
        'Answer 3': 'Never split code',
        'Answer 4': 'Split randomly',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Recommended chunk overlap percentage:',
        'Answer 1': '10-20%',
        'Answer 2': '0% (no overlap needed)',
        'Answer 3': '50% (half overlap)',
        'Answer 4': '90% (almost complete overlap)',
        'Time (seconds)': 20,
        'Points': 1000
    }
]

# Quiz 3: Vector DB & Retrieval
quiz3_data = [
    {
        'Question': 'What are embeddings in RAG?',
        'Answer 1': 'Numerical representations of text that capture semantic meaning',
        'Answer 2': 'Compressed versions of documents',
        'Answer 3': 'Index numbers for documents',
        'Answer 4': 'File sizes in bytes',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Vector databases enable what type of search?',
        'Answer 1': 'Semantic similarity search',
        'Answer 2': 'Exact keyword match only',
        'Answer 3': 'Alphabetical sorting',
        'Answer 4': 'Random selection',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Which is a popular vector database?',
        'Answer 1': 'ChromaDB',
        'Answer 2': 'MySQL',
        'Answer 3': 'Excel',
        'Answer 4': 'Notepad',
        'Time (seconds)': 20,
        'Points': 1000
    },
    {
        'Question': 'Cosine similarity measures:',
        'Answer 1': 'Angle between vectors (semantic similarity)',
        'Answer 2': 'File size difference',
        'Answer 3': 'Number of words',
        'Answer 4': 'Document age',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'What does "k" in top-k retrieval mean?',
        'Answer 1': 'Number of most similar chunks to retrieve',
        'Answer 2': 'Kilobytes of data',
        'Answer 3': 'Thousand documents',
        'Answer 4': 'Keyword count',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'MMR (Maximal Marginal Relevance) is used for:',
        'Answer 1': 'Getting diverse results (not all similar)',
        'Answer 2': 'Faster search',
        'Answer 3': 'Smaller file sizes',
        'Answer 4': 'Exact matching only',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Metadata filtering in vector search allows you to:',
        'Answer 1': 'Search only within specific categories/sources',
        'Answer 2': 'Delete unwanted results',
        'Answer 3': 'Change vector dimensions',
        'Answer 4': 'Increase search speed always',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'ChromaDB vs FAISS - main difference?',
        'Answer 1': 'ChromaDB easier for prototyping, FAISS faster for production',
        'Answer 2': 'No difference at all',
        'Answer 3': 'FAISS is always better',
        'Answer 4': 'ChromaDB works only on Windows',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Why use similarity threshold in retrieval?',
        'Answer 1': 'Filter out low-quality matches',
        'Answer 2': 'Speed up search',
        'Answer 3': 'Reduce database size',
        'Answer 4': 'Increase number of results',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Hybrid search combines:',
        'Answer 1': 'Vector similarity + keyword matching',
        'Answer 2': 'Two different LLMs',
        'Answer 3': 'Multiple databases',
        'Answer 4': 'SQL and NoSQL',
        'Time (seconds)': 30,
        'Points': 1000
    }
]

# Quiz 4: Advanced & Evaluation
quiz4_data = [
    {
        'Question': 'Precision in RAG evaluation measures:',
        'Answer 1': 'Of retrieved docs, how many are relevant?',
        'Answer 2': 'Total number of documents',
        'Answer 3': 'Speed of retrieval',
        'Answer 4': 'Size of answers',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Recall in RAG evaluation measures:',
        'Answer 1': 'Of all relevant docs, how many were retrieved?',
        'Answer 2': 'How fast we retrieve',
        'Answer 3': 'Total database size',
        'Answer 4': 'Answer length',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Faithfulness metric checks if:',
        'Answer 1': 'Answer is based on retrieved documents (no hallucination)',
        'Answer 2': 'Answer is long enough',
        'Answer 3': 'Retrieval was fast',
        'Answer 4': 'User is satisfied',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'RAGAS framework is used for:',
        'Answer 1': 'Automated RAG evaluation',
        'Answer 2': 'Building vector databases',
        'Answer 3': 'Training LLMs',
        'Answer 4': 'Chunking documents',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Production RAG systems MUST have:',
        'Answer 1': 'Logging and monitoring',
        'Answer 2': 'Fancy UI only',
        'Answer 3': 'No error handling needed',
        'Answer 4': 'Largest possible chunks',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Caching in RAG helps with:',
        'Answer 1': 'Reducing costs and improving speed',
        'Answer 2': 'Making answers longer',
        'Answer 3': 'Increasing hallucinations',
        'Answer 4': 'Deleting old data',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'User feedback in RAG is important for:',
        'Answer 1': 'Improving system quality over time',
        'Answer 2': 'Just collecting ratings',
        'Answer 3': 'Slowing down responses',
        'Answer 4': 'Making it complex',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Answer Relevance metric checks if:',
        'Answer 1': 'Answer actually addresses the question asked',
        'Answer 2': 'Answer is grammatically correct',
        'Answer 3': 'Answer is short',
        'Answer 4': 'Retrieval was accurate',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Context Relevance metric checks if:',
        'Answer 1': 'Retrieved chunks are actually useful for answering',
        'Answer 2': 'LLM is fast',
        'Answer 3': 'Database is large',
        'Answer 4': 'User is happy',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'MRR (Mean Reciprocal Rank) measures:',
        'Answer 1': 'How quickly we find the first relevant result',
        'Answer 2': 'Total number of results',
        'Answer 3': 'Database size',
        'Answer 4': 'Answer quality',
        'Time (seconds)': 40,
        'Points': 1000
    },
    {
        'Question': 'Best practice for production RAG:',
        'Answer 1': 'All of the above',
        'Answer 2': 'Log every query',
        'Answer 3': 'Monitor metrics',
        'Answer 4': 'Collect user feedback',
        'Time (seconds)': 30,
        'Points': 1000
    },
    {
        'Question': 'Temperature in LLM controls:',
        'Answer 1': 'Randomness (low=focused, high=creative)',
        'Answer 2': 'Speed of generation',
        'Answer 3': 'Number of tokens',
        'Answer 4': 'Database temperature',
        'Time (seconds)': 30,
        'Points': 1000
    }
]

# Create DataFrames
df_quiz1 = pd.DataFrame(quiz1_data)
df_quiz2 = pd.DataFrame(quiz2_data)
df_quiz3 = pd.DataFrame(quiz3_data)
df_quiz4 = pd.DataFrame(quiz4_data)

# Save to Excel files
print("\n[*] Creating Kahoot-ready Excel files...")
print("-" * 60)

df_quiz1.to_excel('Kahoot_Quiz_1_RAG_Basics.xlsx', index=False)
print("[+] Created: Kahoot_Quiz_1_RAG_Basics.xlsx (8 questions)")

df_quiz2.to_excel('Kahoot_Quiz_2_Chunking.xlsx', index=False)
print("[+] Created: Kahoot_Quiz_2_Chunking.xlsx (10 questions)")

df_quiz3.to_excel('Kahoot_Quiz_3_VectorDB.xlsx', index=False)
print("[+] Created: Kahoot_Quiz_3_VectorDB.xlsx (10 questions)")

df_quiz4.to_excel('Kahoot_Quiz_4_Advanced.xlsx', index=False)
print("[+] Created: Kahoot_Quiz_4_Advanced.xlsx (12 questions)")

print("-" * 60)
print("[+] Done! All 4 Kahoot-ready Excel files created.")
print("\nHOW TO IMPORT TO KAHOOT:")
print("1. Go to kahoot.com and login")
print("2. Create new kahoot")
print("3. Click 'Import' -> 'From spreadsheet'")
print("4. Upload the Excel file")
print("5. Click 'Create' - Done!")
print("\nNote: Answer 1 is always the correct answer in these files.")
print("Kahoot will automatically randomize the answer order when playing.")
