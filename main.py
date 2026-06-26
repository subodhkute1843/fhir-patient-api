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