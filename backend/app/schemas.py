# Example: Sample schema for request and response
from pydantic import BaseModel

class LogRequest(BaseModel):
    data: str

class LogResponse(BaseModel):
    processed_data: str
