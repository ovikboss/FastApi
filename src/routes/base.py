from pydantic import BaseModel

class Books(BaseModel):
    title: str
    author: str
    genre: str
    text: str | None = None

class ItemUpdate(BaseModel):
    field: str
    value: str

class Subscribe(BaseModel):
    user_id:int
    book_id:int
