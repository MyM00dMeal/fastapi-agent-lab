from pydantic import BaseModel

class CalculatorRequest(BaseModel):
    operation: str   # add, sub, mul, div
    a: float
    b: float

class CalculatorResponse(BaseModel):
    result: float
    message: str
