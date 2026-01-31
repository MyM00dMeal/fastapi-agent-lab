def calculate(op: str, a: float, b: float):
    if op == "add":
        return a + b
    if op == "subtract":
        return a - b
    if op == "multiply":
        return a * b
    if op == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Invalid operation"
