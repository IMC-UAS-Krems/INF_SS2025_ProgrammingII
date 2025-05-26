import sqlite3
import PasswordUtil
# Run this only once - to create the tables
conn = sqlite3.connect('tictactoe.db')
cursorObj = conn.cursor()
cursorObj.execute("""CREATE TABLE "users" (
                        "name"	TEXT,
                        "email"	TEXT,
                        "password"	TEXT,
                        PRIMARY KEY("email")
                     )""")

cursorObj.execute("""CREATE TABLE "games" (
                        "player_email"	TEXT,
                        "game_start_time"	TEXT,
                        "gameid"	INTEGER PRIMARY KEY AUTOINCREMENT,
                        FOREIGN KEY("player_email") REFERENCES "users"("email")
                     )""")

# Add sample users
sampleUserData = [{"name": "John Smith", "email": "john32@gma90.com", "password": "Pa§§"},
                    {"name": "Megae Rach", "email": "eegae@msit.com", "password": "Paßß"},
                    {"name": "Raue Polg", "email": "polg@zurlea.com", "password": "Pa&&"},
                    {"name": "Ruaos Weuis", "email": "weis@nuies.com", "password": "Pa##"},
                    {"name": "Juilos Juisr", "email": "juils@23ag.com", "password": "Pa.."},
                    {"name": "Vuis Lutis", "email": "luts@jesas.com", "password": "Pa//"},
                 ]

sqlite_insert_with_param = """INSERT INTO users
                          (name, email, password) 
                          VALUES (?, ?, ?);"""
for user in sampleUserData:
    data_tuple = (user["name"], user["email"], PasswordUtil.hash_password(user["password"]))
    cursorObj.execute (sqlite_insert_with_param, data_tuple)
    conn.commit()