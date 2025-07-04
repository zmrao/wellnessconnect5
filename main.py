import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.settings import settings
from config.database import init_db
from src.api.whatsapp_webhook import router as whatsapp_router
from src.api.appointment_api import router as appointment_router
from src.api.health_assessment_api import router as health_router

# Initialize FastAPI app
app = FastAPI(
    title="WellnessConnect",
    description="AI-Powered Health Concierge Platform",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(whatsapp_router, prefix="/webhook", tags=["WhatsApp"])
app.include_router(appointment_router, prefix="/api/appointments", tags=["Appointments"])
app.include_router(health_router, prefix="/api/health", tags=["Health Assessment"])

@app.on_event("startup")
async def startup_event():
    """Initialize database and services on startup"""
    await init_db()
    print("WellnessConnect started successfully!")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "WellnessConnect API is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "WellnessConnect",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )