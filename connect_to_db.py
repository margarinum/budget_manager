# coding=utf-8

import sqlite3
import psycopg2

def connect_to_db_sqlite():
    try:
        conn = sqlite3.connect(r'C:\Users\Lenovo\PycharmProjects\budget_manager\DB\db.db')
        curs = conn.cursor()
        #В SQLite интересно реализованы ключи - если их не включишь вручную, в таблицу может полететь мусор, поэтому:
        curs.execute("PRAGMA foreign_keys = 1")
        return conn
    except:
        return False

def connect_to_db_pgsql():
    try:
        conn = psycopg2.connect("dbname='test_db' user='test' host='192.168.1.6' password='test'")
        curs = conn.cursor()
        return conn
    except:
        return False

print(connect_to_db_pgsql())