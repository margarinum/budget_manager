from back.DBManagement import *
from back.Categories import *
import sqlite3
import datetime


class Transactions():
    def insertingTransaction(self, p_sum_in, p_sum_out, p_comment, p_category):
        # Выполним забор категорий
        conn = DBManagement.connectToSQLite(self)
        curs = conn.cursor()
        dict_categories = Categories.extractCategories(self)
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

    def deleteTransaction(self, p_id_transaction):

        conn = DBManagement.connectToSQLite(DBManagement)
        curs = conn.cursor()
        try:
            sql_text = '''delete from bm_transaction where transaction_id = %s'''
            curs.execute(sql_text % p_id_transaction);
            conn.commit();
            if conn.total_changes == 0:
                res = 'Ошибка! Транзакиция не удалена'
            elif conn.total_changes == 1:
                res = 'Транзакция удалена'
            else:
                res = 'Что-то пошло не так...';
            conn.rollback();
            conn.close();
        except sqlite3.IntegrityError:
            res = 'Невозможно удалить транзакцию'
        finally:

            return res;
