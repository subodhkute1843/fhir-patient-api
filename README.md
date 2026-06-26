# FHIR Patient API

A simple FastAPI application that exposes a root endpoint and returns a JSON message.

## Requirements

- Python 3.11+ (or compatible)
- `fastapi`
- `uvicorn`

If you are using a virtual environment, activate it first.

## Install

```bash
pip install fastapi uvicorn
```

## Run

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/
```

## What it does

- `main.py` creates a FastAPI app
- `@app.get("/")` defines a GET endpoint for `/`
- `@app.post("/patients")` defines a POST endpoint to create a patient resource
- `@app.get("/patient/{patient_id}")` returns a patient by id
- `@app.get("/patient")` searches patients by `name` query parameter
- the root endpoint returns:

```json
{"message": "FHIR API starting"}
```

## Patient POST example

Send this JSON to `POST http://127.0.0.1:8000/patients`:

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

## Storage behavior

- `patients_db` is a temporary in-memory dictionary.
- Data is only saved while the server is running.
- When the server restarts, the stored patients are lost.

## Notes

- `uvicorn` is the web server used to run the FastAPI app.
- `--reload` restarts the server automatically when code changes.
- `python main.py` alone does not start the server unless you add a run block in `main.py`.
