from fastapi import FastAPI
import uvicorn

from app.main import app as fastapi_app

app = fastapi_app

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=7860)
    # final fix