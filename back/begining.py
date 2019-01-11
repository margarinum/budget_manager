# coding=utf-8
from back.Transactions import *
#import window
import os
from PyQt5 import QtWidgets
import back.main

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


transactions = Transactions();

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
#print(transactions.insertingTransaction(g_sum_in, g_sum_out, g_comment, g_category))
#print(transactions.deleteTransaction(24))
#categories = Categories();
#print(categories.insertCategory("Какая-то категория еще"));
#print(transactions.insertingTransaction(g_sum_in, g_sum_out, g_comment, 3))
#print(categories.deleteCategory(3))




