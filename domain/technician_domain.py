from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class TechnicianDomain:
    id: Optional[str]
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: int
    whatsapp_number: int
    email_address: str
    education: str
    gender: str
    description: str
    hospital_id: str

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'name': self.name,
            'hospital_name': self.hospital_name,
            'address': self.address,
            'contact_number': self.contact_number,
            'whatsapp_number': self.whatsapp_number,
            'email_address': self.email_address,
            'education': self.education,
            'gender': self.gender,
            'description': self.description,
            'hospital_id': self.hospital_id
        }

    # Creates a domain model from a dictionary
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            user_name=data['user_name'],
            name=data['name'],
            hospital_name=data['hospital_name'],
            address=data['address'],
            contact_number=data['contact_number'],
            whatsapp_number=data['whatsapp_number'],
            email_address=data['email_address'],
            education=data['education'],
            gender=data['gender'],
            description=data['description'],
            hospital_id=data['hospital_id']
        )
