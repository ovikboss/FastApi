import asyncio
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, select, delete, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from .config import USER, DBNAME, PORT, PASSWORD
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(f"postgresql+asyncpg://{USER}:{PASSWORD}@localhost:{PORT}/{DBNAME}",
                             isolation_level="SERIALIZABLE", )


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    book_name: Mapped[str] = mapped_column(String(30))
    author: Mapped[str] = mapped_column(String(30))
    genre: Mapped[str]
    text: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, book_name={self.book_name!r}, Author={self.author!r})"


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

