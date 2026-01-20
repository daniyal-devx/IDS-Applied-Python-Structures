#!/usr/bin/env python3
"""
Verification Script
Checks that all required files are present and properly configured
"""

import os
import sys


def check_file_exists(filepath, required=True):
    """Check if file exists"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    req_text = "(REQUIRED)" if required else "(optional)"
    print(f"{status} {filepath} {req_text}")
    return exists


def verify_project_structure():
    """Verify all required files and directories exist"""
    
    print("=" * 80)
    print("InsightForge AI - Project Verification")
    print("=" * 80)
    
    all_good = True
    
    # Core files
    print("\n📁 Core Files:")
    all_good &= check_file_exists("app.py", required=True)
    all_good &= check_file_exists("requirements.txt", required=True)
    all_good &= check_file_exists("apt.txt", required=True)
    all_good &= check_file_exists("README.md", required=True)
    all_good &= check_file_exists("LICENSE", required=False)
    
    # Core modules
    print("\n📦 Core Modules:")
    all_good &= check_file_exists("core/__init__.py", required=True)
    all_good &= check_file_exists("core/pdf_loader.py", required=True)
    all_good &= check_file_exists("core/chunking.py", required=True)
    all_good &= check_file_exists("core/embeddings.py", required=True)
    all_good &= check_file_exists("core/vector_store.py", required=True)
    all_good &= check_file_exists("core/rag_pipeline.py", required=True)
    
    # Utils modules
    print("\n🔧 Utilities:")
    all_good &= check_file_exists("utils/__init__.py", required=True)
    all_good &= check_file_exists("utils/memory.py", required=True)
    all_good &= check_file_exists("utils/logger.py", required=True)
    
    # UI files
    print("\n🎨 UI:")
    all_good &= check_file_exists("ui/styles.css", required=True)
    
    # Documentation
    print("\n📚 Documentation:")
    all_good &= check_file_exists("DEPLOYMENT.md", required=False)
    all_good &= check_file_exists("ASSIGNMENT_REPORT.md", required=False)
    all_good &= check_file_exists(".gitignore", required=False)
    
    # Check requirements.txt content
    print("\n📋 Checking requirements.txt:")
    try:
        with open("requirements.txt", 'r') as f:
            reqs = f.read()
            required_packages = [
                "gradio",
                "groq",
                "PyMuPDF",
                "langchain",
                "sentence-transformers",
                "faiss-cpu"
            ]
            for pkg in required_packages:
                if pkg in reqs:
                    print(f"✅ {pkg} found")
                else:
                    print(f"❌ {pkg} missing")
                    all_good = False
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        all_good = False
    
    # Check environment
    print("\n🔐 Environment Variables:")
    groq_key = os.environ.get("GROQ_API_KEY")
    if groq_key:
        print(f"✅ GROQ_API_KEY is set (length: {len(groq_key)})")
    else:
        print("⚠️  GROQ_API_KEY not set (required for deployment)")
        print("   Set it with: export GROQ_API_KEY='your-key-here'")
    
    # Summary
    print("\n" + "=" * 80)
    if all_good:
        print("✅ All required files present!")
        print("✅ Project structure is correct!")
        print("\nNext steps:")
        print("1. Set GROQ_API_KEY environment variable")
        print("2. Run: python app.py")
        print("3. Open browser to: http://localhost:7860")
        print("4. Or deploy to Hugging Face Spaces (see DEPLOYMENT.md)")
    else:
        print("❌ Some required files are missing!")
        print("Please ensure all files are in place before deployment.")
    print("=" * 80)
    
    return all_good


if __name__ == "__main__":
    success = verify_project_structure()
    sys.exit(0 if success else 1)
