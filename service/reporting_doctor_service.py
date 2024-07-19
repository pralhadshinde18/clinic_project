from schema.reporting_doctor_schema import ReportingDoctorCreate, ReportingDoctorUpdate, ReportingDoctorResponse
from repository.reporting_doctor_repo import ReportingDoctorRepository
from domain.reporting_doctor_domain import ReportingDoctorDomain


def get_reporting_doctor_service():
    return ReportingDoctorService(ReportingDoctorRepository())


class ReportingDoctorService:
    def __init__(self, repository: ReportingDoctorRepository):
        self.repository = repository

    def create_reporting_doctor(self, reporting_doctor: ReportingDoctorCreate) -> ReportingDoctorResponse:
        reporting_doctor_domain = ReportingDoctorDomain(id=None, **reporting_doctor.dict())
        created_reporting_doctor = self.repository.create(reporting_doctor_domain)
        return ReportingDoctorResponse(**created_reporting_doctor.to_dict())

    def list_reporting_doctors(self) -> list[ReportingDoctorResponse]:
        reporting_doctors = self.repository.list()
        return [ReportingDoctorResponse(**reporting_doctor.to_dict()) for reporting_doctor in reporting_doctors]

    def list_reporting_doctors_by_hospital(self, hospital_id: str) -> list[ReportingDoctorResponse]:
        reporting_doctors = self.repository.find_by_hospital_id(hospital_id)
        return [ReportingDoctorResponse(**reporting_doctor.to_dict()) for reporting_doctor in reporting_doctors]
