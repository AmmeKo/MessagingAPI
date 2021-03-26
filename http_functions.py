from flask import make_response, jsonify, request
from db_functions import *


# USER FUNCTIONS
def api_get_users(conn):
    try:
        user_list = get_users(conn)
        if user_list:
            return make_response(jsonify(user_list), 200)
        else:
            return make_response('No Users Found', 404)
    except:
        return make_response('Unable to complete request', 500)


def api_new_user(conn):
    try:
        content = request.json
        name = content['name']
        return make_response(jsonify(new_user(conn, name)), 201)
    except:
        return make_response('"name" field required', 404)


def api_edit_user(conn):
    try:
        content = request.json
        user_id = content['user_id']
        name = content['name']
        return make_response(jsonify(update_user(conn, user_id, name)), 200)
    except:
        return make_response('Both "user_id" and "name" field required', 404)


def api_delete_user(conn):
    try:
        content = request.json
        user_id = content['user_id']
    except:
        return make_response('"user_id" field required', 404)
    try:
        delete_all_messages(conn, user_id)
        delete_user(conn, user_id)
        return make_response(jsonify({}), 204)
    except:
        return make_response('Unable to complete request', 500)


# NEW MESSAGE
def api_send_message(conn, user_id):
    try:
        content = request.json
        recipient = content['recipient']
        message = content['message']
        date = datetime.now()
        return make_response(jsonify(new_message(conn, user_id, recipient, message, date)), 201)
    except:
        return make_response("Missing required information", 404)


# SENT MESSAGES
def api_get_sent(conn, user_id):
    try:
        message_obj = get_sent(conn, user_id)
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response('No Messages Found', 404)
    except:
        return make_response('Unable to complete request', 500)


def api_delete_sent(conn):
    try:
        content = request.json
        message_id = content['message_id']
        delete_message(conn, message_id)
        return make_response(jsonify({}), 204)
    except:
        return make_response('"message_id" field required', 404)


# RECEIVED MESSAGES
def api_get_received(conn, user_id):
    try:
        message_obj = get_received(conn, user_id)
        if message_obj:
            return make_response(jsonify(message_obj), 200)
        else:
            return make_response('No Messages Found', 404)
    except:
        return make_response('Unable to complete request', 500)


def api_delete_received(conn):
    try:
        content = request.json
        message_id = content['message_id']
        delete_message(conn, message_id)
        return make_response(jsonify({}), 204)
    except:
        return make_response('"message_id" field required', 404)