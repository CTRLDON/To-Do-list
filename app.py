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

def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Connect to an external server to determine the IP address
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        print(f"Error: {e}")
        ip_address = 'localhost'
    finally:
        s.close()
    
    return ip_address
#intializing Flask server
Flask_object = Flask_creation_process()

#routes
@Flask_object.route('/') # First thing to opened
def index():
    db,cr = connect_to_database("database.db") # connecting to the database and retrieving the cursor
    cr.execute("SELECT task,id from todos where status=?",("unfinished",)) # selecting using the cursor all data saved in the database
    data = cr.fetchall() # fetching all the data in the database
    tasks = [task[0] for task in data]  # clearing all the data to get the task names only
    ids = [int(task[1]) for task in data]
    print(tasks)

    return flask.render_template("index.html" , tasks=tasks , ids=ids) # rendering the website with tasks paramter
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
@Flask_object.route('/deletetask',methods=['POST']) # when routed to deletetask route it will trigger deleteTask function
def deleteTask():
    db,cr = connect_to_database("database.db") # connecting to the database
    if request.method == 'POST': # checking if the method is 'POST'
          print('something')
          data = request.get_json() # getting data sent by Ajax from the website
          cr.execute("DELETE FROM todos where id = ?" , (data['info'],)) # deleting the database record based on the data sent by the client
          db.commit() # saving changes
          cr.close() # closing the cursor
          db.close() # closing the database
    return flask.redirect('/') # returning to the homepage
# - - - - - - - - - - - - -
@Flask_object.route('/donetask',methods=['POST'])
def doneTask():
    db,cr = connect_to_database("database.db")
    if request.method == 'POST':
          data = request.get_json() # getting data sent by Ajax from the website
          print(data)
          cr.execute("UPDATE todos set status = ? where id = ?" , ("finished",data['id'])) # deleting the database record based on the data sent by the client
          db.commit() # saving changes
          cr.close() # closing the cursor
          db.close() # closing the database
    return flask.redirect('/') 
# - - - - - - - - - - - - -
@Flask_object.route('/finished-tasks')
def finishedPage():
     db,cr = connect_to_database("database.db")
     cr.execute("SELECT task,id FROM todos where status = ?",("finished",))
     data = cr.fetchall()
     doneTasks = [task[0] for task in data]
     doneIds = [task[1] for task in data]
     return flask.render_template("done.html" , tasks=doneTasks,ids=doneIds)
if __name__ == '__main__':
        
        ip_address = get_ip_address() # getting the ip address through the host name
        Flask_object.run(ip_address,5050,debug=True) # running the server