from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome"

@app.route("/hello")
def hello():
	naam = "Nikhil"
	return render_template("test.html",
		name=naam)

if __name__ == "__main__":
	app.run(use_reloader=True)