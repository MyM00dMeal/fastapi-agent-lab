from pydantic import BaseModel, Field


from typing import List, Optional


class CalculationRequest(BaseModel):
    operation:str=Field(..., description="The operation to perform: add, subtract, multiply, divide",examples=["add","subtract","multiply","divide"])
    a:float=Field(..., description="The first operand")
    b:float=Field(..., description="The second operand")

class CalculationResponse(BaseModel):
    id:int
    operation:str
    a:float 
    b:float
    result:float
    status:str


class UpdateCalculation(BaseModel):
    operation:Optional[str]
    a:Optional[float]
    b:Optional[float]