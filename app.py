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
@app.route('/map')
def page2():
    return render_template('map.html')
@app.route('/y2b')
def page3():
    return render_template('y2b.html')
@app.route("/signin", methods=['POST', 'GET'])
def login_page1():
    accounts=db["accounts"]
    username=request.form['userName']
    password=request.form['password']
    user = accounts.find_one(userName=username,password=password)
    if user:
        session['loggedIn']=True
        return render_template("home.html")
    else :
        return render_template("login.html",error="The password or username is incorrect")

@app.route('/ins')
def wtvr():
    return render_template('instructors.html')
@app.route('/wait')
def wtv2r():
    return render_template('sorry.html')

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











