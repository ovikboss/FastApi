import asyncio
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String, select, delete
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


    def change_book(self):
        pass



async def main():
    db = DataBase()
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # await create_book("Преступление и Наказание", "Фёдор Достоевский", "Роман")
    # result = asyncio.create_task(db.get_all_books())
    result1 = asyncio.create_task(db.get_book(1))
    # print(*await result,sep="\n")
    print(*await result1, sep="\n")
    await db.engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
