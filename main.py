from flask import Flask, make_response, request
from http_functions import (api_delete_message, api_delete_user,
    api_get_received, api_get_sent, api_get_users,
    api_new_user, api_send_message, api_edit_user)
from db_functions import create_conn, create_tables


app = Flask(__name__)

# db name/location
db = r"messagingAPI.db"

conn = None
try:
    conn = create_conn(db)
except:
    make_response('Unable to establish connection', 500)


# make tables if DB is new/empty
try:
    create_tables(conn)
except:
    make_response('Unable to create tables', 501)


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_users():
    if request.method == 'GET':
        return api_get_users(conn)
    elif request.method == 'POST':
        return api_new_user(conn)
    elif request.method == 'PUT':
        return api_edit_user(conn)
    elif request.method == 'DELETE':
        return api_delete_user(conn)


@app.route('/<user_id>/send_message', methods=['POST'])
def api_message(user_id):
    return api_send_message(conn, user_id)


@app.route('/<user_id>/sent', methods=['GET', 'DELETE'])
def api_sent(user_id):
    if request.method == 'GET':
        return api_get_sent(conn, user_id)
    elif request.method == 'DELETE':
        return api_delete_message(conn)


@app.route('/<user_id>/received', methods=['GET', 'DELETE'])
def api_received(user_id):
    if request.method == 'GET':
        return api_get_received(conn, user_id)
    elif request.method == 'DELETE':
        return api_delete_message(conn)


if __name__ == '__main__':
    app.run(debug=True)
