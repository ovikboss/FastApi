import asyncio
from typing import List
from typing import Optional
from sqlalchemy import  select, delete, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .config import USER, DBNAME, PORT, PASSWORD
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from .models import Book,UserBook, User




class DataBase:

    engine = create_async_engine(f"postgresql+asyncpg://{USER}:{PASSWORD}@localhost:{PORT}/{DBNAME}",
                                 isolation_level="SERIALIZABLE", )

    async def create_book(self,book_name, author, genre):
        try:
            async with AsyncSession(self.engine) as session:
                book = Book(book_name=book_name, author=author, genre=genre)
                async with session.begin():
                    session.add_all([book])
        except Exception as ex:
            print(ex)


    async def get_all_books(self):
        try:
            data = []
            async with AsyncSession(self.engine) as session:
                stmt = select(Book)
                result = await session.execute(stmt)
                for cont in result.scalars(stmt):
                    data.append(cont)
                return data
        except Exception as ex:
            print(ex)


    async def get_book(self, ID):
        try:
            data = []
            async with AsyncSession(self.engine) as session:
                stmt = select(Book).where(Book.id == ID)
                result = await session.execute(stmt)
                for cont in result.scalars(stmt):
                    data.append(cont)
                return data
        except Exception as ex:
            print(ex)


    async def change_book(self,id, column ,new_value):
        try:
            async with AsyncSession(self.engine) as session:
                print(column)
                match column:
                    case "book_name":
                        stmt = update(Book).where(Book.id == id).values(book_name = new_value)
                        await session.execute(stmt)
                        await session.commit()
                    case "text":
                        stmt = update(Book).where(Book.id == id).values(text = new_value)
                        await session.execute(stmt)
                        await session.commit()
                    case "genre":
                        stmt = update(Book).where(Book.id == id).values(genre = new_value)
                        await session.execute(stmt)
                        await session.commit()
            return "Changed"
        except Exception as ex:
            print(ex)
    
    async def remove_book(self, ID:int):
        try:
            async with AsyncSession(self.engine) as session:
                stmt = delete(Book).where(Book.id == ID)
                result = await session.execute(stmt)
                await session.commit()
            return "Deleted"
        except Exception as ex:
            print(ex)

    async def subscribe(self, user_id, book_id):
        try:
            async with AsyncSession(self.engine) as session:
                user_book = UserBook(user_id = user_id, book_id = book_id )
                async with session.begin():
                    session.add_all([user_book])

        except Exception as ex:
            print(ex)

    async def get_user_book(self, user_id):
        try:
            data = []
            async with AsyncSession(self.engine) as session:
                stmt = select(Book).where(Book.id.in_(select(UserBook.book_id).where(UserBook.user_id == user_id)))
                result = await session.execute(stmt)
                print(stmt)
                for cont in result.scalars(stmt):
                    data.append(cont)
                return data
        except Exception as ex:
            print(ex)





