from pydantic import BaseModel

class LogRequest(BaseModel):
    log: str

class LogResponse(BaseModel):
    processed_log: str
