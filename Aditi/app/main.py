from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.agent import calculator_agent
from app.schemas import CalculatorRequest, CalculatorResponse

app = FastAPI(title="Calculator AI Agent")

templates = Jinja2Templates(directory="templates")


# ================= UI ROUTES =================

@app.get("/", response_class=HTMLResponse)
def show_calculator(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )


@app.post("/", response_class=HTMLResponse)
def calculate_ui(
    request: Request,
    operation: str = Form(...),
    a: float = Form(...),
    b: float = Form(...)
):
    try:
        result, _ = calculator_agent(operation, a, b)
    except Exception as e:
        result = str(e)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )


# ================= REST API ROUTE =================

@app.post("/api/calculate", response_model=CalculatorResponse)
def calculate_api(request: CalculatorRequest):
    try:
        result, message = calculator_agent(
            request.operation,
            request.a,
            request.b
        )
        return CalculatorResponse(result=result, message=message)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
