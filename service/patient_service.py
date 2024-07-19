from schema.patient_schema import PatientCreate, PatientUpdate, PatientResponse
from repository.patient_repo import PatientRepository
from domain.patient_domain import PatientDomain


def get_patient_service():
    return PatientService(PatientRepository())


class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def create_patient(self, patient: PatientCreate) -> PatientResponse:
        patient_domain = PatientDomain(id=None, **patient.dict())
        created_patient = self.repository.create(patient_domain)
        return PatientResponse(**created_patient.to_dict())

    def list_patients(self) -> list[PatientResponse]:
        patients = self.repository.list()
        return [PatientResponse(**patient.to_dict()) for patient in patients]

    def list_patients_by_hospital(self, hospital_id: str) -> list[PatientResponse]:
        patients = self.repository.find_by_hospital_id(hospital_id)
        return [PatientResponse(**patient.to_dict()) for patient in patients]
