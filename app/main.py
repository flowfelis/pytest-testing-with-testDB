from fastapi import FastAPI
from sqlmodel import Session
from sqlmodel import select

from app.db import engine
from app.models import Person

app = FastAPI()


@app.get('/')
def index():
    return {'SERVICE': 'STARTED'}


@app.get('/persons')
def get_all_persons():
    with Session(engine()) as session:
        statement = select(Person.name, Person.surname)
        results = session.exec(statement)
        return {'persons': results.all()}
