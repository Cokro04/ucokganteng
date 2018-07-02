from flask import Flask, jsonify, abort, request
# from flask_mysqldb import MySQL
# import pymysql

# db = pymysql.connect("localhost", "root", "", "ws")
# dbb = pymysql.connect("localhost", "root", "", "affiliasicitedby")


app = Flask(__name__)
app.config["DEBUG"] = True
# mysql = MySQL(app)
empDB=[
 {
 'id':'1',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'2',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]


@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})

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

@app.route('/ip', methods=['GET'])
def haiii():
    return "wakwakkk"

@app.route('/andi/', methods=['PATCH'])
def aslam():
    return "data akan muncul di sini"    

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

@app.route('/welcome')
def api_hello():
    if 'name' in request.args:
        return 'welcome ' + request.args['name']
    else:
        return 'welcome in my world ' 

        