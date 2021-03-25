import sqlite3
from sqlite3 import Error


# create connection
def create_conn(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error:
        print(Error, 'DB Connection Failed')
    return conn


# create tables
def create_tables(cur):
    # sql for new tables
    sql_users = '''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL);'''
    sql_messages = '''CREATE TABLE IF NOT EXISTS messages (
                        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        recipient INTEGER NOT NULL,
                        message TEXT,
                        date TEXT NOT NULL);''' # maybe date should be BLOB?
    try:
        cur.execute(sql_users)
        cur.execute(sql_messages)
    except Error:
        print(Error, 'Tables could not be created')


# INSERT DATA
# new user
def new_user(conn, name):
    sql_new_user = '''INSERT INTO users (name)
                      values('{}');'''.format(name)
    try:
        cur = conn.cursor()
        cur.execute(sql_new_user)
        conn.commit()
    except Error:
        print(Error, 'Could not add user.')


# new message
def new_message(conn, user_id, recipient, message, date):
    sql_new_message = '''INSERT INTO messages (user_id, recipient, message, date)
                         values({},{},'{}','{}');'''.format(user_id, recipient, message, date)
    try:
        cur = conn.cursor()
        cur.execute(sql_new_message)
        conn.commit()
    except Error:
        print(Error, 'Could not send message')


# RETRIEVE DATA
# users
def get_users(cur):
    cur.execute("SELECT * FROM USERS")
    rows = cur.fetchall()
    return rows

# sent messages
def get_sent(cur, user_id): #need to add datetime/max return
    cur.execute("SELECT * FROM messages WHERE user_id = {}".format(user_id))
    rows = cur.fetchall()
    return rows


# received messages
def get_received(cur, user_id): #need to add datetime/max return
    cur.execute("SELECT * FROM messages WHERE recipient = {} LIMIT 2".format(user_id))
    rows = cur.fetchall()
    return rows


# DELETE DATA
# users
def delete_user(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = {}".format(user_id))
    conn.commit()


# messages (which ones should they get to delete? By date, by recipient, all, none?
# For now, users can just delete ALL their messages
def delete_messages(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE user_id = {}".format(user_id))
    cur.execute("DELETE FROM messages WHERE recipient = {}".format(user_id))
    conn.commit()
