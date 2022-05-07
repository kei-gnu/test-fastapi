from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title="I make a toDo Application with FastAPI",
    description="FastAPI tutorial: Let's make a simple toDo Application with FastAPI(and starlette)",
    version='1.0 beta test'
)

def index_test(request: Request):
    return {'Hello': 'World!!'}