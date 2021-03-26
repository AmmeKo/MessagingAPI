import os
import tempfile
import json

import pytest

from main import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


with app.test_client() as c:
    def test_add_user1():
        response = c.post('/users', data=json.dumps({'name': 'test user 1'}), content_type='application/json')
        assert response.status_code == 201


    def test_add_user2():
        response = c.post('/users', data=json.dumps({'name': 'test user 2'}), content_type='application/json')
        assert response.status_code == 201


    def test_edit_user():
        response = c.put('/users', json={'user_id': 1, 'name': 'Flask_Tester1'}, content_type='application/json')
        assert response.status_code == 200


    def test_send_message1():
        response = c.post('/1/send_message', data=json.dumps({'recipient': 2, 'message': 'test message'}), content_type='application/json')
        assert response.status_code == 201


    def test_send_message2():
        response = c.post('/2/send_message', data=json.dumps({'recipient': 1, 'message': 'test message'}), content_type='application/json')
        assert response.status_code == 201


    def test_get_users():
        response = c.get('/users')
        assert response.status_code == 200


    def test_get_sent():
        response = c.get('/1/sent')
        assert response.status_code == 200


    def test_get_received():
        response = c.get('/1/received')
        assert response.status_code == 200


    def test_delete_message():
        response = c.delete('/1/sent', json={'message_id': 1})
        assert response.status_code == 204


    def test_delete_user1():
        response = c.delete('/users', json={'user_id': 1})
        assert response.status_code == 204


    def test_delete_user2():
        response = c.delete('/users', json={'user_id': 2})
        assert response.status_code == 204
