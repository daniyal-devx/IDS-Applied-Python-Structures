"""
Logger Module
Production-grade logging and monitoring
"""

import logging
import sys
from datetime import datetime


def setup_logger(name: str = "InsightForge", level: int = logging.INFO) -> logging.Logger:
    """
    Setup production logger with formatted output
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Console handler with custom format
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # Professional format
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger


class QueryLogger:
    """Log user queries for analytics and monitoring"""
    
    def __init__(self):
        self.queries = []
        self.logger = logging.getLogger("InsightForge.Analytics")
    
    def log_query(self, question: str, num_chunks_retrieved: int, response_generated: bool):
        """
        Log a user query with metadata
        
        Args:
            question: User question
            num_chunks_retrieved: Number of chunks retrieved
            response_generated: Whether response was successfully generated
        """
        query_log = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'question_length': len(question),
            'chunks_retrieved': num_chunks_retrieved,
            'success': response_generated
        }
        
        self.queries.append(query_log)
        self.logger.info(f"Query logged: {question[:50]}... [Success: {response_generated}]")
    
    def get_stats(self) -> dict:
        """Get query statistics"""
        if not self.queries:
            return {'total_queries': 0}
        
        success_count = sum(1 for q in self.queries if q['success'])
        avg_length = sum(q['question_length'] for q in self.queries) / len(self.queries)
        
        return {
            'total_queries': len(self.queries),
            'successful_queries': success_count,
            'failed_queries': len(self.queries) - success_count,
            'avg_question_length': round(avg_length, 1),
            'success_rate': round(success_count / len(self.queries) * 100, 1)
        }
