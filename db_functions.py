import sqlite3
from datetime import datetime


# CREATE CONNECTION
def create_conn(db):
    conn = sqlite3.connect(db, check_same_thread=False)
    return conn


# CREATE TABLES
def create_tables(conn):
    # sql for new tables
    sql_users = '''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL);'''
    sql_messages = '''CREATE TABLE IF NOT EXISTS messages (
                        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        recipient INTEGER NOT NULL,
                        message TEXT,
                        date TEXT NOT NULL);'''  # date not a data type option in SQLite
    cur = conn.cursor()
    cur.execute(sql_users)
    cur.execute(sql_messages)


# INSERT DATA
# new user
def new_user(conn, name):
    sql_new_user = "INSERT INTO users (name) values('{}');".format(name)
    cur = conn.cursor()
    cur.execute(sql_new_user)
    conn.commit()


# new message
def new_message(conn, user_id, recipient, message, date):
    sql_new_message = '''INSERT INTO messages (user_id, recipient, message, date)
                         values({},{},'{}','{}');'''.format(user_id, recipient, message, date)
    cur = conn.cursor()
    cur.execute(sql_new_message)
    conn.commit()


# RETRIEVE DATA
# users
def get_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows


# sent messages
def get_sent(conn, user_id):
    now = datetime.now()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages WHERE user_id = {} ORDER BY date desc LIMIT 100".format(user_id))
    rows = cur.fetchall()
    recent_messages = []
    for message in rows:
        m_date = datetime.strptime(message[-1], '%Y-%m-%d %H:%M:%S.%f')
        if now.day - m_date.day <= 30:
            recent_messages.append(message)
    return recent_messages


# received messages
def get_received(conn, user_id):
    now = datetime.now()
    cur = conn.cursor()
    cur.execute("SELECT * FROM messages WHERE recipient = {} ORDER BY date desc LIMIT 100".format(user_id))
    rows = cur.fetchall()
    recent_messages = []
    for message in rows:
        m_date = datetime.strptime(message[-1], '%Y-%m-%d %H:%M:%S.%f')
        if now.day - m_date.day <= 30:
            recent_messages.append(message)
    return recent_messages


# UPDATE DATA
def update_user(conn, user_id, name):
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = '{}' WHERE user_id = {}".format(name, user_id))
    conn.commit()


# DELETE DATA
# users
# future feature: add option to delete multiple users
def delete_user(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE user_id = {}".format(user_id))
    conn.commit()


# messages
# delete ALL when deleting user
def delete_all_messages(conn, user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE user_id = {}".format(user_id))
    cur.execute("DELETE FROM messages WHERE recipient = {}".format(user_id))
    conn.commit()


'''future feature: add option to delete multiple messages as well as 
option to delete by additional criteria (date, sender/recipient, etc.)'''
def delete_message(conn, message_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE message_id = {}".format(message_id))
    conn.commit()