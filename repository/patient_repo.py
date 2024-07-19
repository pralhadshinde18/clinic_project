from pymongo import MongoClient
from bson import ObjectId
from domain.patient_domain import PatientDomain
from model.patient_model import PatientModel
from typing import List


class PatientRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["hospital_db1"]
        self.collection = self.db["patients"]

    def create(self, patient: PatientDomain) -> PatientDomain:
        patient_model = PatientModel.from_domain(patient)
        result = self.collection.insert_one(patient_model.dict(by_alias=True, exclude={"id"}))
        patient_model.id = result.inserted_id
        return patient_model.to_domain()

    def list(self) -> list[PatientDomain]:
        patients = self.collection.find()
        return [PatientModel(**patient).to_domain() for patient in patients]

    def get(self, patient_id: str) -> PatientDomain:
        patient = self.collection.find_one({"_id": ObjectId(patient_id)})
        if patient:
            return PatientModel(**patient).to_domain()
        return None

    def find_by_hospital_id(self, hospital_id: str) -> List[PatientDomain]:
        patients = self.collection.find({"hospital_id": hospital_id})
        return [PatientModel(**patient).to_domain() for patient in patients]
