from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class HospitalBase(BaseModel):
    hospital_name: str
    area: str
    description: str
    email_address: EmailStr
    rating: float
    contact_number: str
    whatsapp_number: str
    address: str
    category: str


class HospitalCreate(HospitalBase):
    pass


class HospitalUpdate(BaseModel):
    hospital_name: Optional[str] = None
    area: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[EmailStr] = None
    rating: Optional[float] = None
    contact_number: Optional[str] = None
    whatsapp_number: Optional[str] = None
    address: Optional[str] = None
    category: Optional[str] = None


class HospitalResponse(HospitalBase):
    pass

