"""
Memory Module
Conversation history and context management
"""

from typing import List, Dict
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ConversationMemory:
    """Manage conversation history and context"""
    
    def __init__(self, max_history: int = 10):
        """
        Initialize conversation memory
        
        Args:
            max_history: Maximum number of conversation turns to retain
        """
        self.max_history = max_history
        self.history = []
        self.session_start = datetime.now()
        
    def add_turn(self, question: str, answer: str, sources: List[Dict[str, any]] = None):
        """
        Add a conversation turn to history
        
        Args:
            question: User question
            answer: AI answer
            sources: Source citations
        """
        turn = {
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'answer': answer,
            'sources': sources or []
        }
        
        self.history.append(turn)
        
        # Trim history if needed
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
        
        logger.info(f"Added conversation turn. Total turns: {len(self.history)}")
    
    def get_context_for_llm(self, num_turns: int = 3) -> List[Dict[str, str]]:
        """
        Get recent conversation history formatted for LLM
        
        Args:
            num_turns: Number of recent turns to include
            
        Returns:
            List of message dictionaries for LLM
        """
        recent_history = self.history[-num_turns:] if num_turns > 0 else []
        
        messages = []
        for turn in recent_history:
            messages.append({"role": "user", "content": turn['question']})
            messages.append({"role": "assistant", "content": turn['answer']})
        
        return messages
    
    def get_full_history(self) -> List[Dict[str, any]]:
        """Get complete conversation history"""
        return self.history.copy()
    
    def export_to_text(self) -> str:
        """
        Export conversation history to formatted text
        
        Returns:
            Formatted text representation of conversation
        """
        lines = [
            "=" * 80,
            "InsightForge AI - Conversation History",
            f"Session Start: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 80,
            ""
        ]
        
        for i, turn in enumerate(self.history, 1):
            lines.extend([
                f"\n{'─' * 80}",
                f"Turn {i} - {turn['timestamp']}",
                f"{'─' * 80}",
                "",
                f"USER:",
                turn['question'],
                "",
                f"ASSISTANT:",
                turn['answer'],
                ""
            ])
            
            if turn.get('sources'):
                lines.append("SOURCES:")
                for source in turn['sources']:
                    lines.append(f"  • {source['source']}, Page {source['page']} (Relevance: {source['relevance']})")
                lines.append("")
        
        return "\n".join(lines)
    
    def export_to_json(self) -> str:
        """
        Export conversation history to JSON
        
        Returns:
            JSON string of conversation history
        """
        export_data = {
            'session_start': self.session_start.isoformat(),
            'total_turns': len(self.history),
            'conversation': self.history
        }
        
        return json.dumps(export_data, indent=2)
    
    def clear(self):
        """Clear conversation history"""
        self.history = []
        self.session_start = datetime.now()
        logger.info("Cleared conversation history")
