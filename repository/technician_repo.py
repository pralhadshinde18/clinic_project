from pymongo import MongoClient
from bson import ObjectId
from typing import List
from domain.technician_domain import TechnicianDomain
from model.technician_model import TechnicianModel


class TechnicianRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["hospital_db1"]
        self.collection = self.db["technicians"]

    def create(self, technician: TechnicianDomain) -> TechnicianDomain:
        technician_model = TechnicianModel.from_domain(technician)
        result = self.collection.insert_one(technician_model.dict(by_alias=True, exclude={"id"}))
        technician_model.id = result.inserted_id
        return technician_model.to_domain()

    def list(self) -> List[TechnicianDomain]:
        technicians = self.collection.find()
        return [TechnicianModel(**technician).to_domain() for technician in technicians]

    def get(self, technician_id: str) -> TechnicianDomain:
        technician = self.collection.find_one({"_id": ObjectId(technician_id)})
        if technician:
            return TechnicianModel(**technician).to_domain()
        return None

    def find_by_hospital_id(self, hospital_id: str) -> List[TechnicianDomain]:
        technicians = self.collection.find({"hospital_id": hospital_id})
        return [TechnicianModel(**technician).to_domain() for technician in technicians]
