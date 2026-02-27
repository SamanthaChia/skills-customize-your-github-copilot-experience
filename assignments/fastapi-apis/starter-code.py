from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

# simple in-memory storage
items = {}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return items[item_id]

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items[item.id] = item
    return item

# add more routes as needed
