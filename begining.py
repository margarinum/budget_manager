# coding=utf-8

import time

# Данная программа представляет из себя жалкие попытки вспомнить питон
"""

Для начала суть:
Планируется программа, в которой будет фронт и бэк энды.
Начинать будем с бэкэнда

"""

#Глобальные переменные
list_func = []
list_out = []

#Объявим и присвоим тестовые значения
#Тест
g_sum_ent = 3
g_operation = '+'
g_comment = 'comment'
g_category = 'somecategoryыщьу'

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
    return 'Операция добавлена'

#Вызов функции вставки в файл
#inserting_into_file(g_sum_ent, g_operation, g_category, g_comment)

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

a = create_category(g_category)
print(a)