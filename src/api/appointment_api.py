from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from src.models.appointment import Appointment
from src.core.appointment_scheduler import AppointmentScheduler
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

router = APIRouter()

class AppointmentCreate(BaseModel):
    user_phone: str
    treatment_type: str
    preferred_date: datetime
    preferred_time: str
    notes: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: int
    user_phone: str
    treatment_type: str
    appointment_date: datetime
    status: str
    notes: Optional[str]
    
    class Config:
        from_attributes = True

@router.post("/", response_model=AppointmentResponse)
async def create