"""
Chunking Module
Semantic text splitting optimized for RAG retrieval
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class DocumentChunker:
    """Intelligent document chunking with context preservation"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize chunker with optimal parameters for semantic coherence
        
        Args:
            chunk_size: Target size of each chunk in characters
            chunk_overlap: Overlap between chunks to preserve context
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
    def chunk_documents(self, documents: List[Dict[str, any]]) -> List[Dict[str, any]]:
        """
        Split documents into semantic chunks while preserving metadata
        
        Args:
            documents: List of document dictionaries with text and metadata
            
        Returns:
            List of chunk dictionaries with preserved metadata
        """
        all_chunks = []
        
        for doc in documents:
            try:
                # Split text into chunks
                text_chunks = self.text_splitter.split_text(doc['text'])
                
                # Create chunk objects with metadata
                for i, chunk_text in enumerate(text_chunks):
                    chunk = {
                        'text': chunk_text,
                        'page': doc['page'],
                        'source': doc['source'],
                        'chunk_id': f"{doc['source']}_p{doc['page']}_c{i}",
                        'total_pages': doc.get('total_pages', 0)
                    }
                    all_chunks.append(chunk)
                    
            except Exception as e:
                logger.error(f"Error chunking document from {doc.get('source', 'unknown')}: {str(e)}")
                continue
        
        logger.info(f"Created {len(all_chunks)} chunks from {len(documents)} document pages")
        return all_chunks
    
    def get_chunking_stats(self, chunks: List[Dict[str, any]]) -> Dict[str, any]:
        """Get statistics about chunking results"""
        if not chunks:
            return {}
        
        chunk_sizes = [len(chunk['text']) for chunk in chunks]
        
        return {
            'total_chunks': len(chunks),
            'avg_chunk_size': sum(chunk_sizes) / len(chunk_sizes),
            'min_chunk_size': min(chunk_sizes),
            'max_chunk_size': max(chunk_sizes)
        }
