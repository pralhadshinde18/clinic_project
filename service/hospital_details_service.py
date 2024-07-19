from schema.hospital_details_schema import HospitalDetailsResponse
from repository.technician_repo import TechnicianRepository
from repository.reporting_doctor_repo import ReportingDoctorRepository


class HospitalDetailsService:
    def __init__(self, technician_repo: TechnicianRepository, reporting_doctor_repo: ReportingDoctorRepository):
        self.technician_repo = technician_repo
        self.reporting_doctor_repo = reporting_doctor_repo

    def get_hospital_details(self, hospital_id: str) -> HospitalDetailsResponse:
        technicians = self.technician_repo.find_by_hospital_id(hospital_id)
        reporting_doctors = self.reporting_doctor_repo.find_by_hospital_id(hospital_id)
        return HospitalDetailsResponse(
            technicians=[technician.to_dict() for technician in technicians],
            reporting_doctors=[doctor.to_dict() for doctor in reporting_doctors]
        )


def get_hospital_details_service():
    return HospitalDetailsService(TechnicianRepository(), ReportingDoctorRepository())
