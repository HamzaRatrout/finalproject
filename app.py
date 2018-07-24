from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
db_url=os.environ['DATABASE_URL']
# db_url="postgres://wpkfjzkaxiispe:cd075d5678edfd916b08a0e2d0bf7a264e94ef30eac671eb91ff1399383b0c2b@ec2-54-204-23-228.compute-1.amazonaws.com:5432/d30vhtaaeu1lnr"
db = dataset.connect(db_url)
app.secret_key = os.urandom(24)


show_data=False


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
		return render_template('login.html',error="you must be logged in to see the webpage")
# @app.route("/<page_name>/")
# def load_generic_page(page_name):
# 	return render_template(page_name + ".html",title=page_name)


@app.route("/students")
@app.route("/students/")
def page_students():
	return render_template('students.html')

@app.route("/map")
@app.route("/map/")
def page2():
	return render_template('map.html')



@app.route("/data")
def data():
	if show_data==True :
		return render_template('data.html', accounts=db["accounts"] ,show_data=show_data)
	else:
		return render_template('home.html')
@app.route("/login", methods=['POST', 'GET'])

@app.route('/y2b')
def page3():
	return render_template('y2b.html')
@app.route("/signin", methods=['POST', 'GET'])
def login_page1():
    accounts=db["accounts"]
    username=request.form['userName']
    password=request.form['password']
    user = accounts.find_one(userName=username,password=password)
    global show_data
    if username=="1":
    	show_data = True
    else:
    	show_data =False 
    if user:
        session['loggedIn']=True
        return redirect("/home")
    else:
        return render_template("login.html",error="The password or username is incorrect")

@app.route("/register1")
def register1():
	return render_template('register1.html')
# TODO: route to /register
@app.route("/newAccount",methods=['POST', 'GET'])
def register():
	accounts=db["accounts"]
	potential_username=request.form['userName']
	potential_password=request.form['password']
	username_exists=accounts.find_one(userName=potential_username)
	if username_exists:
		return render_template("register1.html", error="username is already taken")
	else :
		accounts.insert(dict(userName=potential_username,password=potential_password))
		return render_template("login.html")
# TODO: route to /error
@app.route("/delete")
def delete_table():
	if show_data== True :
		table= db['accounts']
		table.delete()
		return render_template('data.html')
if __name__ == "__main__":
    app.run(port=3000)











