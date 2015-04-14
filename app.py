from flask import Flask, redirect, abort
from core import get_parsed
app = Flask(__name__) 

@app.route("/problem/<id>")
def problem(id):
	r = get_parsed(id)
	if r is None:
		abort(404)
	else:
		return r

@app.route('/')
def index():
	return redirect("https://github.com/geekpradd/Sphere-Online-Judge-Sublime")


if __name__ == "__main__":
	app.run(debug=True, port=5000)