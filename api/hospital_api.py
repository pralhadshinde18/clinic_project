from fastapi import APIRouter, Depends, HTTPException
from schema.hospital_schema import HospitalCreate, HospitalUpdate, HospitalResponse
from service.hospital_service import HospitalService, get_hospital_service

router = APIRouter()


@router.post("/hospitals", response_model=HospitalResponse)
def create_hospital(hospital: HospitalCreate, service: HospitalService = Depends(get_hospital_service)):
    return service.create_hospital(hospital)


@router.get("/hospitals", response_model=list[HospitalResponse])
def list_hospitals(service: HospitalService = Depends(get_hospital_service)):
    return service.list_hospitals()


@router.put("/hospitals/{hospital_id}", response_model=HospitalResponse)
def update_hospital(hospital_id: str, hospital: HospitalUpdate, service: HospitalService = Depends(get_hospital_service)):
    updated_hospital = service.update_hospital(hospital_id, hospital)
    if not updated_hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return updated_hospital


@router.delete("/hospitals/{hospital_id}", response_model=bool)
def delete_hospital(hospital_id: str, service: HospitalService = Depends(get_hospital_service)):
    deleted = service.delete_hospital(hospital_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return True
