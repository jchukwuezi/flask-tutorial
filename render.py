"""
This file is an example of passing information from backend in flask to frontend in HTML
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    #this function is returning the rendered html file
    return render_template("index.html", content=name, r=2)

#this end point will call fn to set elements in list content
@app.route("/")
def show_list():
    return render_template("index.html", content= ["joe", "bill", "tom"])

if __name__ == "__main__":
    app.run(debug=True)

    