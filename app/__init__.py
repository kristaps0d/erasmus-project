from django.shortcuts import render
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/wrecks")
def wrecks():
	return render_template("wrecks.html")

@app.route("/staircase")
def staircase():
	return render_template("staircase.html")

@app.errorhandler(404)
def not_found(e):
	return "<script>window.location.href = '/'</script>"