"""
This file is an example of a post method in flask
"""
from flask import Flask,redirect,url_for,render_template, request

app = Flask(__name__)

#@app.route is known as a decorator

#by default when you go to this end point it will call these methods
@app.route('/post', methods=["POST", "GET"])
def post():
    #I want to get the name answered in the name bar and send it to the user page
    if request.method == "POST": #checking the request type
        user = request.form["nm"]  
        #it is redirecting to username and also mapping the value entered in form
        return redirect(url_for("user", usr=user))
    else:
        return render_template("postname.html")

@app.route("/<usr>")
def user(usr):
    return "<h1>{}</h1>".format(usr)

    """
    you can also write it like this:
    return f"<h1>{usr}</h1>"
    """

if __name__ == "__main__":
    app.run(debug=True)
     



