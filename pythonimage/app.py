from flask import Flask
from redis import Redis


import os


app = Flask(__name__)


@app.route('/')
def hello():
 return 'Welcome to Java Home App '

if __name__ == "__main__":
 app.run(host="0.0.0.0", debug=True, port=80)
