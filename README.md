# WellnessConnect - AI-Powered Health Concierge Platform

WellnessConnect is a WhatsApp-based AI health concierge that pre-qualifies leads, schedules appointments, and provides personalized wellness recommendations for The Wellness London.

## Features

- **AI Chatbot Integration**: WhatsApp Business integration with Claude AI assistant
- **Smart Lead Qualification**: Automatic categorization by treatment type and urgency
- **Personalized Content Delivery**: Targeted wellness content in English/Arabic
- **Automated Follow-up**: Post-treatment care reminders and wellness plan delivery
- **Dashboard Analytics**: Real-time insights into leads, appointments, and conversions

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure your settings
4. Run database setup: `python scripts/setup_database.py`
5. Start the application: `python main.py`

## Project Structure

- `/src/api/` - API endpoints for WhatsApp webhook and external integrations
- `/src/core/` - Core business logic (AI assistant, lead qualification, scheduling)
- `/src/models/` - Database models
- `/src/services/` - External service integrations
- `/src/utils/` - Utility functions and helpers
- `/content/` - Wellness content templates and assessment questions
- `/templates/` - Dashboard HTML templates

## Implementation Phases

- **Phase 1**: Basic appointment booking and FAQ bot
- **Phase 2**: AI health assessment and content personalization
- **Phase 3**: White-label licensing to other clinics

## License

Proprietary - The Wellness London