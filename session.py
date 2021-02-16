"""
This file is an example of a session in flask
"""
from flask import Flask,redirect,url_for,render_template, request, session
from datetime import timedelta

app = Flask(__name__)
#setting secret key for session
app.secret_key = "jchukwuezi"

#storing permanent session data
app.permanent_session_lifetime = timedelta(seconds=90)


#@app.route is known as a decorator

#by default when you go to this end point it will call these methods
@app.route('/post', methods=["POST", "GET"])
def post():
    #I want to store the name answered in a session
    if request.method == "POST": #checking the request type
        user = request.form["nm"]  
        #sessions are stored in a dictionary
        session["user"] = user
        #it is redirecting to user function
        return redirect(url_for("user"))
    else:
        #checking if name has already been posted
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("postname.html")

#function is going to get the session information
@app.route("/user")
def user():
    #checking if user has entered their name
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("post"))    

#function is going to clear a session
@app.route("/logout")        
def logout():
    #pops off data from session
    session.pop("user", None)
    return redirect(url_for("post"))


if __name__ == "__main__":
    app.run(debug=True)
     
