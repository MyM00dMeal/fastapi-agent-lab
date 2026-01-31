from app.services import add, subtract, multiply, divide

def calculator_agent(operation: str, a: float, b: float):
    if operation == "add":
        return add(a, b), "Addition successful"

    elif operation == "sub":
        return subtract(a, b), "Subtraction successful"

    elif operation == "mul":
        return multiply(a, b), "Multiplication successful"

    elif operation == "div":
        return divide(a, b), "Division successful"

    else:
        raise ValueError("Invalid operation. Use add, sub, mul, or div")
