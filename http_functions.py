from flask import make_response, jsonify, request
from db_functions import (new_message, new_user, get_users, get_received, get_sent,
    update_user, delete_user, delete_all_messages, delete_message)
from datetime import datetime


# USER FUNCTIONS
def api_get_users(conn):
    try:
        user_list = get_users(conn)
        if user_list:
            return make_response(jsonify(user_list), 200)
        else:
            return make_response('No Users Found', 400)
    except:
        return make_response('Unable to complete request', 500)


def api_new_user(conn):
    content = request.json
    if 'name' not in content:
        return make_response('"name" field required', 400)
    name = content['name']
    try:
        return make_response(jsonify(new_user(conn, name)), 201)
    except:
        return make_response('Error creating user', 500)


def api_edit_user(conn):
    content = request.json
    if 'user_id' not in content or 'name' not in content:
        return make_response('Both "user_id" and "name" field required', 400)
    user_id = content['user_id']
    name = content['name']
    try:
        return make_response(jsonify(update_user(conn, user_id, name)), 200)
    except:
        return make_response('Error editing user', 500)


def api_delete_user(conn):
    content = request.json
    if 'user_id' not in content:
        return make_response('"user_id" field required', 400)
    user_id = content['user_id']
    try:
        delete_all_messages(conn, user_id)
        delete_user(conn, user_id)
        return make_response(jsonify({}), 204)
    except:
        return make_response('Unable to complete request', 500)


# NEW MESSAGE
def api_send_message(conn, user_id):
    content = request.json
    if 'recipient' not in content or 'message' not in content:
        return make_response("Missing required information", 400)
    recipient = content['recipient']
    message = content['message']
    date = datetime.now()
    try:
        return make_response(jsonify(new_message(conn, user_id, recipient, message, date)), 201)
    except:
        return make_response("Unable to send message", 500)


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


# DELETE SINGLE MESSAGE
def api_delete_message(conn):
    content = request.json
    if 'message_id' not in content:
        return make_response('"message_id" field required', 400)
    message_id = content['message_id']
    try:
        delete_message(conn, message_id)
        return make_response(jsonify({}), 204)
    except:
        return make_response('Unable to delete message', 500)