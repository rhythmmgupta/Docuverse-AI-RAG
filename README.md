🚀 DocuVerse AI - Intelligent Document Analysis & RAG Assistant
📌 Overview

DocuVerse AI is an AI-powered document intelligence platform that enables users to upload PDF documents, interact with them through natural language, generate summaries, extract insights, compare documents, and export professional reports.

The platform leverages Retrieval-Augmented Generation (RAG), Vector Search, Large Language Models (LLMs), and Semantic Retrieval to provide accurate, context-aware responses directly from uploaded documents.

✨ Features
📄 PDF Upload & Processing
Upload PDF documents securely
Automatic text extraction and parsing
Multi-page document support
Built-in PDF viewer
🤖 AI-Powered Document Chat (RAG)

Ask questions directly about uploaded documents.

Example Queries

What is normalization in DBMS?

Explain DNS resolution process.

What are the advantages of indexing?

Capabilities

Context-aware responses
Semantic document retrieval
Source-backed answers
Natural language interaction
📝 Automatic Document Summarization

Generate structured summaries including:

Executive Summary
Key Points
Important Concepts
Action Items
💡 Intelligent Insights Extraction

Automatically extracts:

Important Topics
Key Concepts
Organizations
Dates
Risks
Critical Information
🔍 Semantic Search

Search documents using natural language instead of exact keywords.

Example

Find references related to database security.
📚 Multi-Document Management
Upload multiple PDFs
Switch between documents
Maintain separate document contexts
Individual vector indexing
⚖️ Document Comparison

Compare two uploaded documents and identify:

Similarities
Differences
Shared Concepts
Missing Information
🕒 Chat History
Stores previous questions
Maintains AI responses
Supports contextual follow-up queries
📤 Export Professional Reports

Generate downloadable PDF reports containing:

Document Summary
Extracted Insights
Question History
AI Responses
🛠️ Tech Stack
Frontend
HTML5
CSS3
JavaScript
Backend
FastAPI
Python
AI & RAG
LangChain
Groq LLM
ChromaDB
HuggingFace Embeddings
Sentence Transformers
PDF Processing
PyPDFLoader
Recursive Character Text Splitter
Report Generation
ReportLab
🏗️ System Architecture
                +----------------------+
                |      User UI         |
                | HTML/CSS/JS Frontend |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      FastAPI API     |
                +----------+-----------+
                           |
        ---------------------------------------
        |                 |                  |
        v                 v                  v

 +--------------+  +---------------+  +--------------+
 | PDF Upload   |  | AI Services   |  | Export PDF   |
 +--------------+  +---------------+  +--------------+

            |
            v

 +----------------------+
 | PDF Text Extraction  |
 |      PyPDFLoader     |
 +----------+-----------+
            |
            v

 +----------------------+
 | Text Chunking        |
 | Recursive Splitter   |
 +----------+-----------+
            |
            v

 +----------------------+
 | HuggingFace          |
 | Embedding Model      |
 +----------+-----------+
            |
            v

 +----------------------+
 | ChromaDB             |
 | Vector Database      |
 +----------+-----------+
            |
            v

 +----------------------+
 | Semantic Retriever   |
 +----------+-----------+
            |
            v

 +----------------------+
 | Groq LLM             |
 +----------+-----------+
            |
            v

 +----------------------+
 | AI Generated Answer  |
 +----------------------+
🔄 RAG Workflow
Step 1: Upload PDF
PDF → Text Extraction
Step 2: Chunk Creation
Document → Smaller Chunks
Step 3: Embedding Generation
Text Chunk → Vector Embedding
Step 4: Chroma Indexing
Embeddings → ChromaDB
Step 5: User Query
Question → Semantic Search
Step 6: Retrieval
Relevant Chunks Retrieved
Step 7: LLM Reasoning
Context + Question → Groq LLM
Step 8: Response Generation
Accurate AI Answer
📂 Project Structure
DocuVerse-AI
│
├── backend
│   ├── main1.py
│   └── services
│       └── export_service.py
│
├── frontend
│   ├── front_end1.html
│   ├── style.css
│   ├── app.js
│   └── Ui.js
│
├── uploads
├── db
│
├── requirements.txt
├── .env
└── README.md
🚀 Running Locally
1️⃣ Clone Repository
git clone https://github.com/Rudraksh-2005/Docuverse-AI-RAG.git

cd Docuverse-AI-RAG
2️⃣ Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create Environment File

Create a .env file in the project root.

GROQ_API_KEY=your_groq_api_key

Get your API key from:

Groq Console

5️⃣ Run Backend

From the project root:

python -m uvicorn backend.main1:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
6️⃣ Run Frontend

Open a new terminal:

cd frontend

python -m http.server 5500

Open:

http://localhost:5500/front_end1.html
7️⃣ Start Using DocuVerse AI
Upload PDF
Upload any PDF document
Automatic indexing begins
Generate Summary
Click Summary
AI creates structured overview
Extract Insights
Click Insights
AI extracts key information
Ask Questions
What is normalization?

Explain DNS resolution process.

Summarize Chapter 3.
Compare Documents
Upload multiple PDFs
Select Compare
Analyze similarities and differences
Export Report
Generate professional PDF reports
Download document analysis
🔮 Future Enhancements
User Authentication
Cloud Storage Integration
OCR for Scanned PDFs
Citation-Based Responses
Real-Time Collaboration
Azure/OpenAI Embeddings
Persistent Vector Database
Multi-User Workspaces
Cloud Deployment Support
