import os

import pytest
from sqlmodel import Session
from sqlalchemy.sql import text
from starlette.testclient import TestClient

from app.db import engine
from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="session")
def test_engine():
    """
    This is needed to make sure connecting to the TEST DB,
    and not to the DEV DB.

    scope="session" means that it will be run while starting all tests,
    and will not run again
    """
    os.environ['Database'] = 'mytest_test'
    return engine()


@pytest.fixture(scope="function", autouse=True)
def test_session(test_engine):
    """
    Beginning of every test:
        1) populate TEST DB with data
    After every test:
        2) delete all data from TEST DB
    """
    with Session(test_engine) as session:
        # Insert some boilerplate data
        with open('insert_data.sql') as f:
            statement = text(f.read())
            session.execute(statement)
            session.commit()

        yield session

        # Remove all data
        with open('truncate_data.sql') as f:
            statement = text(f.read())
            session.execute(statement)
            session.commit()
