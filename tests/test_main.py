def test_main_endpoint(test_app):
    payload = {'SERVICE': 'STARTED'}
    response = test_app.get('/')

    assert response.status_code == 200
    assert response.json() == payload
