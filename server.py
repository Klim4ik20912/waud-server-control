import sqlite3
import random

db = sqlite3.connect("waud.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
id INT,
login TEXT,
password TEXT,
nickname TEXT,
email TEXT,
friends_ids INT
)""")

db.commit()


def check(login, password):
    for logins in sql.execute(f"SELECT login FROM users"):
        print(logins)
        if login in logins:
            pas_bd = sql.execute(f'SELECT password FROM users WHERE login = ?', (login,)).fetchone()[0]
            if password == pas_bd:
                return True
                print('пароль верный, ты успешно вошел в аккаунт')
            else:
                print('пароль неверен!')
                return False


def registration(login, password, nickname, email):
    all_logins = sql.execute("SELECT login FROM users").fetchall()
    print(all_logins)
    sql.execute("SELECT * FROM users WHERE login = ?", (login,))
    if sql.fetchone() is None:
        sql.execute("SELECT * FROM users WHERE email = ?", (email,))
        if sql.fetchone() is None:
            sql.execute("SELECT * FROM users WHERE nickname = ?", (nickname,))
            if sql.fetchone() is None:
                random_id = random.randint(10000000, 9999999999)
                sql.execute(f"INSERT INTO users VALUES ({random_id}, ?, ?, ?, ?, 'NULL')",
                            (login, password, nickname, email))
                db.commit()
                return True
            else:
                return 103
        else:
            return 102
    else:
        return 101


#def reg():
    #login = input('придумай логин ')
    #password = input('придумай пароль ')
    #nickname = input('придумай никнейм ')
    #email = input('напиши свою почту ')
    #a = registration(login, password, nickname, email)
    #print(a)


#@function get user friends by users ids - not working
#def my_friends(id):
    #for b in sql.execute(f"SELECT friends_ids FROM users WHERE id = {id}"):
        #if b[0] != 'NULL':
            #ids = b
            #print(ids)
            #friends_nickname = sql.execute(f"SELECT nickname FROM users WHERE id = {ids[0]}").fetchall()
            #return friends_nickname
        #else:
            #return 'No one friend :('

def token_check(token, id):
    # get token from database
    pass
