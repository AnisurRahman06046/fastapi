from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"msg":"Welcom to fastapi tutorial Day 1"}