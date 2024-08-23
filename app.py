import flask
from flask_sqlalchemy import SQLAlchemy
import socket
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,"database.db")}"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    task = db.Column(db.String(200), nullable =False)
    status = db.Column(db.String(100) , nullable =False)

    def __repr__(self):
        return '<Task %r>' % self.task


@app.route('/')
def index():
    return flask.render_template("index.html")




if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    app.run(ip_address,5050,debug=True)