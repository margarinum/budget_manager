# coding=utf-8

from DBManagement import *
from Transactions import *

# Данная программа представляет из себя жалкие попытки вспомнить питон
"""

Для начала суть:
Планируется программа, в которой будет фронт и бэкэнды.
Начинать будем с бэкэнда

"""

# Объявим и присвоим тестовые значения

g_sum_in = 3
g_sum_out = 0
g_comment = 'comment'
g_category = "3"

#Глобальные переменные
list_func = []
list_out = []
dict_categories = {}

#Функция вставки в файл и БД


#Функция чтения из файла
def read_file ():
    file = open('archive.txt')
    for line in file:
        list_out.append(line)

#Тут должен начинаться класс работы с категориями
#Добавим категорию и вытянем еще раз все из БД
#Добавить проверку на существование

conn = Transactions();

print(conn.insertingTransaction(g_sum_in, g_sum_out, g_comment, g_category))


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

print(conn.deleteTransaction(21))




