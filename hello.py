from flask import Flask, rrender_template
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

@app.route('/search')
def search():
    q = request.args.get('q', '') 
    return 'hoge'


