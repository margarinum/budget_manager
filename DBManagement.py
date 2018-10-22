import sqlite3
import psycopg2
import datetime


class DBManagement():

    SQLiteConnString = r'C:\Users\Lenovo\PycharmProjects\budget_manager\DB\db.db'

    def connectToSQLite(self, SQLiteConnString=SQLiteConnString):
        try:
            conn = sqlite3.connect(SQLiteConnString)
            curs = conn.cursor()
            # В SQLite интересно реализованы ключи - если их не включишь вручную, в таблицу может полететь мусор, поэтому:
            curs.execute("PRAGMA foreign_keys = 1")
            if conn:
                return conn;
        except:
            print('Error connecting to database!');
            return False

    def connectToPGSQL(self):
        try:
            conn = psycopg2.connect("dbname='test_db' user='test' host='192.168.1.6' password='test'")
            curs = conn.cursor()
            if conn:
                print('Connected to Database!')
            return conn
        except:
            print('Error connecting to database!');
            return False;

    def extractCategories(self):
        dict_categories = {}
        conn = DBManagement.connectToSQLite(self)
        with conn:
            curs = conn.cursor()
            curs.execute("select * from dict_category")
            while True:
                row = curs.fetchone()
                if row == None:
                    break
                dict_categories[row[0]] = row[1]
            return dict_categories


    def insertingCategory(self, p_sum_in, p_sum_out, p_comment, p_category):
        # Выполним забор категорий
        conn = DBManagement.connectToSQLite(self)
        curs = conn.cursor()
        dict_categories = DBManagement.extractCategories(self)
        try:
            sql_text = '''insert into bm_transaction(sum_in, sum_out, date_oper, comment, id_category)
                      values (?, ?, ?, ?, ?)'''
            # curs.execute(pref + "('3', '+', '18/02/2018 14:26:31', 'comment', 'category')")
            curs.execute(sql_text, (p_sum_in, p_sum_out, datetime.datetime.now(), p_comment, p_category))

            conn.commit()
        except sqlite3.IntegrityError:
            res = 'Ошибка! Такой категории не сущствует!'
        except AssertionError:
            res = 'Ошибка вставки в БД!'
        else:
            res = 'Транзакция добавлена!'
        finally:
            conn.rollback()
            return res