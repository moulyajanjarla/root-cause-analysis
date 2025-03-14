from fastapi import FastAPI
from .schemas import LogRequest, LogResponse
from .log_processor import process_log

app = FastAPI()

@app.post("/analyze-log", response_model=LogResponse)
def analyze_log(request: LogRequest):
    processed_log = process_log(request.log)
    return {"processed_log": processed_log}
