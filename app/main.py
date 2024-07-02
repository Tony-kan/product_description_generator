from fastapi import FastAPI, APIRouter, HTTPException


app = FastAPI()
todo_router = APIRouter()
# app.include_router(todo_router, prefix="/api/v1/todos")


@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}
