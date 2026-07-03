"""
Advanced AI Features for NYRA Bot
- Semantic understanding and intent detection
- Conversation analytics and insights
- User preference learning
- Multi-turn context awareness
- Sentiment analysis
"""

from datetime import datetime
from typing import Dict, List, Optional
import json

class ConversationAnalytics:
    """Analyze user conversations for insights"""
    
    def __init__(self):
        self.user_stats = {}
        self.conversation_history = {}
    
    def track_conversation(self, user_id: int, message: str, response: str, language: str):
        """Track conversation metrics"""
        if user_id not in self.user_stats:
            self.user_stats[user_id] = {
                "messages": 0,
                "languages": set(),
                "first_seen": datetime.now(),
                "last_seen": datetime.now(),
                "average_response_time": 0,
                "sentiment_trend": [],
                "topics_discussed": []
            }
        
        stats = self.user_stats[user_id]
        stats["messages"] += 1
        stats["languages"].add(language)
        stats["last_seen"] = datetime.now()
        
        if user_id not in self.conversation_history:
            self.conversation_history[user_id] = []
        
        self.conversation_history[user_id].append({
            "timestamp": datetime.now(),
            "message": message,
            "response": response,
            "language": language
        })
    
    def get_user_analytics(self, user_id: int) -> Dict:
        """Get analytics for a specific user"""
        if user_id not in self.user_stats:
            return None
        
        stats = self.user_stats[user_id]
        return {
            "total_messages": stats["messages"],
            "languages_used": list(stats["languages"]),
            "first_seen": stats["first_seen"].isoformat(),
            "last_seen": stats["last_seen"].isoformat(),
            "engagement_days": (datetime.now() - stats["first_seen"]).days
        }


class SemanticIntentDetector:
    """Detect user intent from messages"""
    
    INTENTS = {
        "greeting": ["hello", "hi", "hey", "good morning", "namaste", "konnichiwa"],
        "farewell": ["bye", "goodbye", "see you", "farewell", "cya"],
        "help": ["help", "assist", "guide", "how to", "what's", "explain"],
        "play_game": ["game", "play", "dice", "dart", "basket", "football"],
        "emotion": ["sad", "happy", "angry", "love", "cute", "beautiful"],
        "technical": ["code", "python", "api", "database", "error", "bug"],
        "social": ["friend", "dating", "love", "relationship", "family"]
    }
    
    @staticmethod
    def detect_intent(message: str) -> List[str]:
        """Detect intents from user message"""
        message_lower = message.lower()
        detected_intents = []
        
        for intent, keywords in SemanticIntentDetector.INTENTS.items():
            if any(keyword in message_lower for keyword in keywords):
                detected_intents.append(intent)
        
        return detected_intents if detected_intents else ["general"]


class UserPreferencelearner:
    """Learn and adapt to user preferences"""
    
    def __init__(self):
        self.user_preferences = {}
    
    def update_preference(self, user_id: int, preference_type: str, value):
        """Update user preference"""
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}
        
        self.user_preferences[user_id][preference_type] = value
    
    def get_preference(self, user_id: int, preference_type: str, default=None):
        """Get user preference"""
        if user_id in self.user_preferences:
            return self.user_preferences[user_id].get(preference_type, default)
        return default
    
    def adapt_response_style(self, user_id: int) -> str:
        """Adapt response style based on user preferences"""
        pref_style = self.get_preference(user_id, "response_style", "friendly")
        
        styles = {
            "formal": "professional and respectful tone",
            "casual": "relaxed and friendly tone",
            "funny": "humorous and witty tone",
            "friendly": "warm and sweet tone"
        }
        
        return styles.get(pref_style, styles["friendly"])


class ContextManager:
    """Manage multi-turn conversation context"""
    
    def __init__(self, max_context_turns: int = 10):
        self.context_storage = {}
        self.max_context_turns = max_context_turns
    
    def add_context(self, user_id: int, role: str, content: str):
        """Add context to conversation"""
        if user_id not in self.context_storage:
            self.context_storage[user_id] = []
        
        self.context_storage[user_id].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        })
        
        # Keep only recent context
        if len(self.context_storage[user_id]) > self.max_context_turns:
            self.context_storage[user_id] = self.context_storage[user_id][-self.max_context_turns:]
    
    def get_context(self, user_id: int) -> List[Dict]:
        """Get conversation context for a user"""
        return self.context_storage.get(user_id, [])
    
    def clear_context(self, user_id: int):
        """Clear conversation context"""
        if user_id in self.context_storage:
            del self.context_storage[user_id]


class SentimentAnalyzer:
    """Analyze sentiment of messages"""
    
    POSITIVE_WORDS = ["love", "amazing", "wonderful", "great", "excellent", "beautiful", "lovely", "happy", "joy"]
    NEGATIVE_WORDS = ["hate", "terrible", "awful", "bad", "angry", "sad", "disappointed", "frustrated"]
    
    @staticmethod
    def analyze(message: str) -> str:
        """Analyze sentiment: positive, negative, or neutral"""
        message_lower = message.lower()
        
        positive_count = sum(1 for word in SentimentAnalyzer.POSITIVE_WORDS if word in message_lower)
        negative_count = sum(1 for word in SentimentAnalyzer.NEGATIVE_WORDS if word in message_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"


class AdvancedAIBot:
    """Main advanced AI bot with all features integrated"""
    
    def __init__(self):
        self.analytics = ConversationAnalytics()
        self.intent_detector = SemanticIntentDetector()
        self.preference_learner = UserPreferencelearner()
        self.context_manager = ContextManager()
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def process_message(self, user_id: int, message: str, language: str) -> Dict:
        """Process message with advanced AI features"""
        
        # Detect intent
        intents = self.intent_detector.detect_intent(message)
        
        # Analyze sentiment
        sentiment = self.sentiment_analyzer.analyze(message)
        
        # Add to context
        self.context_manager.add_context(user_id, "user", message)
        
        # Get user preferences for response style
        response_style = self.preference_learner.adapt_response_style(user_id)
        
        return {
            "intents": intents,
            "sentiment": sentiment,
            "response_style": response_style,
            "context": self.context_manager.get_context(user_id)
        }
