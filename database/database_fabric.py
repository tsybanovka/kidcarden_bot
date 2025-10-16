import sqlite3


class database_fabric:

    con:sqlite3.Connection
    cur:sqlite3.Cursor

    def __init__(self):

        self.con = sqlite3.connect("database/db.db")
        self.cur = self.con.cursor()


    def __exit__(self, exc_type, exc_val, exc_tb):

        self.con.close()