from pymongo import MongoClient


class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]


db_inst = Database(uri="mongodb://localhost:27017", db_name="hospital_db1")


def get_technician_collection():
    return db_inst.get_collection("technicians")


def get_reporting_doctor_collection():
    return db_inst.get_collection("reporting_doctors")


def get_hospital_collection():
    return db_inst.get_collection("hospitalss")


def get_patient_collection():
    return db_inst.get_collection("patients")
