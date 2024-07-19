from fastapi import APIRouter, Depends
from schema.patient_schema import PatientCreate, PatientResponse
from service.patient_service import PatientService, get_patient_service

router = APIRouter()


@router.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate, service: PatientService = Depends(get_patient_service)):
    return service.create_patient(patient)


@router.get("/patients", response_model=list[PatientResponse])
def list_patients(service: PatientService = Depends(get_patient_service)):
    result = service.list_patients()
    return result


@router.get("/hospitals/{hospital_id}/patients", response_model=list[PatientResponse])
def list_patients_by_hospital(hospital_id: str, service: PatientService = Depends(get_patient_service)):
    return service.list_patients_by_hospital(hospital_id)
