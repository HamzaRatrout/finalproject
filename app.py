from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
# app.secret_key = urandom(24)




@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/home')
def homepage():
	return render_template('home.html')
@app.route('/students')
def page1():
	return render_template('students.html')

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











