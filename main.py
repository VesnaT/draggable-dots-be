from flask import Flask, request
from flask_cors import CORS

from db import save_data, read_data

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello Draggable Dots"


@app.route("/data", methods=["GET"])
def get_data():
    return read_data()


@app.route("/data", methods=["POST"])
def set_data():
    data = request.get_json(force=True)
    save_data(data)
    return data


if __name__ == "__main__":
    app.run()
