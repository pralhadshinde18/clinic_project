from fastapi import APIRouter, Depends
from service.hospital_details_service import HospitalDetailsService, get_hospital_details_service
from schema.hospital_details_schema import HospitalDetailsResponse

router = APIRouter()


@router.get("/hospitals/{hospital_id}/details", response_model=HospitalDetailsResponse)
def get_hospital_details(hospital_id: str, service: HospitalDetailsService = Depends(get_hospital_details_service)):
    return service.get_hospital_details(hospital_id)
