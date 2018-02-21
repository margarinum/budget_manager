# coding=utf-8

import time
import sqlite3

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

#Объявим и присвоим тестовые значения
#Тест
g_sum_ent = 3
g_operation = '+'
g_comment = 'comment'
g_category = 1

try:
    conn = sqlite3.connect(r'C:\Users\Lenovo\PycharmProjects\budget_manager\DB\db.db')
    curs = conn.cursor()
    #В SQLite интересно реализованы ключи - если их не включишь вручную, в таблицу может полететь мусор, поэтому:
    curs.execute("PRAGMA foreign_keys = 1")
except:
    print("Ошибка подключения к БД!")

#Достанем существующие категории
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Продолжить функционал извлечения из БД

#Тут должен начинаться класс работы с файлом

#Функция вставки в файл
def inserting_into_file (p_sum_ent, p_operation, p_category, p_comment):
    nowdate = time.strftime("%d/%m/%Y %H:%M:%S")

    list_func.append(p_sum_ent)
    list_func.append(p_operation)
    list_func.append(nowdate)
    list_func.append(p_category)
    list_func.append(p_comment)

    file_open = open('archive.txt', 'a')
    string_to_file = str(list_func)
    file_open.write(string_to_file+'\n')
    file_open.close()

    try:
        sql_text = '''insert into bm_transaction(sum_tr, type_oper, date_oper, id_category, comment)
                values (?, ?, ?, ?, ?)'''
        #curs.execute(pref + "('3', '+', '18/02/2018 14:26:31', 'comment', 'category')")
        curs.execute(sql_text, (p_sum_ent, p_operation, nowdate, p_category, p_comment))
        conn.commit()
    except sqlite3.IntegrityError:
        res = 'Ошибка! Такой категории не сущствует!'
    except AssertionError:
        res = 'Ошибка вставки в БД!'
    else:
        res = 'Транзакция добавлена!'
    finally:
        conn.rollback()
        print(res)
        return res



#Вызов функции вставки в файл
inserting_into_file(g_sum_ent, g_operation, g_category, g_comment)

#Функция чтения из файла
def read_file ():
    file = open('archive.txt')
    for line in file:
        list_out.append(line)

#Тут должен начинаться класс работы с категориями

def create_category(p_category_name):
    try:
        with open('categories.txt', 'r') as file:
        #file_open.write(p_category_name+'\n')
            list_func = file.readlines()
            print(list_func)
    #вставить проверку существования категории
            assert p_category_name+'\n' not in list_func
            file = open('categories.txt', 'a')
            file.write(p_category_name + '\n')
            return 'Категория добавлена'
    except AssertionError:
        return 'Категория существует'
    finally:
        file.close()

#a = create_category(g_category)
#print(a)
'''
res_transaction = curs.execute("select * from bm_transaction")
res = res_transaction.fetchall()
print(res)
'''