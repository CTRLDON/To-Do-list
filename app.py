import flask
import socket

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    app.run(ip_address,5050,debug=True)