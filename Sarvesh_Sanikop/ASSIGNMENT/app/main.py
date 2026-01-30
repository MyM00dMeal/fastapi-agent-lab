from fastapi import FastAPI
from .schemas import AgentRequest, AgentResponse
from .agent import run_agent

app = FastAPI(title="FastAPI Agent")

@app.post("/agent", response_model=AgentResponse)
def agent_endpoint(req: AgentRequest):
    result = run_agent(req.message)
    return AgentResponse(response=result)
