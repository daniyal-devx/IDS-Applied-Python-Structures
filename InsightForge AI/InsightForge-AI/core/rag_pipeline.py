"""
RAG Pipeline Module
End-to-end retrieval-augmented generation orchestration
"""

from groq import Groq
from typing import List, Dict, Tuple
import logging
import os

logger = logging.getLogger(__name__)


class RAGPipeline:
    """Enterprise RAG pipeline with Groq LLM integration"""
    
    def __init__(self, groq_api_key: str, model: str = "llama-3.1-70b-versatile"):
        """
        Initialize RAG pipeline
        
        Args:
            groq_api_key: Groq API key
            model: Groq model identifier
        """
        self.client = Groq(api_key=groq_api_key)
        self.model = model
        logger.info(f"Initialized RAG pipeline with model: {model}")
    
    def generate_answer(
        self,
        question: str,
        retrieved_chunks: List[Tuple[Dict[str, any], float]],
        mode: str = "executive",
        conversation_history: List[Dict[str, str]] = None
    ) -> Tuple[str, List[Dict[str, any]]]:
        """
        Generate answer using retrieved context and LLM
        
        Args:
            question: User question
            retrieved_chunks: List of (chunk, score) tuples from retrieval
            mode: Answer mode ("executive" or "technical")
            conversation_history: Previous conversation turns
            
        Returns:
            Tuple of (answer_text, source_citations)
        """
        try:
            # Prepare context from retrieved chunks
            context_parts = []
            sources = []
            
            for i, (chunk, score) in enumerate(retrieved_chunks, 1):
                context_parts.append(
                    f"[Context {i} - {chunk['source']}, Page {chunk['page']}]\n{chunk['text']}\n"
                )
                sources.append({
                    'source': chunk['source'],
                    'page': chunk['page'],
                    'relevance': round(score, 3),
                    'text_preview': chunk['text'][:200] + "..."
                })
            
            context = "\n".join(context_parts)
            
            # Build prompt based on mode
            system_prompt = self._build_system_prompt(mode)
            user_prompt = self._build_user_prompt(question, context, mode)
            
            # Prepare messages with conversation history
            messages = [{"role": "system", "content": system_prompt}]
            
            if conversation_history:
                messages.extend(conversation_history)
            
            messages.append({"role": "user", "content": user_prompt})
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=2048,
                top_p=0.9
            )
            
            answer = response.choices[0].message.content
            
            logger.info(f"Generated answer for question: {question[:50]}...")
            return answer, sources
            
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise
    
    def generate_summary(
        self,
        chunks: List[Dict[str, any]],
        mode: str = "executive"
    ) -> str:
        """
        Generate document summary
        
        Args:
            chunks: Document chunks to summarize
            mode: Summary mode
            
        Returns:
            Summary text
        """
        try:
            # Sample chunks for summary (use representative chunks)
            sample_size = min(10, len(chunks))
            sampled_chunks = chunks[::max(1, len(chunks) // sample_size)][:sample_size]
            
            # Prepare content
            content = "\n\n".join([
                f"[{chunk['source']}, Page {chunk['page']}]\n{chunk['text']}"
                for chunk in sampled_chunks
            ])
            
            # Build summary prompt
            if mode == "executive":
                prompt = f"""Analyze the following document excerpts and provide an executive summary.

Focus on:
- Key insights and findings
- Main themes and topics
- Strategic implications
- Critical takeaways

Documents:
{content}

Provide a concise, high-level executive summary (3-5 paragraphs):"""
            else:
                prompt = f"""Analyze the following document excerpts and provide a technical summary.

Focus on:
- Methodologies and approaches
- Technical details and specifications
- Data and findings
- Implementation considerations

Documents:
{content}

Provide a detailed technical summary:"""
            
            # Generate summary
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert document analyst and summarizer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=1500
            )
            
            summary = response.choices[0].message.content
            
            logger.info(f"Generated {mode} summary")
            return summary
            
        except Exception as e:
            logger.error(f"Error generating summary: {str(e)}")
            raise
    
    def _build_system_prompt(self, mode: str) -> str:
        """Build system prompt based on mode"""
        if mode == "executive":
            return """You are InsightForge AI, an elite business intelligence assistant.

Your role:
- Provide clear, actionable insights for decision-makers
- Focus on strategic implications and key takeaways
- Use business language, avoid unnecessary jargon
- Be concise and impactful

Guidelines:
- Always cite sources with [Source: filename, Page X] format
- Synthesize information across documents when relevant
- Highlight contradictions or uncertainties
- Provide confidence levels when appropriate"""
        else:
            return """You are InsightForge AI, an expert technical analyst.

Your role:
- Provide detailed, technically accurate information
- Include relevant methodologies and data
- Explain technical concepts thoroughly
- Reference specific sections and details

Guidelines:
- Always cite sources with [Source: filename, Page X] format
- Include relevant technical details and specifications
- Note limitations or gaps in the data
- Cross-reference related information"""
    
    def _build_user_prompt(self, question: str, context: str, mode: str) -> str:
        """Build user prompt with context"""
        return f"""Question: {question}

Context from documents:
{context}

Instructions:
- Answer the question based ONLY on the provided context
- Cite specific sources using [Source: filename, Page X] format
- If the context doesn't contain relevant information, state this clearly
- {'Focus on strategic insights and business implications' if mode == 'executive' else 'Provide comprehensive technical details'}
- Be precise and evidence-based

Answer:"""
