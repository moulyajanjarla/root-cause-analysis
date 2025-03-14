from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for log data
class LogEntry(BaseModel):
    log_data: str
    timestamp: str

@app.get("/")
def read_root():
    return {"message": "Root Cause Analysis API is running"}

# Process logs endpoint
@app.post("/process-logs")
def process_logs(log_entry: LogEntry):
    processed_logs = [f"Processed: {log_entry.log_data} at {log_entry.timestamp}"]
    return {"status": "success", "processed_logs": processed_logs}
