import os
import hashlib

BOT_TOKEN = "8664546839:AAE1G87GaLz59qZoHnWl1Qa1UJbTD7MhJ1E"

try:
    INSTANCE_ID = hashlib.sha256(BOT_TOKEN.encode()).hexdigest()
except (TypeError, AttributeError):
    INSTANCE_ID = "local_instance"

MONGO_URI = "mongodb+srv://pabitrabarman0002:rajrajkumar02@rajrajkumar.rrwa7zy.mongodb.net/?retryWrites=true&w=majority&appName=Rajrajkumar"

GROQ_API_KEYS = [
    "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",
    "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",
    "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",
    "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",
  ]

GROQ_MODEL = "llama-3.1-8b-instant"

LOG_CHAT_ID = -1003723055654
OWNER_ID = 7572263943

# 🤖 Bot Owner Configuration
BOT_OWNER_ID = 8705127026  # Advanced AI Bot Owner

# Advanced AI Configuration
ENABLE_ADVANCED_FEATURES = True
ENABLE_SENTIMENT_ANALYSIS = True
ENABLE_CONTEXT_MANAGEMENT = True
ENABLE_USER_LEARNING = True
ENABLE_MULTI_MODEL = True

# Security Configuration
ENABLE_THREAT_DETECTION = True
ENABLE_RATE_LIMITING = True
MAX_REQUESTS_PER_MINUTE = 30
ENABLE_INPUT_SANITIZATION = True

# Bot Owner Permissions
BOT_OWNER_PERMISSIONS = {
    "stats": True,
    "broadcast": True,
    "admin_commands": True,
    "user_management": True,
    "analytics": True,
    "security_logs": True,
    "advanced_features_control": True,
    "system_management": True
}

# Feature Flags
FEATURES = {
    "ai_chat": True,
    "anime_reactions": True,
    "games": True,
    "welcome_messages": True,
    "nsfw_filter": True,
    "chat_memory": True,
    "bot_stats": True,
    "broadcast": True,
    "advanced_analytics": True,
    "sentiment_analysis": True,
    "intent_detection": True,
    "user_preference_learning": True,
    "multi_turn_context": True,
    "reasoning_engine": True,
    "memory_system": True,
    "personality_adaptation": True,
    "threat_detection": True,
    "rate_limiting": True
}

def is_bot_owner(user_id: int) -> bool:
    """Check if user is bot owner"""
    return user_id == BOT_OWNER_ID

def get_bot_owner_id() -> int:
    """Get bot owner ID"""
    return BOT_OWNER_ID

def has_owner_permission(user_id: int, permission: str) -> bool:
    """Check if user has owner permission"""
    if not is_bot_owner(user_id):
        return False
    return BOT_OWNER_PERMISSIONS.get(permission, False)

NSFW_WORDS = [
    "chutiya", "madarchod", "bhosdi", "bhosdiwala", "chutka", "kaminey", "haraamikhor",
    "bhosdike", "bhosdika", "anal", "arse", "ass", "asshole", "bastard", "bitch", "blowjob",
    "bollocks", "boner", "boobs", "bugger", "bullshit", "cock", "cocksucker", "cunt", "dick",
    "dildo", "dyke", "fag", "faggot", "fuck", "fucked", "fucker", "fucking", "goddamn",
    "jackass", "jizz", "kunt", "motherfucker", "nigga", "nigger", "penis", "piss", "prick",
    "pussy", "queer", "rape", "shit", "slut", "twat", "whore", "wank", "wanker", "cum",
    "vagina", "scrotum", "semen", "porn", "pornography", "xxx", "masturbate", "masturbating",
    "fuddi", "fudi", "randwa", "randi", "gandu", "gand", "bhenchod", "lund", "loda",
    "chud", "chodna", "chudai", "gaand",
]
