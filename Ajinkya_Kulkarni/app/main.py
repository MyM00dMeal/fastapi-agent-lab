from fastapi import FastAPI
from schemas import AgentRequest,AgentResponse
from agent import run_agent

app = FastAPI()

@app.post("/agent",response_model=AgentResponse)
def agent_endpoint(request: AgentRequest):
    try:
        result = run_agent(request.task,request.data)
        return AgentResponse(success=True,result=result)
    except Exception as e:
        return AgentResponse(success = False,error = str(e))


