from schema.technician_schema import TechnicianCreate, TechnicianResponse
from repository.technician_repo import TechnicianRepository
from domain.technician_domain import TechnicianDomain


def get_technician_service():
    return TechnicianService(TechnicianRepository())


class TechnicianService:
    def __init__(self, repository: TechnicianRepository):
        self.repository = repository

    def create_technician(self, technician: TechnicianCreate) -> TechnicianResponse:
        technician_domain = TechnicianDomain(id=None, **technician.dict())
        created_technician = self.repository.create(technician_domain)
        return TechnicianResponse(**created_technician.to_dict())

    def list_technicians(self) -> list[TechnicianResponse]:
        technicians = self.repository.list()
        return [TechnicianResponse(**technician.to_dict()) for technician in technicians]

    def list_technicians_by_hospital(self, hospital_id: str) -> list[TechnicianResponse]:
        technicians = self.repository.find_by_hospital_id(hospital_id)
        return [TechnicianResponse(**technician.to_dict()) for technician in technicians]
