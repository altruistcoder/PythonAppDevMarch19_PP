from flask import Flask, render_template, request
from datetime import datetime
from bson import json_util
import random

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("home.html")


@app.route("/form", methods=['GET', 'POST'])
def submit_data():
	if request.method == 'GET':
		return render_template("form.html")
	else:
		text_data = request.form.get('text-data').split()
		random.shuffle(text_data)
		r = " ".join(text_data)
		return json_util.dumps(r)


if __name__ == "__main__":
	app.run(port=8000, use_reloader=True, debug=True)
