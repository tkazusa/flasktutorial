from flask import Flask, render_template
app = Flask(__name__)


@app.route('/title/<title>')
def title(title):
    return render_template('index.html', title=title)

@app.route('/hoge', methods=['POST'])
def Hoge():
    return 'Hoge'


@app.route('/hoge', methods=['GET'])
def hoge():
    return 'hoge'


