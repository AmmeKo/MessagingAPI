from flask import Flask, make_response, jsonify, request
from db_functions import *
from datetime import datetime


app = Flask(__name__)

# db name/location
db = r"messagingAPI.db"


conn = create_conn(db)
cur = conn.cur()


create_tables(cur)

#new_user(conn, 1, 'Amme')
#new_message(conn, 1, 2, 'hello there', datetime.now())

#users = get_users(cur)
#for item in users:
#    print(item)

#sent = get_sent(cur, 1)
#for item in sent:
#    print(item)

#received = get_received(cur, 2)
#for item in received:
#    print(item)

#delete_messages(conn, 1)
#delete_user(conn, 1)

'''
def fetch_user(user_id):
    return users.find_one(user_id=user_id)


def fetch_users():
    user_list = []
    for user in users:
        user_list.append(user)
    return user_list


def fetch_message(message_id):
    return messages.find_one(message_id=message_id)


def fetch_messages_sender():
    sent = []
    for message in messages:
        sent.append(message)
    return sent
    #going to need 100/30days bit here


def fetch_messages_recipient():
    received = []
    for message in messages:
        received.append(message)
    return received
    #going to need 100/30days bit here


@app.route('/users', methods=['GET', 'PUT', 'POST', 'DELETE'])
def api_users():
    if request.method == "GET":
        return make_response(jsonify(fetch_users()), 200)
    elif request.method == 'POST':
        content = request.json
        user_id = content['user_id']
        users.insert(content)
        return make_response(jsonify(fetch_user(user_id)), 201)  # 201 = Created
    elif request.method == 'PUT':
        content = request.json
        users.update(content, ['id'])
        user_obj = fetch_users()
        return make_response(jsonify(user_obj), 200)


@app.route('/messages/sent', methods=['GET', 'POST', 'DELETE'])
def api_messages():
    if request.method == "GET":
        message_obj = fetch_messages_sender()
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response(jsonify(message_obj), 404)
    elif request.method == 'POST':
        content = request.json
        message_id = content['message_id']
        messages.insert(content)
        return make_response(jsonify(fetch_message(message_id)), 201)  # 201 = Created
    elif request.method == "PUT":  # Updates the book
        content = request.json
        messages.update(content, ['book_id'])
        message_obj = fetch_messages_sender()
        return make_response(jsonify(message_obj), 200)
    elif request.method == "DELETE":
        messages.delete(id=message_obj)

        return make_response(jsonify({}), 204)


#@app.route('/messages/received', methods=['GET', 'PUT', 'DELETE'])


#@app.route('/messages/<message_id>', methods=['GET', 'PUT', 'DELETE'])
'''

if __name__ == '__main__':
    app.run(debug=True)
