import os
from sqlmodel import create_engine


def engine():
    postgres_db_uri = (
        'postgresql+psycopg2://'
        f'{os.environ["Username"]}:'
        f'{os.environ["Password"]}@'
        f'{os.environ["Host"]}:'
        f'{os.environ["Port"]}/'
        f'{os.environ["Database"]}'
    )

    return create_engine(postgres_db_uri)
