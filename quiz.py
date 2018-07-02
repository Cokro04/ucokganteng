from flask import Flask, jsonify, abort
from flask_mysqldb import MySQL
import pymysql

db = pymysql.connect("localhost", "root", "", "ws")
dbb = pymysql.connect("localhost", "root", "", "affiliasicitedby")


app = Flask(__name__)
mysql = MySQL(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/ron', methods=['DELETE'])
def cobain():
   cursor = db.cursor()
   sql = "SELECT * FROM quiz WHERE id=2"
   cursor.execute(sql)
   results = cursor.fetchall()
   return str(results)

@app.route('/hello', methods=['VIEW'])
def hello():
    return "Hello World"

@app.route('/aff', methods=['GET'])
def bisa():
  cursor = dbb.cursor()
  sql = "SELECT * FROM searchpost"
  cursor.execute(sql)
  results = cursor.fetchall()
  return str(results)
    
if __name__ == '__main__':
    app.run(debug=True)