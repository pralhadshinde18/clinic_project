from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from bson import ObjectId
from domain.technician_domain import TechnicianDomain


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


class TechnicianModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
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

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_domain(cls, technician_domain: 'TechnicianDomain'):
        return cls(
            id=technician_domain.id,
            user_name=technician_domain.user_name,
            name=technician_domain.name,
            hospital_name=technician_domain.hospital_name,
            address=technician_domain.address,
            contact_number=technician_domain.contact_number,
            whatsapp_number=technician_domain.whatsapp_number,
            email_address=technician_domain.email_address,
            education=technician_domain.education,

            gender=technician_domain.gender,
            description=technician_domain.description,
            hospital_id=technician_domain.hospital_id
        )

    def to_domain(self) -> 'TechnicianDomain':
        return TechnicianDomain(
            id=str(self.id) if self.id else None,
            user_name=self.user_name,
            name=self.name,
            hospital_name=self.hospital_name,
            address=self.address,
            contact_number=self.contact_number,
            whatsapp_number=self.whatsapp_number,
            email_address=self.email_address,
            education=self.education,
            gender=self.gender,
            description=self.description,
            hospital_id=self.hospital_id
        )
