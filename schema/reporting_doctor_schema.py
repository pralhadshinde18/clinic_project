from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ReportingDoctorBase(BaseModel):
    user_name: str
    name: str
    address: str
    hospital_name: str
    contact_number: int
    whatsapp_number: int
    email_address: EmailStr
    education: str
    category: str
    speciality: str
    gender: str
    description: str
    hospital_id: str


class ReportingDoctorCreate(ReportingDoctorBase):
    pass


class ReportingDoctorUpdate(BaseModel):
    user_name: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    hospital_name: Optional[str] = None
    contact_number: Optional[int] = None
    whatsapp_number: Optional[int] = None
    email_address: Optional[EmailStr] = None
    education: Optional[str] = None
    category: Optional[str] = None
    speciality: Optional[str] = None
    gender: Optional[str] = None
    description: Optional[str] = None
    hospital_id: Optional[str] = None


class ReportingDoctorResponse(ReportingDoctorBase):
    pass

