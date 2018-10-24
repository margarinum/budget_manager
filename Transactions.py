from DBManagement import *
import psycopg2
import sqlite3
import datetime

class Transactions():
    def insertingTransaction(self, p_sum_in, p_sum_out, p_comment, p_category):
        # Выполним забор категорий
        conn = DBManagement.connectToSQLite(self)
        curs = conn.cursor()
        dict_categories = DBManagement.extractCategories(self)
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
        # Выполним забор категорий
        conn = DBManagement.connectToSQLite(self)
        curs = conn.cursor()

        #try:
        sql_text = '''select count(*) from bm_transaction where transaction_id = %s'''
        curs.execute(sql_text % p_id_transaction)
        rowCount = curs.fetchone()[0]
        if (rowCount == 1):
            sql_text = '''delete from bm_transaction where transaction_id = %s'''
            curs.execute(sql_text % p_id_transaction)
            conn.commit()
        elif (rowCount == 0):
            return "Транзакции не существует"

#            res = "Транзакция удалена!"
#        except AssertionError:
#            res = 'Ошибка вставки в БД!'
#        finally:
#            conn.rollback()

