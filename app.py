from flask import Flask
import json
from core import get_parsed
app = Flask(__name__) 

@app.route("/problem/<id>")
def problem(id):
	return json.dumps(get_parsed(id))

if __name__=="__main__":
	app.run(debug=True)
