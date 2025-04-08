import sqlite3

conn = sqlite3.connect('example.db')  # << create a "database file"

""" Create a table here """
# cursorObj = conn.cursor()
# cursorObj.execute("""CREATE TABLE employees
#     (
#         id         integer PRIMARY KEY,
#         name       text,
#         salary     real,
#         department text,
#         position   text,
#         hireDate   text
#     )"""
# )
# conn.commit()

""" insert data into our table here """
cursorObj = conn.cursor()
cursorObj.execute("INSERT INTO employees VALUES(5, 'Stefan', 2700, 'Manager', 'IT', '2019-01-07')")
# cursorObj.execute("INSERT INTO employees VALUES(2, 'Jane', 4700, 'HR', 'Manager', '2007-04-06')")
conn.commit()

class Employee(object):
    def __init__(self, myid, name, salary, department, position, hireDate):
        self.myid = myid
        self.name = name
        # ...

    def saveToDB(self, database):
        cursorObj = conn.cursor()
        if database.doesNotContainMeYet():
        # if ";" in self.name or "DROP" in self.name:
        #     print("Nice Try. Not allowing SQL Injections...")
            cursorObj.execute(f"INSERT INTO employees VALUES :i, :n, :s, 'Manager', 'IT', '2019-01-07')",
                              {"i": self.myid, "n": self.name})
        else:
            cursorObj.execute("UPDATE VALUES :n, :s, WHERE id = :id", { "n": self.name})
        database.commit()  # actually sends to the database

    def removeFromDB(self, database):
        pass



class User():

    def authenticate(self):
        if input("Username:") == self.username and input("Password") == self.password():
            # continue doing stuff
            pass
        else:
            print("Sorry, no access")
