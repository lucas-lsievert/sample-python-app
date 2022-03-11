#!/usr/bin/python
from flask import Flaks
app = Flask(__name__)

@app.route("/")
def home():
  return "Hello from python"
