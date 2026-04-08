from fastapi import FastAPI
from app.models import AgentAction
from app.env import KrushiMitraEnv

app = FastAPI(title="KrushiMitra AI OpenEnv")

env = KrushiMitraEnv(task_name="crop_selection")


@app.get("/")
def home():
    return {"message": "KrushiMitra AI is running"}


@app.post("/set_task/{task_name}")
def set_task(task_name: str):
    global env
    env = KrushiMitraEnv(task_name=task_name)
    env.reset()
    return {"message": f"Task set to {task_name}"}

@app.post("/reset")
def reset_env():
    return env.reset()


@app.get("/state")
def get_state():
    return env.state()


@app.post("/step")
def step_env(action: AgentAction):
    return env.step(action)