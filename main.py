from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/hello", response_class=PlainTextResponse)
def hello():
    return "Hello World"

@app.get("/", response_class=PlainTextResponse)
def hello():
    return
