from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/intro")
def intro():
	name = request.args.get("name")
	funfact = request.args.get("funfact")
	if not name or not funfact:
		return render_template("intro_fail.html",name=name,funfact=funfact)
	return render_template("intro.html",name=name,funfact=funfact)