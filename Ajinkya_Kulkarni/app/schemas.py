from pydantic import BaseModel
from typing import Optional,Dict,Any

class AgentRequest(BaseModel):
    task: str
    data: Dict[str,Any]

class AgentResponse(BaseModel):
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None