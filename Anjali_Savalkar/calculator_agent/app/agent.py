from app import utils,services,storage

class CalculatorAgent:
    def decide_and_execute(self,operation: str,a: float,b: float) ->dict:
        utils.validate_operation(operation)

        if operation == "add":
            result=services.add(a,b)
        elif operation == "subtract":
            result=services.subtract(a,b)
        elif operation == "multiply":
            result=services.multiply(a,b)
        elif operation == "divide":
            result=services.divide(a,b)
      

        id=storage.generate_id()
        record={

            "id":id,
            "operation":operation,
            "a":a,
            "b":b,
            "result":result,
            "status":"completed"
        }
        storage.calculation_db[id]=record
        return record