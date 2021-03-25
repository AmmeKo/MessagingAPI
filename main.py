from flask import Flask, make_response, jsonify, request
from db_functions import *
from datetime import datetime


app = Flask(__name__)

# db name/location
db = r"messagingAPI.db"
conn = create_conn(db)
#cur = conn.cursor()

# make tables if DB is new/empty
create_tables(conn)


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_users():
    if request.method == "GET":
        return make_response(jsonify(get_users(conn)), 200)
    elif request.method == 'POST':
        content = request.json
        name = content['name']
        return make_response(jsonify(new_user(conn, name)), 201)
    elif request.method == 'PUT':
        content = request.json
        user_id = content['user_id']
        name = content['name']
        return make_response(jsonify(update_user(conn, user_id, name)), 200)
    elif request.method == "DELETE":
        content = request.json
        user_id = content['user_id']
        delete_all_messages(conn, user_id)
        delete_user(conn, user_id)
        return make_response(jsonify({}), 204)


@app.route('/<user_id>/send_message', methods=['POST'])
def api_message(user_id):
    if request.method == 'POST':
        content = request.json
        recipient = content['recipient']
        message = content['message']
        date = datetime.now()
        return make_response(jsonify(new_message(conn, user_id, recipient, message, date)), 201)


@app.route('/<user_id>/sent', methods=['GET', 'DELETE'])
def api_messages_sent(user_id):
    if request.method == "GET":
        message_obj = get_sent(conn, user_id)
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response(jsonify(message_obj), 404)
    elif request.method == "DELETE":
        content = request.json
        message_id = content['message_id']
        delete_message(conn, message_id)
        return make_response(jsonify({}), 204)


@app.route('/<user_id>/received', methods=['GET', 'DELETE'])
def api_messages_received(user_id):
    if request.method == "GET":
        message_obj = get_received(conn, user_id)
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response(jsonify(message_obj), 404)
    elif request.method == "DELETE":
        content = request.json
        message_id = content['message_id']
        delete_message(conn, message_id)
        return make_response(jsonify({}), 204)



if __name__ == '__main__':
    app.run(debug=True)
