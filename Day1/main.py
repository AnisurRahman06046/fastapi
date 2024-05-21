from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class ModelName(str,Enum):
    alexnet='alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get("/")
async def root():
    return {"msg":"Welcom to fastapi tutorial Day 1"}

# path parameters
@app.get("/items/{id}")
async def getItems(id:int):
    return {"itemid":id}


@app.get("/models/{model_name}")
async def getModels(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"msg":"DL"}
    if model_name.value=='lenet':
        return {"model_name":model_name,"msg":"LeCNN"}
    return  {"model_name":model_name,"msg":"have some rsiduals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}