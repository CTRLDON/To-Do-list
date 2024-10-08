# Importing Libraries | 
import flask #Flask Framework
from flask_sqlalchemy import SQLAlchemy # Python(JS input) -> SQL
import socket # Local IP
import os # Path configuration
from flask import request   
import sqlite3

#functions
def Flask_creation_process():
    """Flask init proces, no inputs.
    Outputs: Flask object"""
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,"database.db")}"
    global db
    db = sqlite3.connect("database.db")
    cr = db.cursor()
    query = """
            CREATE TABLE IF NOT EXISTS todos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                status TEXT
            )
            """
    cr.execute(query)
    db.commit()
    cr.close()
    db.close()
    return app

def connect_to_database(database_name):
     db = sqlite3.connect(database_name)
     cr = db.cursor()
     return (db,cr)
#intializing Flask server
Flask_object = Flask_creation_process()

#routes
@Flask_object.route('/') # First thing to opened
def index():
    db,cr = connect_to_database("database.db")
    cr.execute("SELECT * from todos")
    data = cr.fetchall()
    tasks = [task[1] for task in data]    
    print(tasks)

    return flask.render_template("index.html" , tasks=tasks)
# - - - - - - - - - - - - - 
@Flask_object.route('/addtask' , methods=['POST'])
def addTask():
    db,cr = connect_to_database("database.db") # connecting to the database and retrieving db and cursor
    if request.method == 'POST': # checking if the method is POST
        data = request.get_json() # getting the json data sent by Ajax api request
        cr.execute("INSERT into todos(task,status) values(?,?)", (data['info'] , "unfinished")) # inserting the retrieved data into the todo table
        db.commit() # saving the changes in the database
        cr.close() # closing the cursor
        db.close() # closing the database
    return flask.redirect('/') # returning to the homepage
# - - - - - - - - - - - - -
@Flask_object.route('/deletetask',methods=['POST'])
def deleteTask():
    db,cr = connect_to_database("database.db")
    if request.method == 'POST':
          print('something')
          data = request.get_json()
          cr.execute("DELETE FROM todos where id = ?" , (data['info'],))
          db.commit()
          cr.close()
          db.close()
    return flask.redirect('/')
# - - - - - - - - - - - - - 
if __name__ == '__main__':
        hostname = socket.gethostname() # getting the hostname to get the ip address
        ip_address = socket.gethostbyname(hostname) # getting the ip address through the host name
        Flask_object.run(ip_address,5050,debug=True) # running the server