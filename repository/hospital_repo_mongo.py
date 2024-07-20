from pymongo import MongoClient
from bson import ObjectId
from domain.hospital_domain import HospitalDomain
from model.hospital_model import HospitalModel
from database import get_hospital_collection


class HospitalRepository:
    def __init__(self):
        self.collection = get_hospital_collection()
        # self.client = MongoClient("mongodb://localhost:27017")
        # self.db = self.client["hospital_db1"]
        # self.collection = self.db["hospitalss"]

    def create(self, hospital: HospitalDomain) -> HospitalDomain:
        hospital_model = HospitalModel.from_domain(hospital)
        result = self.collection.insert_one(hospital_model.dict(by_alias=True, exclude={"id"}))
        hospital_model.id = result.inserted_id
        return hospital_model.to_domain()

    def list(self) -> list[HospitalDomain]:
        hospitals = self.collection.find()
        return [HospitalModel(**hospital).to_domain() for hospital in hospitals]

    def get(self, hospital_id: str) -> HospitalDomain:
        hospital = self.collection.find_one({"_id": ObjectId(hospital_id)})
        if hospital:
            return HospitalModel(**hospital).to_domain()
        return None

    def update(self, hospital_id: str, hospital: HospitalDomain) -> HospitalDomain:
        hospital_model = HospitalModel.from_domain(hospital)
        update_data = hospital_model.dict(by_alias=True, exclude={"id"})
        self.collection.update_one({"_id": ObjectId(hospital_id)}, {"$set": update_data})
        return self.get(hospital_id)

    def delete(self, hospital_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(hospital_id)})
        return result.deleted_count > 0
