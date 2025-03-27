import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from src.routes.base import  Books, ItemUpdate,Subscribe, UserAuth
from src.routes.base import UserData
from src.DB.db import *
from fastapi import  Request

templates = Jinja2Templates(directory="templates")
router = APIRouter()

data_base = DataBase()

@router.post("/addbook/")
async def addbook(book: Books):
    print(book)
    asyncio.create_task(data_base.create_book(book.title, book.author, book.genre))
    return "Книга добавлена"


@router.get("/")
async def index():
    return "hello world"

@router.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "message": "Добро пожаловать!!", 'title': 'О нас'})



@router.get("/books/{id}")
async def get_one_book(id: int):
    try:
        result1 = asyncio.create_task(data_base.get_book(id))
        return await result1
    except:
        return "404"


@router.get("/books")
async def get_books():
    try:
        result1 = asyncio.create_task(data_base.get_all_books())
        return await result1
    except:
        return "404"

@router.get("/book_delete/{id}")
async def book_delete(id:int):
    try:
        result = asyncio.create_task(data_base.remove_book(id))
        return await result
    except Exception as ex:
        return "error"

@router.put("/change_book/{id}")
async def book_delete(id:int, item_update:ItemUpdate):
    try:
        result = asyncio.create_task(data_base.change_book(id, item_update.field, item_update.value))
        return await result
    except Exception as ex:
        return "error"

@router.get("/subscribe/{book_id}/{user_id}")
async def subscribe_book(book_id, user_id):
    result1 = asyncio.create_task(data_base.subscribe(user_id = int(user_id), book_id= int(book_id)))
    return await result1


@router.get("/user/{user_id}")
async def get_my_book(user_id):
    result1 = asyncio.create_task(data_base.get_user_book(user_id = int(user_id)))
    return await result1

@router.post("/auth")
async def auth(user: UserAuth):
    return await data_base.auth(username= user.username, password=user.password)

@router.post("/reg")
async def reg(user: UserData):
    return  await data_base.reg(username= user.username, password = user.password, email= user.email)

@router.get("/unsubscribe/{book_id}/{user_id}")
async def subscribe_book(book_id, user_id):
    result1 = asyncio.create_task(data_base.unsubscribe(user_id = int(user_id), book_id= int(book_id)))
    return await result1