from typing import Optional

from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class Person(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    surname: str


class PersonResponse(BaseModel):
    name: str
    surname: str
