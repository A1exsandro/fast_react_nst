from typing import Optional

from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    __tablename__ = "student"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    nome: str = Field(unique=True, index=True)
    