from pydantic import BaseModel

class Books(BaseModel):
    title: str
    author: str
    genre: str
    text: str | None = None

class ItemUpdate(BaseModel):
    field: str
    value: str
