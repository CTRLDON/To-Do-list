# Importing Libraries | 
import flask #Flask Framework
from flask_sqlalchemy import SQLAlchemy # Python(JS input) -> SQL
import socket # Local IP
import os # Path configuration
from flask import request

#functions
def Flask_creation_process():
    """Flask init proces, no inputs.
    Outputs: Flask object"""
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,"database.db")}"
    global db
    db = SQLAlchemy(app)
    return app

#intializing Flask server
Flask_object = Flask_creation_process()

#routes
@Flask_object.route('/') # First thing to opened
def index():
    return flask.render_template("index.html")
# - - - - - - - - - - - - - 
@Flask_object.route('/addtask' , methods=['POST','GET'])
def addTask():
    if request.method == 'POST':
        data = request.form.get('info')
        print(data)
        return flask.redirect('/')

if __name__ == '__main__':
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        Flask_object.run(ip_address,5050,debug=True)