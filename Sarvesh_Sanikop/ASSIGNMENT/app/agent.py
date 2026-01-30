from .services import calculate

def run_agent(message: str) -> str:
    parts = message.lower().split()

    if len(parts) != 3:
        return "Use: operation number number"

    op, a, b = parts

    try:
        a = float(a)
        b = float(b)
    except:
        return "Numbers required"

    result = calculate(op, a, b)
    return str(result)
