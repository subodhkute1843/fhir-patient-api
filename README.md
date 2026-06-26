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
- the endpoint returns:

```json
{"message": "FHIR API starting"}
```

## Notes

- `uvicorn` is the web server used to run the FastAPI app.
- `--reload` restarts the server automatically when code changes.
- `python main.py` alone does not start the server unless you add a run block in `main.py`.
