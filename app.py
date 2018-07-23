from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
app.secret_key = urandom(24)

# TODO: set up database
# db = dataset.connect(“<database>”)


@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











