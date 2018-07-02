from flask import Flask, jsonify, abort
# from flask_mysqldb import MySQL
# import pymysql

# db = pymysql.connect("localhost", "root", "", "ws")
# dbb = pymysql.connect("localhost", "root", "", "affiliasicitedby")


app = Flask(__name__)
app.config["DEBUG"] = True
# mysql = MySQL(app)

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



# @app.route('/ron', methods=['DELETE'])
# def cobain():
#    cursor = db.cursor()
#    sql = "SELECT * FROM quiz WHERE id=2"
#    cursor.execute(sql)
#    results = cursor.fetchall()
#    return str(results)

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

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
    
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/roza/', methods=['GET'])
def home():
    return "<h1>Saya suka beajar WEBSERVICE.</p>"

app.run()