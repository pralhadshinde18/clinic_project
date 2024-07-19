from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId

from domain.hospital_domain import HospitalDomain


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

# This method validates if a value is a valid ObjectId.
    @classmethod
    def validate(cls, v, field=None, config=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# This method updates the JSON schema to represent the ObjectId as a string.
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class HospitalModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    hospital_name: str
    area: str
    description: str
    email_address: EmailStr
    rating: float
    contact_number: str
    whatsapp_number: str
    address: str
    category: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_domain(cls, hospital_domain: 'HospitalDomain'):
        return cls(
            id=hospital_domain.id,
            hospital_name=hospital_domain.hospital_name,
            area=hospital_domain.area,
            description=hospital_domain.description,
            email_address=hospital_domain.email_address,
            rating=hospital_domain.rating,
            contact_number=hospital_domain.contact_number,
            whatsapp_number=hospital_domain.whatsapp_number,
            address=hospital_domain.address,
            category=hospital_domain.category
        )

    def to_domain(self) -> 'HospitalDomain':
        return HospitalDomain(
            id=str(self.id) if self.id else None,
            hospital_name=self.hospital_name,
            area=self.area,
            description=self.description,
            email_address=self.email_address,
            rating=self.rating,
            contact_number=self.contact_number,
            whatsapp_number=self.whatsapp_number,
            address=self.address,
            category=self.category
        )
