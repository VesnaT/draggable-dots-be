from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello Draggable Dots"


@app.route("/data", methods=["GET"])
def get_data():
    return [{"id": i, "color": "#673ab7"} for i in range(4)]


if __name__ == "__main__":
    app.run()
