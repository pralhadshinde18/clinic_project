from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from datetime import date

from domain.patient_domain import PatientDomain


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


class PatientModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
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

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @classmethod
    def from_domain(cls, patient_domain: 'PatientDomain'):
        return cls(
            id=patient_domain.id,
            name=patient_domain.name,
            address=patient_domain.address,
            contact_number=patient_domain.contact_number,
            whatsapp_number=patient_domain.whatsapp_number,
            age=patient_domain.age,
            gender=patient_domain.gender,
            reference_by=patient_domain.reference_by,
            test_conducted_by=patient_domain.test_conducted_by,
            test_hospital=patient_domain.test_hospital,
            referred_doctor=patient_domain.referred_doctor,
            referred_hospital=patient_domain.referred_hospital,
            clinical_category=patient_domain.clinical_category,
            clinical_sub_category=patient_domain.clinical_sub_category,
            test=patient_domain.test,
            format=patient_domain.format,
            exam_procedure=patient_domain.exam_procedure,
            hospital_id=patient_domain.hospital_id
        )

    def to_domain(self) -> 'PatientDomain':
        return PatientDomain(
            id=str(self.id) if self.id else None,
            name=self.name,
            address=self.address,
            contact_number=self.contact_number,
            whatsapp_number=self.whatsapp_number,
            age=self.age,
            gender=self.gender,
            reference_by=self.reference_by,
            test_conducted_by=self.test_conducted_by,
            test_hospital=self.test_hospital,
            referred_doctor=self.referred_doctor,
            referred_hospital=self.referred_hospital,
            clinical_category=self.clinical_category,
            clinical_sub_category=self.clinical_sub_category,
            test=self.test,
            format=self.format,
            exam_procedure=self.exam_procedure,
            hospital_id=self.hospital_id
        )
