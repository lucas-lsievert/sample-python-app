#!/usr/bin/python
from flask import Flaks
app = Flask(__name__)

@app.route("/")
def home():
  return "Hello from python"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
