from fastapi import FastAPI
from api.hospital_api import router as hospital_router
from api.patient_api import router as patient_router
from api.reporting_doctor_api import router as reporting_doctor_router
from api.technician_api import router as technician_router

app = FastAPI()

app.include_router(hospital_router, tags=["Hospital"])

app.include_router(patient_router, tags=["patient"])

app.include_router(reporting_doctor_router, tags=["reporting_doctor"])

app.include_router(technician_router, tags=["technician_router"])

