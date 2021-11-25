from sqlmodel import SQLModel, Field


class Person(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    surname: str
