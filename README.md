# 🚀 AI Study Assistant — RAG Based AI Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

### 📚 Intelligent PDF Question Answering System using Retrieval-Augmented Generation (RAG)

Ask questions from PDFs and get AI-generated answers using semantic search and Large Language Models.

</div>

---

# ✨ Features

✅ PDF Question Answering  
✅ Retrieval-Augmented Generation (RAG)  
✅ Semantic Search using Embeddings  
✅ Vector Database with FAISS  
✅ Hugging Face LLM Integration  
✅ Prompt Engineering  
✅ Clean Modular Architecture  
✅ Fast Retrieval Pipeline  
✅ Easily Scalable System  

---

# 🧠 Problem Statement

Students and users often struggle to search through large PDFs, notes, reports, and documentation manually.

Traditional keyword-based systems:
- Fail to understand context
- Return irrelevant results
- Cannot generate intelligent answers

This project solves the problem using:

> 🔥 Retrieval-Augmented Generation (RAG)

The system retrieves relevant content from uploaded documents and generates context-aware AI responses.

---

# 🏗️ Project Architecture

```text
PDF Documents
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Embeddings Generation
      ↓
FAISS Vector Database
      ↓
Retriever
      ↓
LLM + Prompt Engineering
      ↓
AI Generated Answer
```

---

# 📂 Project Structure

```text
AI-STUDY-ASSISTANT/
│
├── backend/
│   ├── rag_pipeline/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── llm/
│   │   ├── model.py
│   │   └── prompt.py
│   │
│   ├── api/
│   └── utils/
│
├── data/
│   ├── raw_pdfs/
│   └── processed_chunks/
│
├── vector_db/
├── notebooks/
├── report/
│
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| RAG Framework | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| LLM | Hugging Face Transformers |
| PDF Processing | PyPDF |
| Version Control | Git + GitHub |

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-study-assistant-rag.git
cd ai-study-assistant-rag
```

---

## 2️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 Add PDF Files

Place your PDFs inside:

```text
data/raw_pdfs/
```

---

# ▶️ Run Project

```bash
python backend/main.py
```

---

# 🧪 Example Query

```text
Question:
What is the purpose of the system?
```

### 🤖 Output

```text
The system is designed to automate and manage operations efficiently using AI-powered retrieval and response generation.
```

---

# 🔍 How RAG Works

## Step 1 — Load Documents
PDFs are loaded using document loaders.

## Step 2 — Split Text
Large documents are divided into smaller chunks.

## Step 3 — Create Embeddings
Each chunk is converted into vector embeddings.

## Step 4 — Store in Vector DB
Embeddings are stored inside FAISS.

## Step 5 — Retrieve Relevant Chunks
Semantic similarity retrieves relevant context.

## Step 6 — Generate AI Answer
LLM generates answers using retrieved context.

---

# 🌟 Unique Features

✅ Context-Aware AI Responses  
✅ Semantic Search Engine  
✅ Modular AI Pipeline  
✅ Academic PDF Question Answering  
✅ Fast Retrieval with FAISS  
✅ Scalable Architecture  

---

# 📈 Future Enhancements

🚀 Chatbot UI  
🚀 Multi-PDF Support  
🚀 Voice Assistant Integration  
🚀 Cloud Deployment  
🚀 AI Quiz Generator  
🚀 User Authentication  

---

# 👨‍💻 Developer

### Sahib Chouhan

BCA (AI & ML) Student  
Generative AI & Full Stack Development Enthusiast

---

# 📜 License

This project is created for educational and learning purposes.

---

<div align="center">

## ⭐ If you like this project, give it a star on GitHub ⭐

</div>