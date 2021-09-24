from pydantic import BaseModel

class Item(BaseModel):
    a: int = None
    b: int = None