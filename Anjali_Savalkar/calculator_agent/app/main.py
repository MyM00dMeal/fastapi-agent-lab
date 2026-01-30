from fastapi import FastAPI,HTTPException
from app.schemas import *
from app.services import *
from app.agent import *

from app.storage import *


app = FastAPI(title="Calculator AI Agent")

agent=CalculatorAgent()

@app.get("/")
def home():
    return {"message":"Welcome to the Calculator AI Agent!"}

@app.post("/calculate",response_model=CalculationResponse)
def calculate(req:CalculationRequest):
    try:
        return agent.decide_and_execute(req.operation,req.a,req.b)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))




@app.get("/history")
def get_history():
    return list(calculation_db.values())

@app.get('/history/{calc_id}')
def get_calculation(calc_id:int):
    if calc_id not in calculation_db:
        raise HTTPException(status_code=404,detail="Calculation not found")
    return calculation_db[calc_id]

@app.put('/history_update/{clac_id}')
def update_calculation(calc_id:int , update:UpdateCalculation):
    if calc_id not in calculation_db:
        raise HTTPException(status_code=404,detail="Calculation not found")
    record=calculation_db[calc_id]
    if update.operation:
        try:
            utils.validate_operation(update.operation)
            record['operation']=update.operation
        except ValueError as e:
            raise HTTPException(status_code=400,detail=str(e))
        

    if update.a is not None:
        record['a']=update.a

    if update.b is not None:
        record['b']=update.b
    try:
        new_result=agent.decide_and_execute(record['operation'],record['a'],record['b'])
        record['result']=new_result['result']
        calculation_db[calc_id]=record
        return record   
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    


@app.delete('/history/{calc_id}')
def delete_calculation(calc_id:int):
    if calc_id not in calculation_db:
        raise HTTPException(status_code=404,detail="Calculation not found")
    del calculation_db[calc_id]
    return {"message":"Calculation deleted successfully"}