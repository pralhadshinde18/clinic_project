from fastapi import APIRouter, Depends
from schema.reporting_doctor_schema import ReportingDoctorCreate, ReportingDoctorResponse
from service.reporting_doctor_service import ReportingDoctorService, get_reporting_doctor_service

router = APIRouter()


@router.post("/reporting_doctors", response_model=ReportingDoctorResponse)
def create_reporting_doctor(reporting_doctor: ReportingDoctorCreate, service: ReportingDoctorService = Depends(get_reporting_doctor_service)):
    return service.create_reporting_doctor(reporting_doctor)


@router.get("/reporting_doctors", response_model=list[ReportingDoctorResponse])
def list_reporting_doctors(service: ReportingDoctorService = Depends(get_reporting_doctor_service)):
    return service.list_reporting_doctors()


@router.get("/hospitals/{hospital_id}/reporting_doctors", response_model=list[ReportingDoctorResponse])
def list_reporting_doctors_by_hospital(hospital_id: str, service: ReportingDoctorService = Depends(get_reporting_doctor_service)):
    return service.list_reporting_doctors_by_hospital(hospital_id)
