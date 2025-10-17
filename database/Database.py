import sqlite3, json
from database.database_fabric import database_fabric
from database.data_classes import INFORMATION


class Database_read(database_fabric):

    def get_partners(self):

        self.cur.execute('SELECT partners FROM INFORMATION')

        data = eval(self.cur.fetchone()[0])

        return data
    def get_metodics(self):

        self.cur.execute('SELECT metodics FROM INFORMATION')

        path = self.cur.fetchone()[0]

        with open(path, "r", encoding="utf-8") as file:
            data = json.loads(file.readline())

        return data
    def get_projects(self):

        self.cur.execute('SELECT projects FROM INFORMATION')

        data = self.cur.fetchone()[0]

        return data
    def get_licence(self):

        self.cur.execute('SELECT licence FROM INFORMATION')

        data = self.cur.fetchone()[0]

        return data
    def get_teachers_info(self):

        self.cur.execute('SELECT teachers_info FROM INFORMATION')

        data = self.cur.fetchone()[0]

        return data
    def get_contacts(self):

        self.cur.execute('SELECT contacts FROM INFORMATION')

        data = self.cur.fetchone()[0]

        return data
    def get_groups_teachers(self):

        self.cur.execute('SELECT groups_teachers FROM INFORMATION')

        path = self.cur.fetchone()[0]

        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads("".join(file.readlines()))

        return data