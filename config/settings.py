import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://localhost:5432/wellnessconnect"
    
    # WhatsApp
    WHATSAPP_PHONE_NUMBER_ID: str = ""
    WHATSAPP_ACCESS_TOKEN: str = ""
    WHATSAPP_VERIFY_TOKEN: str = ""
    WHATSAPP_WEBHOOK_URL: str = ""
    
    # Claude AI
    CLAUDE_API_KEY: str = ""
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Application
    SECRET_KEY: str = "your-secret-key-change-in-production"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Clinic Information
    CLINIC_NAME: str = "The Wellness London"
    CLINIC_PHONE: str = "+44123456789"
    CLINIC_EMAIL: str = "info@thewellnesslondon.com"
    CLINIC_ADDRESS: str = "123 Wellness Street, London, UK"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()