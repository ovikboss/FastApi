from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey, String
from typing import Optional, List

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


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30),unique=True)
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30),unique=True)

class UserBook(Base):
    __tablename__ = "user_book"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    book_id:Mapped[int] = mapped_column(ForeignKey('books.id'))

    def __repr__(self):
        return f"User_id : {self.user_id}, Book_id: {self.book_id}"
