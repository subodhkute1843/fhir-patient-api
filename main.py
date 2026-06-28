from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection
DATABASE_URL = "postgresql://postgres:postgres@localhost/fhir_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#Define Patient Table
class PatientDB(Base):
    __tablename__ = "patients"
    id = Column(String, primary_key=True)
    name = Column(String)
    dob = Column(String)

#create table
Base.metadata.create_all(bind=engine)

app = FastAPI()

class Patient(BaseModel):
    id: str
    name: str
    dob: str

# @app.get("/")
# def hello():
#     return {"message": "FHIR API starting"}

@app.post("/patient")
def create_patient(patient: Patient):
    #pydenting automatically validates : if name or dob is missing, return 400
    db = SessionLocal()
    db_patient = PatientDB(id=patient.id, name=patient.name, dob=patient.dob)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient) 
    return {
        "resourceType": "Patient",
        "id" : db_patient.id,
        "name": db_patient.name,
        "dateOfBirth": db_patient.dob
    }

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    db = SessionLocal()
    p = db.query(PatientDB).filter(PatientDB.id == patient_id).first()
    if not p:
        raise HTTPException(status_code=404,detail="Patient not found")
    return { 
        "resourceType"  : "Patient",
        "id" : p.id,
        "name"  :  p.name,
        "dateOfBirth" : p.dob
    }

@app.get("/patient")
def search_patients(name: str = Query(None)):
    if not name :
        return {"error" : "name query parameter required"}
    db = SessionLocal()
    results = db.query(PatientDB).filter(PatientDB.name.ilike(f"%{name}%")).all()
    return {
        "entry": [{
            "resourceType"  : "Patient",
            "id" : r.id,
            "name"  :  r.name,
            "dateOfBirth" : r.dob
        } for r in results
        ]
    }
