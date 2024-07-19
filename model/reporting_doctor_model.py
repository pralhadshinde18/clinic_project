from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId

from domain.reporting_doctor_domain import ReportingDoctorDomain


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None, config=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class ReportingDoctorModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
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

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_domain(cls, reporting_doctor_domain: 'ReportingDoctorDomain'):
        return cls(
            id=reporting_doctor_domain.id,
            user_name=reporting_doctor_domain.user_name,
            name=reporting_doctor_domain.name,
            address=reporting_doctor_domain.address,
            hospital_name=reporting_doctor_domain.hospital_name,
            contact_number=reporting_doctor_domain.contact_number,
            whatsapp_number=reporting_doctor_domain.whatsapp_number,
            email_address=reporting_doctor_domain.email_address,
            education=reporting_doctor_domain.education,
            category=reporting_doctor_domain.category,
            speciality=reporting_doctor_domain.speciality,
            gender=reporting_doctor_domain.gender,
            description=reporting_doctor_domain.description,
            hospital_id=reporting_doctor_domain.hospital_id
        )

    def to_domain(self) -> 'ReportingDoctorDomain':
        return ReportingDoctorDomain(
            id=str(self.id) if self.id else None,
            user_name=self.user_name,
            name=self.name,
            address=self.address,
            hospital_name=self.hospital_name,
            contact_number=self.contact_number,
            whatsapp_number=self.whatsapp_number,
            email_address=self.email_address,
            education=self.education,
            category=self.category,
            speciality=self.speciality,
            gender=self.gender,
            description=self.description,
            hospital_id=self.hospital_id
        )
