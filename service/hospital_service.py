from schema.hospital_schema import HospitalCreate, HospitalUpdate, HospitalResponse
from repository.hospital_repo_mongo import HospitalRepository
from domain.hospital_domain import HospitalDomain


def get_hospital_service():
    return HospitalService(HospitalRepository())


class HospitalService:
    def __init__(self, repository: HospitalRepository):
        self.repository = repository

    def create_hospital(self, hospital: HospitalCreate) -> HospitalResponse:
        hospital_domain = HospitalDomain(id=None, **hospital.dict())
        created_hospital = self.repository.create(hospital_domain)
        return HospitalResponse(**created_hospital.to_dict())

    def list_hospitals(self) -> list[HospitalResponse]:
        hospitals = self.repository.list()
        return [HospitalResponse(**hospital.to_dict()) for hospital in hospitals]

    def update_hospital(self, hospital_id: str, hospital: HospitalUpdate) -> HospitalResponse:
        existing_hospital = self.repository.get(hospital_id)
        if not existing_hospital:
            return None
        update_data = hospital.dict(exclude_unset=True)
        updated_hospital_domain = HospitalDomain(**{**existing_hospital.to_dict(), **update_data})
        updated_hospital = self.repository.update(hospital_id, updated_hospital_domain)
        return HospitalResponse(**updated_hospital.to_dict())

    def delete_hospital(self, hospital_id: str) -> bool:
        return self.repository.delete(hospital_id)
