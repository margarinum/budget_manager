# coding=utf-8

import time
import sqlite3
from connect_to_db import connect_to_db_sqlite
from connect_to_db import connect_to_db_pgsql

# Данная программа представляет из себя жалкие попытки вспомнить питон
"""

Для начала суть:
Планируется программа, в которой будет фронт и бэк энды.
Начинать будем с бэкэнда

"""

#Глобальные переменные
list_func = []
list_out = []
dict_categories = {}

#Соединение с БД SQLite и PostgreSQL находятся в connect_to_db.py
conn = connect_to_db_pgsql()

if conn:
    print('Connected to Database!')
else:
    print('Error connecting to database!')

curs = conn.cursor()

#Достанем существующие категории для SQLite
def extract_categories():
    with conn:
        curs.execute("select * from test_schema.dict_category")
        while True:
            row = curs.fetchone()
            if row == None:
                break
            dict_categories[row[0]]=row[1]
        return dict_categories

extract_categories()
# Объявим и присвоим тестовые значения

g_sum_in = 3
g_sum_out = 0
g_comment = 'comment'
g_category = "3"

#Функция вставки в файл и БД
def inserting_into_file (p_sum_in, p_sum_out, p_comment, p_category):
    #Выполним забор категорий
    extract_categories()
    if not p_category in dict_categories:
        res = 'Категории не существует!'
        return res
    else:
        nowdate = time.strftime("%d/%m/%Y %H:%M:%S")
        list_func.append(g_sum_in)
        list_func.append(g_sum_out)
        list_func.append(nowdate)
        list_func.append(p_category)
        list_func.append(p_comment)

        file_open = open('archive.txt', 'a')
        string_to_file = str(list_func)
        file_open.write(string_to_file+'\n')
        file_open.close()

        try:
            sql_text = '''insert into bm_transaction(sum_in, sum_out, date_oper, comment, id_category)
                  values (?, ?, ?, ?, ?)'''
            #curs.execute(pref + "('3', '+', '18/02/2018 14:26:31', 'comment', 'category')")
            curs.execute(sql_text, (p_sum_in, p_sum_out, nowdate, p_comment, p_category))

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

#Функция чтения из файла
def read_file ():
    file = open('archive.txt')
    for line in file:
        list_out.append(line)

#Тут должен начинаться класс работы с категориями
#Добавим категорию и вытянем еще раз все из БД
#Добавить проверку на существование

def create_category(p_category_name):
    try:
        sql_text = '''insert into dict_category (nm_category)
                      values (?)'''
        curs.execute(sql_text, (p_category_name,))
        conn.commit()
        extract_categories()
        res = 'Success'
    except sqlite3.IntegrityError:
        res = 'Ошибка! Категория существует'
    except:
        res = 'Ошибка'
    finally:
        conn.rollback()
        return res


'''a = create_category(g_category)
print(a)
print(dict_categories)'''
'''
res_transaction = curs.execute("select * from bm_transaction")
res = res_transaction.fetchall()
print(res)

#Вызов функции вставки в файл
print (inserting_into_file(g_sum_in, g_sum_out, g_comment, g_category))

'''