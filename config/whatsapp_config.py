from config.settings import settings

class WhatsAppConfig:
    """WhatsApp Business API configuration"""
    
    BASE_URL = "https://graph.facebook.com/v18.0"
    PHONE_NUMBER_ID = settings.WHATSAPP_PHONE_NUMBER_ID
    ACCESS_TOKEN = settings.WHATSAPP_ACCESS_TOKEN
    VERIFY_TOKEN = settings.WHATSAPP_VERIFY_TOKEN
    
    # Message templates
    WELCOME_MESSAGE = {
        "en": "Welcome to The Wellness London! 🌟 I'm your AI health concierge. How can I help you today?",
        "ar": "مرحباً بك في The Wellness London! 🌟 أنا مساعدك الصحي الذكي. كيف يمكنني مساعدتك اليوم؟"
    }
    
    MENU_OPTIONS = {
        "en": [
            "📅 Book an appointment",
            "🩺 Health assessment",
            "💉 Blood testing info",
            "🧬 PRP treatment info",
            "⚖️ Weight management",
            "📞 Speak to a human"
        ],
        "ar": [
            "📅 حجز موعد",
            "🩺 تقييم صحي",
            "💉 معلومات فحص الدم",
            "🧬 معلومات علاج PRP",
            "⚖️ إدارة الوزن",
            "📞 التحدث مع شخص"
        ]
    }
    
    # Webhook configuration
    WEBHOOK_VERIFY_TOKEN = settings.WHATSAPP_VERIFY_TOKEN
    
    @classmethod
    def get_headers(cls):
        """Get headers for WhatsApp API requests"""
        return {
            "Authorization": f"Bearer {cls.ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }