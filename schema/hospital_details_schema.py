from pydantic import BaseModel
from typing import List
from schema.technician_schema import TechnicianResponse
from schema.reporting_doctor_schema import ReportingDoctorResponse


class HospitalDetailsResponse(BaseModel):
    technicians: List[TechnicianResponse]
    reporting_doctors: List[ReportingDoctorResponse]
