# FHIR Patient API

A simple FastAPI application that stores patient data in PostgreSQL using SQLAlchemy.

## Requirements

- Python 3.11+ (or compatible)
- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `psycopg2-binary`

If you are using a virtual environment, activate it first.

## Install

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

## Run

```bash
uvicorn main:app --reload
```

## What it does

- `main.py` creates a FastAPI app
- connects to PostgreSQL via SQLAlchemy
- defines `PatientDB` as a SQLAlchemy table for patient records
- defines `Patient` as a Pydantic request model
- `@app.post("/patient")` inserts a patient into the database
- `@app.get("/patient/{patient_id}")` returns a patient by id
- `@app.get("/patient")` searches patients by `name` query parameter

## Patient POST example

Send this JSON to `POST http://127.0.0.1:8000/patient`:

```json
{
  "id": "123",
  "name": "Jonn Doe",
  "dob": "1990-01-01"
}
```

## Get a patient by id

Request:

```http
GET http://127.0.0.1:8000/patient/123
```

Response example:

```json
{
  "resourceType": "Patient",
  "id": "123",
  "name": "Jonn Doe",
  "dateOfBirth": "1990-01-01"
}
```

## Search patients by name

Request:

```http
GET http://127.0.0.1:8000/patient?name=john
```

Response example:

```json
{
  "entry": [
    {
      "resourceType": "Patient",
      "id": "123",
      "name": "Jonn Doe",
      "dateOfBirth": "1990-01-01"
    }
  ]
}
```

## Database behavior

- The app uses PostgreSQL via the `DATABASE_URL` configured in `main.py`.
- `Base.metadata.create_all(bind=engine)` creates the `patients` table automatically.
- Data is stored persistently in the database.

## Notes

- `uvicorn` is the web server used to run the FastAPI app.
- `--reload` restarts the server automatically when code changes.
- `python main.py` alone does not start the server unless you add a run block in `main.py`.
