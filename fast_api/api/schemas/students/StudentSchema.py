from typing import Optional

from sqlmodel import SQLModel, Field


class StudentCreate(SQLModel):
    nome: str = Field(index=True)


class ResponseSchema(SQLModel):
    id: int
    nome: str