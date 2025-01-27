import uvicorn
from fastapi import FastAPI
from .base import  Books, ItemUpdate
from .DB.db import *


app = FastAPI()

data_base = DataBase()

@app.post("/addbook/")
async def addbook(book: Books):
    print(book.author)
    asyncio.create_task(data_base.create_book(book.title, book.author, book.genre))
    return "Книга добавлена"


@app.get("/")
async def index():
    return "hello world"


@app.get("/books/{id}")
async def get_one_book(id: int):
    try:
        result1 = asyncio.create_task(data_base.get_book(id))
        return await result1
    except:
        return "404"


@app.get("/books")
async def get_books():
    try:
        result1 = asyncio.create_task(data_base.get_all_books())
        return await result1
    except:
        return "404"

@app.get("/book_delete/{id}")
async def book_delete(id:int):
    try:
        result = asyncio.create_task(data_base.remove_book(id))
        return await result
    except Exception as ex:
        return "error"

@app.put("/change_book/{id}")
async def book_delete(id:int, item_update:ItemUpdate):
    try:
        result = asyncio.create_task(data_base.change_book(id, item_update.field, item_update.value))
        return await result
    except Exception as ex:
        return "error"


if __name__ == "__main__":
    uvicorn.run("routes:app")
