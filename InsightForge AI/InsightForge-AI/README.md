# ⚡ InsightForge AI - Enterprise Knowledge Intelligence Platform

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-brightgreen)
![Status](https://img.shields.io/badge/status-production-success)

**Production-ready RAG system for enterprise document intelligence**

[Features](#features) • [Architecture](#architecture) • [Installation](#installation) • [Usage](#usage) • [Deployment](#deployment)

</div>

---

## 🎯 Overview

InsightForge AI is an enterprise-grade Retrieval-Augmented Generation (RAG) platform that transforms static documents into interactive knowledge bases. Built for consultants, decision-makers, and knowledge workers who need instant, accurate insights from complex document collections.

### Why InsightForge AI?

- **Production-Ready**: Clean architecture, error handling, logging, and monitoring
- **Enterprise-Grade UI**: Professional dark theme with intuitive interface
- **Intelligent Retrieval**: FAISS-powered vector search with semantic understanding
- **Contextual Conversations**: Multi-turn dialogue with conversation memory
- **Source Citations**: Every answer includes page-level references
- **Flexible Modes**: Executive summaries or technical deep-dives

---

## ✨ Features

### Core Capabilities

- **📁 Multi-Document Processing**: Upload and analyze multiple PDF documents simultaneously
- **🧠 Advanced RAG Pipeline**: State-of-the-art retrieval with sentence-transformers embeddings
- **💬 Conversational AI**: Context-aware multi-turn conversations powered by Groq LLMs
- **📊 Auto-Summarization**: Generate executive or technical summaries on-demand
- **🔍 Source Attribution**: Every answer cites specific pages and documents
- **📥 Export Functionality**: Download complete chat history in Text or JSON format
- **📈 Query Analytics**: Monitor usage patterns and success rates

### Technical Excellence

- **Semantic Chunking**: LangChain RecursiveCharacterTextSplitter for optimal context windows
- **Vector Search**: FAISS with normalized embeddings for fast, accurate retrieval
- **LLM Integration**: Groq API with llama-3.1-70b-versatile model
- **Conversation Memory**: Maintains context across interactions
- **Production Logging**: Comprehensive logging for debugging and monitoring
- **Error Handling**: Graceful degradation with user-friendly error messages

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface (Gradio)                  │
├─────────────────────────────────────────────────────────────┤
│                      Application Layer                       │
│  ┌────────────┐  ┌────────────┐  ┌─────────────────────┐  │
│  │  PDF Loader │  │  Chunking  │  │  Embedding Generator │  │
│  └────────────┘  └────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                     Storage & Retrieval                      │
│  ┌────────────────────┐  ┌──────────────────────────────┐  │
│  │  Vector Store       │  │  Conversation Memory         │  │
│  │  (FAISS Index)      │  │  (In-Memory History)         │  │
│  └────────────────────┘  └──────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                      RAG Pipeline                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Retrieval → Context Assembly → LLM Generation       │   │
│  │              (Groq API)                              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Gradio 4.44 | Enterprise UI with custom theming |
| **PDF Processing** | PyMuPDF (fitz) | Fast, accurate text extraction |
| **Chunking** | LangChain | Semantic text splitting |
| **Embeddings** | sentence-transformers | all-MiniLM-L6-v2 model |
| **Vector DB** | FAISS | High-performance similarity search |
| **LLM** | Groq API | llama-3.1-70b-versatile |
| **Memory** | Custom | Conversation history management |

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Groq API key ([Get one here](https://console.groq.com))
- 4GB+ RAM (8GB recommended)
- Linux/macOS/Windows

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/insightforge-ai.git
cd insightforge-ai
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**
```bash
export GROQ_API_KEY="your-api-key-here"
```

5. **Run the application**
```bash
python app.py
```

6. **Open browser**
Navigate to `http://localhost:7860`

---

## 🚀 Usage

### Quick Start Guide

1. **Upload Documents**: Click "Upload PDFs" and select one or more PDF files
2. **Process**: Click "🚀 Process Documents" to extract and index content
3. **Ask Questions**: Type your question and press Enter or click "Send"
4. **Get Summary**: Click "Generate Summary" for document overview
5. **Export**: Download your conversation history anytime

### Answer Modes

- **Executive Mode**: High-level strategic insights, business implications
- **Technical Mode**: Detailed analysis, methodologies, specifications

### Best Practices

- **Document Quality**: Use well-formatted PDFs with clear text (avoid scanned images)
- **Question Style**: Be specific and context-aware
- **Follow-ups**: Leverage conversation memory for multi-turn dialogue
- **Citations**: Check source references to verify information

---

## ☁️ Deployment

### Hugging Face Spaces

1. **Create a new Space**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Gradio" as SDK

2. **Upload files**
```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME
cp -r /path/to/insightforge-ai/* .
git add .
git commit -m "Initial deployment"
git push
```

3. **Set secrets**
   - Go to Space Settings → Repository Secrets
   - Add: `GROQ_API_KEY` with your API key

4. **Configure**
   - Ensure `requirements.txt` and `apt.txt` are in root directory
   - Check `app.py` is the entry point

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Your Groq API key for LLM access |

---

## 📊 Project Structure

```
InsightForge-AI/
│
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── apt.txt                    # System dependencies
│
├── core/                      # Core business logic
│   ├── pdf_loader.py          # PDF processing with PyMuPDF
│   ├── chunking.py            # Semantic text chunking
│   ├── embeddings.py          # Sentence-transformer embeddings
│   ├── vector_store.py        # FAISS vector storage
│   └── rag_pipeline.py        # RAG orchestration + Groq LLM
│
├── ui/                        # User interface
│   └── styles.css             # Midnight Intelligence theme
│
├── utils/                     # Utilities
│   ├── memory.py              # Conversation memory
│   └── logger.py              # Logging and analytics
│
└── README.md                  # This file
```

---

## 🎨 UI Design

### Midnight Intelligence Theme

The UI features a carefully crafted dark theme designed for extended use:

- **Color Palette**: Deep slate backgrounds with blue/cyan accents
- **Typography**: Inter font family for clarity
- **Spacing**: Consistent padding and margins
- **Interactions**: Smooth transitions and hover effects
- **Accessibility**: High contrast ratios and semantic HTML

---

## 🔧 Advanced Features

### 1. Cross-Document Reasoning
The system can synthesize information across multiple documents, identifying patterns and connections.

### 2. Citation Highlighting
Every answer includes source references with page numbers and relevance scores.

### 3. Conversational Context
Maintains conversation history for contextual follow-up questions.

### 4. Export Options
Download complete chat history in Text or JSON format for record-keeping.

### 5. Query Analytics
Monitor usage patterns, success rates, and question characteristics.

---

## 📈 Performance

### Benchmarks (Typical Usage)

| Metric | Value |
|--------|-------|
| **Document Processing** | ~2-5 seconds per PDF |
| **Embedding Generation** | ~1-2 seconds for 100 chunks |
| **Vector Search** | <100ms for k=5 retrieval |
| **LLM Response** | 2-4 seconds (depends on Groq) |
| **Total Latency** | 3-6 seconds end-to-end |

### Scalability

- **Documents**: Tested with 50+ PDFs
- **Chunks**: Handles 10,000+ chunks efficiently
- **Memory**: ~2-4GB RAM for typical workloads
- **Concurrent Users**: Supports multiple simultaneous users

---

## 🛠️ Troubleshooting

### Common Issues

**Problem**: "GROQ_API_KEY not set"
- **Solution**: Set environment variable before running: `export GROQ_API_KEY="your-key"`

**Problem**: PDF extraction fails
- **Solution**: Ensure PDFs contain actual text (not scanned images)

**Problem**: Out of memory errors
- **Solution**: Reduce chunk_size in `app.py` or process fewer documents

**Problem**: Slow embedding generation
- **Solution**: First run downloads model (~90MB), subsequent runs are faster

---

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- [ ] Support for more file formats (DOCX, TXT, etc.)
- [ ] Multi-modal support (images, tables)
- [ ] Advanced chunking strategies
- [ ] Custom embedding models
- [ ] User authentication
- [ ] Cloud storage integration
- [ ] Real-time collaboration

---

## 📄 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

- **Groq**: Fast LLM inference
- **LangChain**: RAG framework
- **Sentence-Transformers**: Embedding models
- **FAISS**: Vector similarity search
- **Gradio**: Rapid UI development
- **PyMuPDF**: PDF processing

---

## 📞 Support

For issues, questions, or feature requests:

- 📧 Email: support@insightforge.ai
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/insightforge-ai/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/insightforge-ai/discussions)

---

<div align="center">

**Built with ⚡ by InsightForge Team**

*Transforming Documents into Intelligence*

</div>
