from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Hello World')


@app.route('/login', methods=['GET'])
def render_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('error.html', l=["Hoge", "Fuga", "Foo"])


@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.form['username'] and request.file['file']:
        f = request.file['file']
        filepath = 'static/' + secure_filename(f.filename)
        f.save('filepath')
        return render_template('result.html',
                               name=request.form['name'],
                               image_url=filepath)

