# 🚀 Quick Start Guide - InsightForge AI

Get up and running in 5 minutes!

## Prerequisites
- Python 3.10+
- Groq API key ([Get free key](https://console.groq.com))

## Installation

### 1. Set up environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API key
```bash
# Linux/Mac
export GROQ_API_KEY="your-groq-api-key-here"

# Windows (Command Prompt)
set GROQ_API_KEY=your-groq-api-key-here

# Windows (PowerShell)
$env:GROQ_API_KEY="your-groq-api-key-here"
```

### 4. Run the application
```bash
python app.py
```

### 5. Open in browser
Navigate to: **http://localhost:7860**

## First Use

1. **Upload Documents**: Click "Upload PDFs" and select your PDF files
2. **Process**: Click "🚀 Process Documents" and wait for completion
3. **Ask Questions**: Type your question in the chat box
4. **Get Summary**: Click "Generate Summary" for document overview
5. **Export**: Download chat history anytime

## Tips
- Start with 2-3 documents for faster processing
- Use Executive mode for business insights
- Use Technical mode for detailed analysis
- Citations show page numbers for verification

## Troubleshooting

**"GROQ_API_KEY not set"**
- Make sure to set the environment variable before running

**"Module not found"**
- Run: `pip install -r requirements.txt`

**Slow first run**
- Normal - downloads AI model (~90MB) on first use

## Need Help?
See full documentation in README.md

---

**Ready to deploy?** See DEPLOYMENT.md for Hugging Face Spaces guide
