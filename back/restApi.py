# coding:utf8

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from back.DBManagement import DBManagement;

db_connect = create_engine('sqlite:///DB/db.db')
app = Flask(__name__)
api = Api(app)


class getDictCategory(Resource):
    def get(self):
        # conn = db_connect.connect()
        conn = db_connect.connect()
        query = conn.execute("select id_category, nm_category from main.dict_category;")
        result = {'categories': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class getTransactions(Resource):
    def get(self):
        # conn = db_connect.connect()
        conn = db_connect.connect()
        query = conn.execute(
            "select dc.nm_category, bt.sum_in, bt.sum_out, bt.date_oper, bt.comment from bm_transaction bt join dict_category dc on bt.id_category = dc.id_category;")
        result = {'transactions': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class getBalance(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select sum(sum_in)-sum(sum_out) from main.bm_transaction bt;")
        return {'balance': [i[0] for i in query.cursor.fetchall()]} # Fetches first


api.add_resource(getDictCategory, '/getCategories')  # Route_1
api.add_resource(getTransactions, '/getTransactions')  # Route 2
api.add_resource(getBalance, '/getBalance')  # Route 1

if __name__ == '__main__':
    app.run(port=5002)
