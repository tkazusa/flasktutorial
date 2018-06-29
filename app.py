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
    return render_template('error.html')


@app.route('/upload', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    return render_template('result.html', name=request.form['name'])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
