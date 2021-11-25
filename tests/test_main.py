def test_main_endpoint(test_app):
    payload = {'SERVICE': 'STARTED'}

    response = test_app.get('/')

    assert response.status_code == 200
    assert response.json() == payload


def test_get_all_persons(test_app):
    payload = {
        'persons': [
            {
                'name': 'Tracy',
                'surname': 'McGrady'
            },
        ]
    }

    response = test_app.get('/persons')

    assert response.status_code == 200
    assert response.json() == payload
