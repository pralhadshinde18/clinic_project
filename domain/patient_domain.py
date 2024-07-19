from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class PatientDomain:
    id: Optional[str]
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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'contact_number': self.contact_number,
            'whatsapp_number': self.whatsapp_number,
            'age': self.age,
            'gender': self.gender,
            'reference_by': self.reference_by,
            'test_conducted_by': self.test_conducted_by,
            'test_hospital': self.test_hospital,
            'referred_doctor': self.referred_doctor,
            'referred_hospital': self.referred_hospital,
            'clinical_category': self.clinical_category,
            'clinical_sub_category': self.clinical_sub_category,
            'test': self.test,
            'format': self.format,
            'exam_procedure': self.exam_procedure,
            'hospital_id': self.hospital_id
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            name=data['name'],
            address=data['address'],
            contact_number=data['contact_number'],
            whatsapp_number=data['whatsapp_number'],
            age=data['age'],
            gender=data['gender'],
            reference_by=data['reference_by'],
            test_conducted_by=data['test_conducted_by'],
            test_hospital=data['test_hospital'],
            referred_doctor=data['referred_doctor'],
            referred_hospital=data['referred_hospital'],
            clinical_category=data['clinical_category'],
            clinical_sub_category=data['clinical_sub_category'],
            test=data['test'],
            format=data['format'],
            exam_procedure=data['exam_procedure'],
            hospital_id=data['hospital_id']
        )
