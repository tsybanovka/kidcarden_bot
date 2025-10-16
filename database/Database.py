import sqlite3, json
from database.database_fabric import database_fabric
from database.data_classes import INFORMATION


class Database(database_fabric):

    def get_partners(self) -> INFORMATION.partners:

        self.cur.execute('SELECT partners FROM INFORMATION')

        data = eval(self.cur.fetchone())

        return data
    def get_metodics(self) -> INFORMATION.metodics:

        self.cur.execute('SELECT metodics FROM INFORMATION')

        path = self.cur.fetchone()

        with open(path, "r", encoding="utf-8") as file:
            data = json.loads(file.readline())

        return data
    def get_projects(self) -> INFORMATION.projects:

        self.cur.execute('SELECT projects FROM INFORMATION')

        data = self.cur.fetchone()

        return data
    def get_licence(self) -> INFORMATION.licence:

        self.cur.execute('SELECT licence FROM INFORMATION')

        data = self.cur.fetchone()

        return data
    def get_teachers_info(self) -> INFORMATION.teachers_info:

        self.cur.execute('SELECT teachers_info FROM INFORMATION')

        data = self.cur.fetchone()

        return data
    def get_contacts(self) -> INFORMATION.contacts:

        self.cur.execute('SELECT contacts FROM INFORMATION')

        data = self.cur.fetchone()

        return data