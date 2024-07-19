from dataclasses import dataclass
from typing import Optional


@dataclass
class HospitalDomain:
    id: Optional[str]
    hospital_name: str
    area: str
    description: str
    email_address: str
    rating: float
    contact_number: str
    whatsapp_number: str
    address: str
    category: str

    def to_dict(self):
        return {
            'id': self.id,
            'hospital_name': self.hospital_name,
            'area': self.area,
            'description': self.description,
            'email_address': self.email_address,
            'rating': self.rating,
            'contact_number': self.contact_number,
            'whatsapp_number': self.whatsapp_number,
            'address': self.address,
            'category': self.category
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            hospital_name=data['hospital_name'],
            area=data['area'],
            description=data['description'],
            email_address=data['email_address'],
            rating=data['rating'],
            contact_number=data['contact_number'],
            whatsapp_number=data['whatsapp_number'],
            address=data['address'],
            category=data['category']
        )
