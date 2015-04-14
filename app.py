from flask import Flask, redirect
import json
from core import get_parsed
app = Flask(__name__) 

@app.route("/problem/<id>")
def problem(id):
	return json.dumps(get_parsed(id))

@app.route('/')
def index():
    return redirect("https://github.com/geekpradd/Sphere-Online-Judge-Sublime")
