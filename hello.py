from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=['POST'])
def webhook():
    print(request.header)
    print("body: %s" % request.data)
    return request.data


if __name__ == "__main__":
    app.run()
