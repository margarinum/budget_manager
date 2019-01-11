from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify
from back.DBManagement import DBManagement;

db_connect = create_engine('sqlite:///db.db')
app = Flask(__name__)
api = Api(app)

class DictCategory(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from main.dict_category");
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(DictCategory, '/dictCategory') # Route_1
if __name__ == '__main__':
    app.run(port=5002)
