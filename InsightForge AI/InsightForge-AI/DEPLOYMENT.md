# 🚀 Deployment Guide - Hugging Face Spaces

## Prerequisites

Before deploying, ensure you have:

1. ✅ A Hugging Face account ([Sign up here](https://huggingface.co/join))
2. ✅ A Groq API key ([Get one here](https://console.groq.com))
3. ✅ Git installed on your machine
4. ✅ All project files ready

---

## Step-by-Step Deployment

### 1. Create a New Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click the **"Create new Space"** button
3. Fill in the details:
   - **Owner**: Your username or organization
   - **Space name**: `insightforge-ai` (or your preferred name)
   - **License**: MIT
   - **Select the Space SDK**: Choose **Gradio**
   - **Space hardware**: CPU (basic) - Free tier is sufficient
   - **Visibility**: Public or Private (your choice)
4. Click **"Create Space"**

### 2. Clone the Space Repository

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/insightforge-ai
cd insightforge-ai
```

### 3. Copy Project Files

Copy all files from the InsightForge-AI directory to your Space:

```bash
# From the InsightForge-AI directory
cp -r * /path/to/insightforge-ai/
cd /path/to/insightforge-ai/
```

### 4. Verify File Structure

Ensure your Space has this structure:

```
insightforge-ai/
├── app.py
├── requirements.txt
├── apt.txt
├── README.md
├── .gitignore
├── core/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── ui/
│   └── styles.css
└── utils/
    ├── __init__.py
    ├── memory.py
    └── logger.py
```

### 5. Configure Secrets

1. Go to your Space on Hugging Face
2. Click on **Settings** (gear icon)
3. Scroll to **Repository secrets**
4. Click **"New secret"**
5. Add:
   - **Name**: `GROQ_API_KEY`
   - **Value**: Your Groq API key
6. Click **"Add secret"**

### 6. Commit and Push

```bash
# Add all files
git add .

# Commit with message
git commit -m "Initial deployment of InsightForge AI"

# Push to Hugging Face
git push
```

### 7. Wait for Build

- Hugging Face will automatically start building your Space
- This may take 5-10 minutes for first deployment
- Monitor the build logs in the Space interface
- The Space will download sentence-transformers model (~90MB) on first run

### 8. Verify Deployment

Once built, your Space will be live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/insightforge-ai
```

Test the deployment:
1. Upload a sample PDF
2. Process the document
3. Ask a test question
4. Verify the response includes citations

---

## 🔧 Configuration Options

### Adjust Space Hardware

If experiencing performance issues:

1. Go to Space **Settings**
2. Under **Space hardware**, select a higher tier:
   - **CPU basic**: Free (default)
   - **CPU upgrade**: $0.03/hour (4 vCPU, 16GB RAM)
   - **T4 small**: $0.60/hour (GPU-accelerated)

### Environment Variables

You can add additional environment variables in **Settings → Repository secrets**:

| Variable | Purpose | Required |
|----------|---------|----------|
| `GROQ_API_KEY` | Groq API authentication | ✅ Yes |
| `HF_TOKEN` | Hugging Face API (if needed) | ❌ No |

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Build fails with "No module named 'core'"
- **Solution**: Ensure `__init__.py` files exist in `core/` and `utils/` directories

**Issue**: "GROQ_API_KEY not set" error
- **Solution**: Double-check the secret name is exactly `GROQ_API_KEY` (case-sensitive)

**Issue**: PDF upload fails
- **Solution**: Verify `apt.txt` contains required system libraries

**Issue**: Slow first load
- **Solution**: Normal - the sentence-transformers model downloads on first run

**Issue**: Out of memory errors
- **Solution**: Upgrade to CPU upgrade tier or optimize chunk size

---

## 📊 Monitoring

### View Logs

1. Click on **Logs** tab in your Space
2. Monitor real-time application logs
3. Check for errors or warnings

### Usage Analytics

InsightForge AI includes built-in analytics:
- Click **"📊 View Analytics"** in the sidebar
- See query counts, success rates, and patterns

---

## 🔄 Updates and Maintenance

### Updating Your Space

```bash
# Make changes to your local files
# Then commit and push
git add .
git commit -m "Update: description of changes"
git push
```

The Space will automatically rebuild with your changes.

### Rollback

If you need to rollback:

1. Go to **Files** tab in your Space
2. Click **"View repository history"**
3. Select a previous commit
4. Click **"Revert to this version"**

---

## 🎯 Best Practices

1. **Test Locally First**: Always test changes locally before pushing
2. **Monitor Costs**: Keep an eye on Space usage if using paid tiers
3. **Version Control**: Use meaningful commit messages
4. **Security**: Never commit API keys or secrets to git
5. **Documentation**: Keep README updated with changes

---

## 📞 Support

If you encounter issues:

- 📖 [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- 💬 [Hugging Face Forums](https://discuss.huggingface.co/)
- 🐛 [Report Issues](https://github.com/yourusername/insightforge-ai/issues)

---

## ✅ Deployment Checklist

Before marking deployment complete, verify:

- [ ] Space is accessible via public URL
- [ ] PDF upload and processing works
- [ ] Questions generate responses with citations
- [ ] Summary generation functions correctly
- [ ] Chat history export works
- [ ] Analytics display properly
- [ ] UI renders correctly (dark theme, spacing, etc.)
- [ ] No error messages in logs
- [ ] All secrets configured correctly
- [ ] README displays properly

---

**Congratulations! Your InsightForge AI platform is now live! 🎉**
