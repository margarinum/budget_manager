from DBManagement import *
import sqlite3
import datetime

class Categories():

    def extractCategories(self):
        dict_categories = {}
        conn = DBManagement.connectToSQLite(self)
        with conn:
            curs = conn.cursor()
            curs.execute("select * from dict_category")
            while True:
                row = curs.fetchone()
                if row is None:
                    break
                dict_categories[row[0]] = row[1]
            return dict_categories

    def insertingCategory(self):
        conn = DBManagement.connectToSQLite(self);
        curs = conn.cursor();

