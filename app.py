import flask #Flask Framework
from flask_sqlalchemy import SQLAlchemy # Python(JS input) -> SQL
import socket # Local IP
import os # Path configuration
from flask import request

basedir = os.path.abspath(os.path.dirname(__file__)) # importaing main files Directory
#init Flask Object: app
app = flask.Flask(__name__)
# confiuring flask to have database path 
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,"database.db")}"
# SQL object database called (db)
db = SQLAlchemy(app)

class Task(db): #try to use db.Model
    
    '''input: data base model -> obj type: SQLAlchemy object
    output: Task object'''

    id = db.Column(db.Integer , primary_key=True)
    task = db.Column(db.String(200), nullable =False)
    status = db.Column(db.String(100) , nullable =False)

    def __repr__(self):
        return '<Task %r>' % self.task


@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/addtask' , methods=['POST','GET'])
def addTask():
    if request.method == 'POST':
        data = request.form.get('info')
        print(data)
        return flask.redirect('/')


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    app.run(ip_address,port=5050,debug=True)