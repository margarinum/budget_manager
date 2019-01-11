from back.DBManagement import *
import sqlite3

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

    def insertCategory(self, p_category_name):
        conn = DBManagement.connectToSQLite(self);
        curs = conn.cursor();
        try:
            sql_text = r'''insert into dict_category(nm_category) values ('{}')'''.format(p_category_name)
            # curs.execute(pref + "('3', '+', '18/02/2018 14:26:31', 'comment', 'category')")
            curs.execute(sql_text)

            conn.commit()
            res = 'Категория добавлена!'
        except sqlite3.IntegrityError:
            res = r'''Категория '{}' уже существует.'''.format(p_category_name)
        except:
            res = 'Ошибка вставки в БД'
        finally:
            conn.commit()
            conn.close()
            return res

    def deleteCategory(self,p_id_category):
        conn = DBManagement.connectToSQLite(self)
        curs = conn.cursor()
        try:
            sql_text = '''delete from dict_category where id_category = %s'''
            curs.execute(sql_text % p_id_category);
            conn.commit();
            if conn.total_changes == 0:
                res = 'Категории не существует!'
            elif conn.total_changes == 1:
                res = 'Категория удалена'
            else:
                res = 'Что-то пошло не так...';
            conn.commit()

        except sqlite3.IntegrityError:
            res = 'Невозможно удалить транзакцию, так как к ней привязаны транзакции'
        finally:
            conn.rollback()
            conn.close()
            return res;

