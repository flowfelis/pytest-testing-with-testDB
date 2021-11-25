from app.models import Person
from fastapi import status


def test_main_endpoint(client):
    payload = {'SERVICE': 'STARTED'}

    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == payload


def test_get_all_persons(client, session):
    payload = [
        {
            'name': 'Max',
            'surname': 'Payne'
        }
    ]

    session.add(
        Person(
            name='Max',
            surname='Payne'
        )
    )
    session.commit()
    response = client.get('/persons')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == payload


def test_create_a_person(client):
    payload = {
        'name': 'Anthony',
        'surname': 'Hopkins'
    }

    response = client.post('/persons', json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['name'] == 'Anthony'
    assert data['surname'] == 'Hopkins'
