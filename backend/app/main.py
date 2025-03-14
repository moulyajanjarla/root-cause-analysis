from fastapi import FastAPI
from .log_processor import process_log

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Root Cause Analysis API is running"}

@app.post("/process/")
def process(data: str):
    result = process_log(data)
    return {"processed_data": result}
