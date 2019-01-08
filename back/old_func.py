# coding=utf-8
#Файл с устаревшим кодом, который, возможно, понадобится


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