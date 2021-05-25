from flask import Flask ,render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio = SocketIO(app)


@app.route("/",methods=["GET","POST"])
def receiver ():
    return render_template("index.html")

@app.route("/send",methods=["GET","POST"])
def sender ():
    return render_template("send.html")

#receiving
@socketio.on('connect')
def connected():
    print('connect')

#sending
@socketio.on('message')
def message(json, methods=['GET']):
    #print(json)
    socketio.emit('message_response', json)


if __name__ =="__main__":
    socketio.run(app)