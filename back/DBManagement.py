import sqlite3
import psycopg2
import os


class DBManagement():


    #SQLiteConnString = r'C:\Users\Lenovo\PycharmProjects\budget_manager\DB\db.db'
    #Достанем нахождение БД
    cwd = os.getcwd()
    SQLiteConnString = (cwd + '\\' + 'DB'+'\\'+'db.db')



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




