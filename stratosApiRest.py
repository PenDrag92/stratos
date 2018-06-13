import os, time, sqlite3
from datetime import datetime
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def get_tasks():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
