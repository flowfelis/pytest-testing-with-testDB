from fastapi import FastAPI
from fastapi import Depends
from fastapi import status
from sqlmodel import Session
from sqlmodel import select

from app.db import get_session
from app.models import Person
from app.models import PersonResponse

app = FastAPI()


@app.get('/')
def index():
    return {'SERVICE': 'STARTED'}


@app.get('/persons')
def get_all_persons(session: Session = Depends(get_session)):
    persons = session.exec(select(Person.name, Person.surname)).all()
    return persons


@app.post('/persons', response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
def create_a_person(*, person: Person, session: Session = Depends(get_session)):
    session.add(person)
    session.commit()
    session.refresh(person)
    return person
