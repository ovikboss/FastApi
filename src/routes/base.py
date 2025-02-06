from pydantic import BaseModel

class Books(BaseModel):
    title: str
    author: str
    genre: str
    text: str | None = None

    def __repr__(self):
        return f"{self.author,self.title,self.genre}"

class ItemUpdate(BaseModel):
    field: str
    value: str

class Subscribe(BaseModel):
    user_id:int
    book_id:int


class UserData(BaseModel):
    username: str
    password: str
    email:str


class UserAuth(BaseModel):
    username: str
    password: str
