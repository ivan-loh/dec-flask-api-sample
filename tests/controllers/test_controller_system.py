def test_get_server_time(unsafe_client):

    from datetime import datetime

    response = unsafe_client.get('api/v1/system/time')

    assert response.status_code == 200

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert response.json == {'time': now}
