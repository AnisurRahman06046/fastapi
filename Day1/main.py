from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
app = FastAPI()

class ModelName(str,Enum):
    alexnet='alexnet'
    resnet = 'resnet'
    lenet = 'lenet'
    
class Items(BaseModel):
    name:str 
    price:float 
    qty:int 
    description: str | None = None
    
    
    
    
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.post("/create")
async def createItems(items:Items):
    return items

@app.get("/")
async def root():
    return {"msg":"Welcom to fastapi tutorial Day 1"}

# path parameters
@app.get("/items/{id}")
async def getItems(id:int,q:str | None = None):
    if q:
        return {"itemid":id,"q":q}
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


# query parameters
@app.get("/items")
async def readItems(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]


# multiple path and query parameters
@app.get("/users/{userid}/items/{itemid}")
async def read_user_item(userid:int,itemid:str,q:str | None = None, short:bool=False):
    item = {"item_id": userid, "owner_id": itemid}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"this is  an amazing item"})
        
    return item


