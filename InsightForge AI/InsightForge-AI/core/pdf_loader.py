"""
PDF Loader Module
Handles PDF document processing with page-level tracking
"""

import fitz  # PyMuPDF
from typing import List, Dict, Tuple
import logging

logger = logging.getLogger(__name__)


class PDFLoader:
    """Enterprise-grade PDF document loader with metadata preservation"""
    
    def __init__(self):
        self.documents = []
        
    def load_pdfs(self, pdf_files: List) -> List[Dict[str, any]]:
        """
        Load multiple PDF files and extract text with page numbers
        
        Args:
            pdf_files: List of file objects from Gradio
            
        Returns:
            List of document dictionaries with text, page numbers, and metadata
        """
        all_documents = []
        
        for pdf_file in pdf_files:
            try:
                # Open PDF with PyMuPDF
                doc = fitz.open(pdf_file.name)
                filename = pdf_file.name.split('/')[-1]
                
                logger.info(f"Processing {filename}: {len(doc)} pages")
                
                # Extract text from each page
                for page_num in range(len(doc)):
                    page = doc[page_num]
                    text = page.get_text()
                    
                    # Clean and normalize text
                    text = self._clean_text(text)
                    
                    if text.strip():  # Only add non-empty pages
                        all_documents.append({
                            'text': text,
                            'page': page_num + 1,
                            'source': filename,
                            'total_pages': len(doc)
                        })
                
                doc.close()
                logger.info(f"Successfully processed {filename}")
                
            except Exception as e:
                logger.error(f"Error processing {pdf_file.name}: {str(e)}")
                raise
        
        self.documents = all_documents
        return all_documents
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize extracted text"""
        # Remove excessive whitespace
        text = ' '.join(text.split())
        # Remove special characters that might break processing
        text = text.replace('\x00', '')
        return text
    
    def get_summary_stats(self) -> Dict[str, any]:
        """Get statistics about loaded documents"""
        if not self.documents:
            return {}
        
        sources = set(doc['source'] for doc in self.documents)
        total_pages = sum(doc['total_pages'] for doc in self.documents if 'total_pages' in doc)
        total_chars = sum(len(doc['text']) for doc in self.documents)
        
        return {
            'num_files': len(sources),
            'total_pages': len(self.documents),
            'total_characters': total_chars,
            'sources': list(sources)
        }
