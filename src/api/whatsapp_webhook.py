from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import PlainTextResponse
from config.whatsapp_config import WhatsAppConfig
from src.services.whatsapp_service import WhatsAppService
from src.core.ai_assistant import AIAssistant
import json
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/whatsapp")
async def verify_webhook(request: Request):
    """Verify WhatsApp webhook"""
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    
    if mode == "subscribe" and token == WhatsAppConfig.WEBHOOK_VERIFY_TOKEN:
        logger.info("WhatsApp webhook verified successfully")
        return PlainTextResponse(challenge)
    else:
        logger.warning("WhatsApp webhook verification failed")
        raise HTTPException(status_code=403, detail="Verification failed")

@router.post("/whatsapp")
async def handle_webhook(request: Request):
    """Handle incoming WhatsApp messages"""
    try:
        body = await request.json()
        logger.info(f"Received webhook: {json.dumps(body, indent=2)}")
        
        # Process webhook data
        if "entry" in body:
            for entry in body["entry"]:
                if "changes" in entry:
                    for change in entry["changes"]:
                        if change.get("field") == "messages":
                            await process_message(change["value"])
        
        return {"status": "success"}
    
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

async def process_message(message_data):
    """Process incoming WhatsApp message"""
    try:
        if "messages" not in message_data:
            return
        
        for message in message_data["messages"]:
            sender_phone = message["from"]
            message_text = message.get("text", {}).get("body", "")
            message_type = message.get("type", "text")
            
            logger.info(f"Processing message from {sender_phone}: {message_text}")
            
            # Initialize services
            whatsapp_service = WhatsAppService()
            ai_assistant = AIAssistant()
            
            # Process message through AI assistant
            response = await ai_assistant.process_message(
                sender_phone, message_text, message_type
            )
            
            # Send response back to user
            if response:
                await whatsapp_service.send_message(sender_phone, response)
    
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")