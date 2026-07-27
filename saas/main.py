from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="saas-awesome")

class Request(BaseModel):
    input: str
    options: dict = {}


@app.get("/health")
def health():
    return {"status": "ok", "service": __name__}

@app.get("/readyz")
def readyz():
    return {"status": "ready", "service": __name__}

@app.get("/")
def home():
    return {"name": "saas-awesome", "description": "😎 Awesome lists about all kinds of interesting topics", "source": "https://github.com/sindresorhus/awesome"}

@app.post("/run")
def run(req: Request):
    # TODO: wrap the actual tool logic here
    return {"status": "prototype", "input": req.input, "message": "Coming soon"}
