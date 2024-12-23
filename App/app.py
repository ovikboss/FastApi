import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from DataBase.db import *


class Books(BaseModel):
    title: str
    author: str
    genre: str
    text: str | None = None


app = FastAPI()


@app.post("/addbook/")
async def addbook(book: Books):
    print(book.author)
    # asyncio.create_task(create_book(book.title, book.author, book.genre))
    return "Книга добавлена"


@app.get("/")
async def index():
    return "hello world"


@app.get("/books/{id}")
async def get_one_book(id: int):
    try:
        result1 = asyncio.create_task(get_book(id))
        return await result1
    except:
        return "404"


@app.get("/books")
async def get_one_book():
    try:
        result1 = asyncio.create_task(get_all_books())
        return await result1
    except:
        return "404"


if __name__ == "__main__":
    uvicorn.run("app:app")
