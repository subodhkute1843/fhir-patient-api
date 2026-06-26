from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
   
app = FastAPI()

#Temporory storage (will use database later)
patients_db = {}

class Patient(BaseModel):
    id: str
    name: str
    dob: str

@app.get("/")
def hello():
    return {"message": "FHIR API starting"}


@app.post("/patients")
def create_patient(patient: Patient):
    #pydenting automatically validates : if name or dob is missing, return 400
    patients_db[patient.id] = patient.dict()
    return {
        "resourceType": "Patient",
        "id" : patient.id,
        "name": patient.name,
        "dateOfBirth": patient.dob
    }

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404,detail="Patient not found")
    p = patients_db[patient_id]
    return { 
        "resourceType"  : "Patient",
        "id" : p["id"],
        "name"  :  p["name"],
        "dateOfBirth" : p["dob"]
    }

@app.get("/patient")
def search_patients(name: str = Query(None)):
    if not name :
        return {"error" : "name query parameter required"}
    
    results = []
    for patient_id, p in patients_db.items():
        if name.lower() in p["name"].lower() :
            results.append({
                "resourceType" : "Patient",
                "id" : p["id"],
                "name"  :  p["name"],
                "dateOfBirth" : p["dob"]
            })

    return {"entry" : results}
