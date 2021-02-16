"""
This file is an example of passing a parameter in an end point
"""
from flask import Flask, redirect, url_for, render_template

#instantiating class
app = Flask(__name__)

#the url end point for particular thing in the app
@app.route('/<name>')
def user(name):
    #returning html directly to the browser
    return '<h1>Hello {}</h1>'.format(name)

#app.route has a function that it will go to depending on the page
"""
@app.route("/")
def home():
    return "Hello this is the home page <h1>Hello<h1>"
"""

@app.route("/admin")
def admin():
    #using redirect and url_for to redirect to the function
    #return redirect(url_for("home"))

    #using redirect + url_for to redirect to function that requires parameter
    return redirect(url_for("user", name="Admin!"))

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
