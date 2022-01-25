from flask import Flask
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

app = Flask(__name__)

cloud_config = {
        'secure_connect_bundle': r'C:\Users\Gabriel\Downloads\secure-connect-crud-todo.zip'
    }
auth_provider = PlainTextAuthProvider('IXGTAjWCXmWaUXduzQWPhrOK',
                                          'ql8raKsiRhQc0M3HlmF_oP1gPhUJg_JYk38Ren1n154q3A,q018+ZKXv,iQY3zr6+NP.7qI5jQSeOGlcihWSE,fnwW7FUaMi4smJgsF,wwpuAoZi+0mu0tFPlGBr,2.a')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('todo')

@app.route('/', methods=['GET'])
def cassandra():
    row = session.execute("select release_version from system.local").one()
    if row:
        return f'{row[0]}'
    else:
        print("An error occurred.")\


@app.route('/create-todo-table', methods=['GET'])
def createTable():
    row = session.execute("CREATE TABLE todo_list (id int primary key, owner int, name varchar, isDone boolean)")
    if row:
        return f'{row[0]}'
    else:
        print("An error occurred.")\


@app.route('/record-todo', methods=['GET'])
def recordTodo():
    row = session.execute("insert into todo.todo_list (id, owner, name, isdone) values (2, 55, 'Learn cassandra with flask', false);")
    if row:
        return f'{row[0]}'
    else:
        print("An error occurred.")\


@app.route('/delete-todo', methods=['GET'])
def deleteTodo():
    row = session.execute("delete from todo.todo_list where id = 1;")
    if row:
        return f'{row[0]}'
    else:
        print("An error occurred.")


@app.route('/update-todo', methods=['GET'])
def updateTodo():
    row = session.execute("update todo.todo_list set isdone = false where id = 2;")
    if row:
        return f'{row[0]}'
    else:
        print("An error occurred.")


