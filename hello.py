#!/usr/bin/python3

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<div style="text-align:center"><form action="/greetings">Name: <input type="text" name="user"></div>'

@app.route('/greetings/<username>')
def hello_username(username):
	to_return = ""
	names = username.split(",")
	for name in names:
		to_return = to_return + "Hello, " + name + ".\n"
	return "<pre>" + to_return + "</pre>"

@app.route('/greetings')
def Greeting_Page():
	user = request.args.get("user")
	return "Hello, " + user
