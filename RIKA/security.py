"""
Advanced Security Features
- Input validation and sanitization
- Threat detection
- Rate limiting
- User authentication
- Encryption
"""

import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum


class ThreatLevel(Enum):
    """Threat severity levels"""
    SAFE = "safe"
    WARNING = "warning"
    CRITICAL = "critical"


class ThreatDetector:
    """Detect and prevent threats"""
    
    MALICIOUS_PATTERNS = [
        r"(\b(drop|delete|insert|update|exec|select)\b.*\b(from|into|database|table)\b)",  # SQL injection
        r"(<script|javascript:|onerror=|onload=)",  # XSS attempts
        r"(../|..\\|etc/|var/www)",  # Path traversal
        r"(\$\{|eval|exec|system|passthru)",  # Code injection
    ]
    
    @staticmethod
    def check_threat(message: str) -> Dict:
        """Check message for threats"""
        import re
        
        threat_analysis = {
            "is_safe": True,
            "threat_level": ThreatLevel.SAFE.value,
            "detected_patterns": [],
            "timestamp": datetime.now()
        }
        
        message_lower = message.lower()
        
        for pattern in ThreatDetector.MALICIOUS_PATTERNS:
            if re.search(pattern, message_lower, re.IGNORECASE):
                threat_analysis["is_safe"] = False
                threat_analysis["threat_level"] = ThreatLevel.CRITICAL.value
                threat_analysis["detected_patterns"].append(pattern)
        
        return threat_analysis


class RateLimiter:
    """Rate limit user requests"""
    
    def __init__(self, max_requests: int = 30, time_window: int = 60):
        self.max_requests = max_requests
        self.time_window = time_window  # seconds
        self.user_requests = {}
    
    def is_rate_limited(self, user_id: int) -> bool:
        """Check if user is rate limited"""
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
        
        now = datetime.now()
        # Clean old requests
        self.user_requests[user_id] = [
            req_time for req_time in self.user_requests[user_id]
            if now - req_time < timedelta(seconds=self.time_window)
        ]
        
        if len(self.user_requests[user_id]) >= self.max_requests:
            return True
        
        self.user_requests[user_id].append(now)
        return False
    
    def get_remaining_requests(self, user_id: int) -> int:
        """Get remaining requests for user"""
        if user_id not in self.user_requests:
            return self.max_requests
        
        return max(0, self.max_requests - len(self.user_requests[user_id]))


class InputSanitizer:
    """Sanitize user input"""
    
    DANGEROUS_CHARS = ['<', '>', '"', "'", '&', ';', '`']
    
    @staticmethod
    def sanitize(user_input: str) -> str:
        """Remove dangerous characters"""
        sanitized = user_input
        for char in InputSanitizer.DANGEROUS_CHARS:
            sanitized = sanitized.replace(char, "")
        return sanitized.strip()
    
    @staticmethod
    def validate_length(text: str, max_length: int = 2000) -> bool:
        """Validate text length"""
        return len(text) <= max_length
    
    @staticmethod
    def validate_language(text: str) -> bool:
        """Validate text language compatibility"""
        # Check for valid Unicode ranges
        try:
            text.encode('utf-8')
            return True
        except (UnicodeEncodeError, UnicodeDecodeError):
            return False


class UserAuthentication:
    """User authentication system"""
    
    def __init__(self):
        self.authenticated_users = {}
        self.user_sessions = {}
    
    def authenticate_user(self, user_id: int, token: str) -> bool:
        """Authenticate user with token"""
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        
        if user_id not in self.authenticated_users:
            self.authenticated_users[user_id] = {
                "token": token_hash,
                "authenticated_at": datetime.now()
            }
            return True
        
        return self.authenticated_users[user_id]["token"] == token_hash
    
    def create_session(self, user_id: int) -> str:
        """Create user session"""
        session_token = hashlib.sha256(
            f"{user_id}{datetime.now().timestamp()}".encode()
        ).hexdigest()
        
        self.user_sessions[user_id] = {
            "session_token": session_token,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(hours=24)
        }
        
        return session_token
    
    def validate_session(self, user_id: int, session_token: str) -> bool:
        """Validate user session"""
        if user_id not in self.user_sessions:
            return False
        
        session = self.user_sessions[user_id]
        if datetime.now() > session["expires_at"]:
            del self.user_sessions[user_id]
            return False
        
        return session["session_token"] == session_token


class EncryptionManager:
    """Manage data encryption"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password securely"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, hash_value: str) -> bool:
        """Verify password against hash"""
        return EncryptionManager.hash_password(password) == hash_value


class AdvancedSecuritySystem:
    """Complete security system"""
    
    def __init__(self):
        self.threat_detector = ThreatDetector()
        self.rate_limiter = RateLimiter()
        self.input_sanitizer = InputSanitizer()
        self.authentication = UserAuthentication()
        self.encryption = EncryptionManager()
    
    def validate_request(self, user_id: int, message: str) -> Dict:
        """Comprehensive request validation"""
        
        validation_result = {
            "is_valid": True,
            "checks": {
                "rate_limit": not self.rate_limiter.is_rate_limited(user_id),
                "threat_check": self.threat_detector.check_threat(message)["is_safe"],
                "input_length": self.input_sanitizer.validate_length(message),
                "language_valid": self.input_sanitizer.validate_language(message)
            }
        }
        
        validation_result["is_valid"] = all(validation_result["checks"].values())
        
        return validation_result
