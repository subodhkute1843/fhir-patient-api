from fastapi import FastAPI
from pydantic import BaseModel
   
app = FastAPI()

class Patient(BaseModel):
    id: str
    name: str
    dob: str

@app.get("/")
def hello():
    return {"message": "FHIR API starting"}


@app.post("/patients")
def create_patient(patient: Patient):
    return {
        "resourceType": "Patient",
        "id" : patient.id,
        "name": patient.name,
        "dateOfBirth": patient.dob
    }

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    #For now, return mock data (we'll add database later)
    return { 
        "resourceType"  : "Patient",
        "id" : patient_id,
        "name"  :  "John Doe",
        "dateOfBirth" : "1990-01-01"
    }