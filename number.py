from flask import Flask, request
app = Flask(__name__)


@app.route("/<int:number>")
def add(number):
    return "number %s" % (number + 1)

if __name__ == "__main__":
    app.run()
