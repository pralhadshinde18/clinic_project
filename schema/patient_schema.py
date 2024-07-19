from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


class PatientBase(BaseModel):
    name: str
    address: str
    contact_number: int
    whatsapp_number: int
    age: int
    gender: str
    reference_by: str
    test_conducted_by: str
    test_hospital: str
    referred_doctor: str
    referred_hospital: str
    clinical_category: str
    clinical_sub_category: str
    test: str
    format: str
    exam_procedure: str
    hospital_id: str


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[int] = None
    whatsapp_number: Optional[int] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    reference_by: Optional[str] = None
    test_conducted_by: Optional[str] = None
    test_hospital: Optional[str] = None
    referred_doctor: Optional[str] = None
    referred_hospital: Optional[str] = None
    clinical_category: Optional[str] = None
    clinical_sub_category: Optional[str] = None
    test: Optional[str] = None
    format: Optional[str] = None
    exam_procedure: Optional[str] = None
    hospital_id: Optional[str] = None


class PatientResponse(PatientBase):
    pass

