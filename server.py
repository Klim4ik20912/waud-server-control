import sqlite3
import random
import wmi

c = wmi.WMI()

db = sqlite3.connect("waud.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
id INT,
login TEXT,
password TEXT,
nickname TEXT,
email TEXT,
friends_ids INT,
token TEXT
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
                sql.execute(f"INSERT INTO users VALUES ({random_id}, ?, ?, ?, ?, 'NULL', 'NULL')",
                            (login, password, nickname, email))
                db.commit()
                return True
            else:
                return 103
        else:
            return 102
    else:
        return 101


def reg():
    login = input('придумай логин ')
    password = input('придумай пароль ')
    nickname = input('придумай никнейм ')
    email = input('напиши свою почту ')
    a = registration(login, password, nickname, email)
    print(a)


#@function get user friends by users ids - not working
def my_friends(id):
    # need json
    pass


def token_check(token, id):
    user_token = sql.execute(f"SELECT token FROM users WHERE id = {id}").fetchone()
    if user_token[0] == token:
        return True
    else:
        return False


def app_activity():
    if (c.Win32_Process(name='dota2.exe')):
        return 'Dota 2'
    elif (c.Win32_Process(name='osu!.exe')):
        return 'Osu!'
    elif (c.Win32_Process(name='csgo.exe')):
        return 'Counter-Strike: Global Offensive'
    elif (c.Win32_Process(name='rust.exe')):
        return 'Rust'
    elif (c.Win32_Process(name='gta5.exe')):
        return 'Grand Theft Auto V'
    elif (c.Win32_Process(name='Discord.exe')):
        return 'Discord'
    elif (c.Win32_Process(name='opera.exe')):
        return 'Opera-GX'
