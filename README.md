# 🚀 DocuVerse AI

> AI-Powered Document Intelligence Platform using RAG, FastAPI, Groq LLM, ChromaDB, and LangChain.

---

## 📖 Overview

DocuVerse AI is an intelligent document analysis platform that enables users to upload PDF documents, interact with them using natural language, generate summaries, extract insights, compare documents, and export professional reports.

The project leverages **Retrieval-Augmented Generation (RAG)** to provide context-aware answers grounded in uploaded documents.

---

## ✨ Features

| Feature | Description |
|----------|------------|
| 📄 PDF Upload | Upload and process PDF documents |
| 👀 PDF Viewer | Built-in document preview |
| 🤖 AI Chat | Ask questions about uploaded documents |
| 📝 Summary Generation | Generate structured document summaries |
| 💡 Insights Extraction | Extract key information automatically |
| 🔍 Semantic Search | Search documents using natural language |
| 📚 Multi-Document Support | Manage multiple uploaded PDFs |
| ⚖️ Document Comparison | Compare two documents side-by-side |
| 🕒 Chat History | Store previous interactions |
| 📤 Export Reports | Generate downloadable PDF reports |

---

# 🏗️ System Architecture

```text
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
 | Embeddings           |
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
 | Retriever            |
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
```

---

# 🔄 RAG Workflow

## Step 1: Upload PDF

```text
PDF → Text Extraction
```

## Step 2: Chunk Creation

```text
Document → Smaller Chunks
```

## Step 3: Embedding Generation

```text
Chunks → Vector Embeddings
```

## Step 4: Vector Storage

```text
Embeddings → ChromaDB
```

## Step 5: User Query

```text
Question → Retriever
```

## Step 6: Context Retrieval

```text
Relevant Chunks Retrieved
```

## Step 7: LLM Processing

```text
Context + Question → Groq LLM
```

## Step 8: Response Generation

```text
Accurate AI Answer
```

---

# 🛠️ Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- FastAPI
- Python

## AI & RAG

- LangChain
- Groq LLM
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

## PDF Processing

- PyPDFLoader
- Recursive Character Text Splitter

## Report Generation

- ReportLab

---

# 📂 Project Structure

```text
DocuVerse-AI
│
├── backend
│   ├── main1.py
│   ├── services
│   │   └── export_service.py
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
```

---

# 🚀 Running Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Rudraksh-2005/Docuverse-AI-RAG.git

cd Docuverse-AI-RAG
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment File

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API Key from:

https://console.groq.com/keys

---

## 5️⃣ Run Backend

From the project root:

```bash
python -m uvicorn backend.main1:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 6️⃣ Run Frontend

Open a new terminal:

```bash
cd frontend

python -m http.server 5500
```

Open in browser:

```text
http://localhost:5500/front_end1.html
```

---

# 🎯 How To Use

## Upload PDF

- Click **Upload Document**
- Select a PDF file
- Automatic indexing begins

## Generate Summary

- Click **Summary**
- Receive a structured AI-generated summary

## Extract Insights

- Click **Insights**
- View important concepts and key information

## Ask Questions

Example:

```text
What is normalization?

Explain DNS resolution process.

Summarize Chapter 4.
```

## Compare Documents

- Upload multiple documents
- Select Compare
- Analyze similarities and differences

## Export Report

- Generate professional PDF reports
- Download analysis results

---

# 🔮 Future Enhancements

- User Authentication
- Cloud Storage Integration
- OCR Support for Scanned PDFs
- Citation-Based Answers
- Azure/OpenAI Embeddings
- Multi-User Workspaces
- Real-Time Collaboration
- Cloud Deployment

---

# 👨‍💻 Author

**Rudraksh Agrawal**

AI • RAG Systems • FastAPI • LangChain • Full Stack Development • Vector Databases • Cloud Technologies

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.
