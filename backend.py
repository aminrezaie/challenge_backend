from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=True)

client = MongoClient('localhost',
                     username='admin',
                     password='@aA12345678')

db = client.admin


@app.route('/add', methods=['POST'])
@cross_origin(supports_credentials=True)
def add():
    inserted = db.magnetics.insert_one(
        {"lat": request.json['lat'], "lng": request.json['lng'], "value": request.json['value'],
         "timestamp": datetime.now()})
    return str(inserted.inserted_id)


@app.route('/getAll')
@cross_origin(supports_credentials=True)
def get_all():
    collection = db['magnetics']
    cursor = collection.find({})
    list_cur = list(cursor)
    return dumps(list_cur);


@app.route('/health')
@cross_origin(supports_credentials=True)
def health_check():
    return 'Im OK, Thanks';


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
