from pymongo import MongoClient
from bson import ObjectId
from typing import List
from domain.reporting_doctor_domain import ReportingDoctorDomain
from model.reporting_doctor_model import ReportingDoctorModel


class ReportingDoctorRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["hospital_db1"]
        self.collection = self.db["reporting_doctors"]

    def create(self, reporting_doctor: ReportingDoctorDomain) -> ReportingDoctorDomain:
        reporting_doctor_model = ReportingDoctorModel.from_domain(reporting_doctor)
        result = self.collection.insert_one(reporting_doctor_model.dict(by_alias=True, exclude={"id"}))
        reporting_doctor_model.id = result.inserted_id
        return reporting_doctor_model.to_domain()

    def list(self) -> List[ReportingDoctorDomain]:
        reporting_doctors = self.collection.find()
        return [ReportingDoctorModel(**reporting_doctor).to_domain() for reporting_doctor in reporting_doctors]

    def get(self, reporting_doctor_id: str) -> ReportingDoctorDomain:
        reporting_doctor = self.collection.find_one({"_id": ObjectId(reporting_doctor_id)})
        if reporting_doctor:
            return ReportingDoctorModel(**reporting_doctor).to_domain()
        return None

    def find_by_hospital_id(self, hospital_id: str) -> List[ReportingDoctorDomain]:
        reporting_doctors = self.collection.find({"hospital_id": hospital_id})
        return [ReportingDoctorModel(**reporting_doctor).to_domain() for reporting_doctor in reporting_doctors]
