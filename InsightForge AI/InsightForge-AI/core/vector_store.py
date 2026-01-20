"""
Vector Store Module
FAISS-based vector storage and similarity search
"""

import faiss
import numpy as np
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)


class VectorStore:
    """High-performance vector storage and retrieval using FAISS"""
    
    def __init__(self, embedding_dim: int):
        """
        Initialize FAISS index
        
        Args:
            embedding_dim: Dimension of embedding vectors
        """
        self.embedding_dim = embedding_dim
        # Use inner product index (equivalent to cosine similarity with normalized vectors)
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.chunks = []
        self.is_built = False
        
    def build_index(self, embeddings: np.ndarray, chunks: List[Dict[str, any]]):
        """
        Build FAISS index from embeddings
        
        Args:
            embeddings: NumPy array of embeddings (n_chunks, embedding_dim)
            chunks: List of chunk dictionaries with metadata
        """
        try:
            # Ensure embeddings are float32
            embeddings = embeddings.astype('float32')
            
            # Add vectors to index
            self.index.add(embeddings)
            self.chunks = chunks
            self.is_built = True
            
            logger.info(f"Built FAISS index with {len(chunks)} vectors")
            
        except Exception as e:
            logger.error(f"Error building FAISS index: {str(e)}")
            raise
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[Tuple[Dict[str, any], float]]:
        """
        Search for top-k most similar chunks
        
        Args:
            query_embedding: Query embedding vector
            k: Number of results to return
            
        Returns:
            List of (chunk_dict, similarity_score) tuples
        """
        if not self.is_built:
            raise ValueError("Index not built. Call build_index first.")
        
        try:
            # Ensure query is 2D and float32
            query_embedding = query_embedding.reshape(1, -1).astype('float32')
            
            # Search index
            similarities, indices = self.index.search(query_embedding, min(k, len(self.chunks)))
            
            # Package results with metadata
            results = []
            for idx, sim in zip(indices[0], similarities[0]):
                if idx < len(self.chunks):  # Safety check
                    results.append((self.chunks[idx], float(sim)))
            
            logger.info(f"Retrieved {len(results)} chunks for query")
            return results
            
        except Exception as e:
            logger.error(f"Error searching index: {str(e)}")
            raise
    
    def get_index_stats(self) -> Dict[str, any]:
        """Get statistics about the vector store"""
        return {
            'total_vectors': self.index.ntotal if self.is_built else 0,
            'embedding_dim': self.embedding_dim,
            'is_built': self.is_built
        }
