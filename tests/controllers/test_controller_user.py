from app.models.user import User as UserModel


def test_get_users(client, db_session):
    users = [
        UserModel(id=1, username='testusername1', email='testemail1@test.com'),
        UserModel(id=2, username='testusername2', email='testemail2@test.com'),
        UserModel(id=3, username='testusername3', email='testemail3@test.com')
    ]
    db_session.add_all(users)
    db_session.commit()

    response = client.get('/api/v1/users')

    assert response.status_code == 200

    data = response.json
    assert len(data) == 3

    for i in range(3):
        assert data[i]['id'] == i+1
        assert data[i]['username'] == f'testusername{i+1}'
        assert data[i]['email'] == f'testemail{i+1}@test.com'
