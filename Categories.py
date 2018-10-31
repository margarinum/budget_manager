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

    def insertingCategory(self, p_category_name):
        conn = DBManagement.connectToSQLite(self);
        curs = conn.cursor();
        res = ''

        sql_text = '''insert into dict_category(nm_category)
                      values (?)'''
            # curs.execute(pref + "('3', '+', '18/02/2018 14:26:31', 'comment', 'category')")
        curs.execute(sql_text, p_category_name)

        conn.commit()
        res = 'Категория добавлена!'

        #res = 'Ошибка вставки в БД!'
        return res


