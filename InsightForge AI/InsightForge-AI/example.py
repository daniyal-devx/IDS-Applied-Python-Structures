"""
Example Usage Script
Demonstrates core functionality without UI
"""

import os
from core.pdf_loader import PDFLoader
from core.chunking import DocumentChunker
from core.embeddings import EmbeddingGenerator
from core.vector_store import VectorStore
from core.rag_pipeline import RAGPipeline
from utils.logger import setup_logger

# Setup
logger = setup_logger()
logger.info("Starting InsightForge AI example...")

# Simulate PDF files (you would pass actual file objects in production)
# For testing purposes, this script demonstrates the workflow

def demonstrate_workflow():
    """Demonstrate the complete RAG workflow"""
    
    print("=" * 80)
    print("InsightForge AI - Example Workflow")
    print("=" * 80)
    
    # Step 1: Initialize components
    print("\n1. Initializing components...")
    pdf_loader = PDFLoader()
    chunker = DocumentChunker()
    embedding_generator = EmbeddingGenerator()
    
    # Step 2: Check Groq API key
    print("\n2. Checking configuration...")
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        print("❌ GROQ_API_KEY not set. Please set it in environment variables.")
        print("   export GROQ_API_KEY='your-api-key-here'")
        return
    
    rag_pipeline = RAGPipeline(groq_api_key)
    print("✅ Configuration valid")
    
    # Step 3: Explain PDF loading
    print("\n3. PDF Loading Process:")
    print("   - PDFLoader.load_pdfs(files) extracts text from all pages")
    print("   - Preserves page numbers for citation")
    print("   - Returns list of document dictionaries")
    
    # Step 4: Explain chunking
    print("\n4. Chunking Process:")
    print("   - DocumentChunker.chunk_documents(docs) splits text")
    print("   - Uses RecursiveCharacterTextSplitter")
    print("   - Chunk size: 1000 chars, Overlap: 200 chars")
    print("   - Maintains metadata (source, page number)")
    
    # Step 5: Explain embeddings
    print("\n5. Embedding Generation:")
    print("   - EmbeddingGenerator uses sentence-transformers")
    print("   - Model: all-MiniLM-L6-v2 (384 dimensions)")
    print("   - Converts text to semantic vectors")
    print(f"   - Embedding dimension: {embedding_generator.embedding_dim}")
    
    # Step 6: Explain vector store
    print("\n6. Vector Storage:")
    print("   - VectorStore uses FAISS for efficient similarity search")
    print("   - Builds index from embeddings")
    print("   - Enables fast k-NN retrieval")
    
    # Step 7: Explain RAG pipeline
    print("\n7. RAG Pipeline:")
    print("   - Retrieves top-k relevant chunks")
    print("   - Constructs prompt with context")
    print("   - Calls Groq LLM (llama-3.1-70b-versatile)")
    print("   - Returns answer with citations")
    
    # Step 8: Usage flow
    print("\n8. Complete Workflow:")
    print("   User uploads PDFs → Extract text → Chunk → Embed → Index")
    print("   User asks question → Generate query embedding → Search index")
    print("   Retrieve top chunks → Build prompt → Call LLM → Return answer")
    
    print("\n" + "=" * 80)
    print("Example Complete!")
    print("=" * 80)
    print("\nTo run the full application:")
    print("  python app.py")
    print("\nThen open browser to: http://localhost:7860")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_workflow()
