from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class TechnicianBase(BaseModel):
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: int
    whatsapp_number: int
    email_address: EmailStr
    education: str
    gender: str
    description: str
    hospital_id: str


class TechnicianCreate(TechnicianBase):
    pass


class TechnicianResponse(TechnicianBase):
    pass
