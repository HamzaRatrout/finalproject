from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
db_url=os.environ['DATABASE_URL']
db = dataset.connect(db_url)
app.secret_key = os.urandom(24)





@app.route('/')
def login_page():
    return render_template('login.html')
# @app.route('/home')
# def homepage():
# 	return render_template('home.html')
@app.route ("/home")
def load_home_page ():
	if 'loggedIn' in session and  session['loggedIn']==True :

		return render_template("home.html",title="Home")
	else :
		return render_template('loginPage.html',error="you must be logged in to see the webpage")
@app.route("/<page_name>/")
def load_generic_page(page_name):
	return render_template(page_name + ".html",title=page_name)


# @app.route('/students')
# def page1():
# 	return render_template('students.html')
# @app.route('/map')
# def page2():
# 	return render_template('map.html')
@app.route("/login", methods=['POST', 'GET'])
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

    
# TODO: route to /register
@app.route("/register",methods=['POST', 'GET'])
def register():
	accounts=db["accounts"]
	potential_username=request.form['userName']
	potential_password=request.form['password']
	username_exists=accounts.find_one(userName=potential_username)
	if username_exists:
		return render_template("register.html", error="username is already taken")
	else :
		accounts.insert(dict(userName=potential_username,password=potential_password))
		return render_template("login.html")
# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











