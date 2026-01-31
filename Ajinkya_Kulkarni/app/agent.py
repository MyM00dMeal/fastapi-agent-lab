from services import calculate

def run_agent(task:str,data:dict):
    if task == "calculate":
        return calculate(
            data["a"],
            data["b"],
            data["operation"]
        )
    elif task == "uppercase":
        return data["text"].upper()
    else:
        raise ValueError("Unknown Task")