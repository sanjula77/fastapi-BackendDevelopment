from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PostData(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/post")
async def create_item(payload: PostData):
    return {"item": payload}