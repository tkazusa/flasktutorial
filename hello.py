from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' 


@app.route('/hoge', methods=['POST'])
def Hoge():
    return 'Hoge'


@app.route('/hoge', methods=['GET'])
def hoge():
    return 'hoge'


