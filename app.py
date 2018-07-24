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

    table= db['profiles']
	table.insert(dict(firstName=firstName ,lastName=lastName,password=password))
	return render_template('data.html', messages= list (table.all()))
# TODO: route to /register
# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











