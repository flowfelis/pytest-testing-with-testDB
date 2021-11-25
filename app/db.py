import os

from sqlmodel import Session
from sqlmodel import create_engine


def get_session():
    postgres_db_uri = (
        'postgresql+psycopg2://'
        f'{os.environ["Username"]}:'
        f'{os.environ["Password"]}@'
        f'{os.environ["Host"]}:'
        f'{os.environ["Port"]}/'
        f'{os.environ["Database"]}'
    )

    engine = create_engine(postgres_db_uri)
    with Session(engine) as session:
        yield session
