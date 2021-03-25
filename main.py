from flask import Flask, make_response, jsonify, request
from db_functions import *
from datetime import datetime


app = Flask(__name__)

# db name/location
db = r"messagingAPI.db"
conn = create_conn(db)
cur = conn.cur()

# make tables if DB is new/empty
create_tables(cur)


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_users():
    if request.method == "GET":
        return make_response(jsonify(fetch_users()), 200)
        # users = get_users(cur)
        # for item in users:
        #    print(item)
    elif request.method == 'POST':
        content = request.json
        user_id = content['user_id']
        users.insert(content)
        return make_response(jsonify(fetch_user(user_id)), 201)  # 201 = Created
        # new_user(conn, 1, 'Amme')
    elif request.method == 'PUT':
        content = request.json
        users.update(content, ['id'])
        user_obj = fetch_users()
        return make_response(jsonify(user_obj), 200)
    elif request.method == "DELETE":
        messages.delete(id=message_obj)
        return make_response(jsonify({}), 204)
    # delete_user(conn, 1)


@app.route('/<user_id>/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        content = request.json
        message_id = content['message_id']
        messages.insert(content)
        return make_response(jsonify(fetch_message(message_id)), 201)  # 201 = Created
    # new_message(conn, 1, 2, 'hello there', datetime.now())
    pass


@app.route('/<user_id>/sent', methods=['GET', 'DELETE'])
def api_messages():
    if request.method == "GET":
        message_obj = fetch_messages_sender()
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response(jsonify(message_obj), 404)
        # sent = get_sent(cur, 1)
        # for item in sent:
        #    print(item)
    elif request.method == "DELETE":
        messages.delete(id=message_obj)
        return make_response(jsonify({}), 204)
        # delete_messages(conn, 1)


@app.route('/<user_id>/received', methods=['GET', 'DELETE'])
def api_messages():
    if request.method == "GET":
        message_obj = fetch_messages_sender()
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response(jsonify(message_obj), 404)
        # received = get_received(cur, 2)
        # for item in received:
        #    print(item)
    elif request.method == "DELETE":
        messages.delete(id=message_obj)
        return make_response(jsonify({}), 204)
        # delete_messages(conn, 1)



if __name__ == '__main__':
    app.run(debug=True)
