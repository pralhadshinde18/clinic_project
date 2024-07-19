from dataclasses import dataclass
from typing import Optional


@dataclass
class ReportingDoctorDomain:
    id: Optional[str]
    user_name: str
    name: str
    address: str
    hospital_name: str
    contact_number: int
    whatsapp_number: int
    email_address: str
    education: str
    category: str
    speciality: str
    gender: str
    description: str
    hospital_id: str

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'name': self.name,
            'address': self.address,
            'hospital_name': self.hospital_name,
            'contact_number': self.contact_number,
            'whatsapp_number': self.whatsapp_number,
            'email_address': self.email_address,
            'education': self.education,
            'category': self.category,
            'speciality': self.speciality,
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
            address=data['address'],
            hospital_name=data['hospital_name'],
            contact_number=data['contact_number'],
            whatsapp_number=data['whatsapp_number'],
            email_address=data['email_address'],
            education=data['education'],
            category=data['category'],
            speciality=data['speciality'],
            gender=data['gender'],
            description=data['description'],
            hospital_id=data['hospital_id']
        )
