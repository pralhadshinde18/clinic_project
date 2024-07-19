from fastapi import APIRouter, Depends
from schema.technician_schema import TechnicianCreate, TechnicianResponse
from service.technician_service import TechnicianService, get_technician_service

router = APIRouter()


@router.post("/technicians", response_model=TechnicianResponse)
def create_technician(technician: TechnicianCreate, service: TechnicianService = Depends(get_technician_service)):
    return service.create_technician(technician)


@router.get("/technicians", response_model=list[TechnicianResponse])
def list_technicians(service: TechnicianService = Depends(get_technician_service)):
    return service.list_technicians()


@router.get("/hospitals/{hospital_id}/technicians", response_model=list[TechnicianResponse])
def list_technicians_by_hospital(hospital_id: str, service: TechnicianService = Depends(get_technician_service)):
    return service.list_technicians_by_hospital(hospital_id)
