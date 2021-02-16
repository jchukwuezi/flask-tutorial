"""
An example of message flashing with a form
"""

from flask import Flask,redirect,url_for,render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
#setting secret key for session
app.secret_key = "jchukwuezi"

#storing permanent session data
app.permanent_session_lifetime = timedelta(seconds=90)


# I want user to enter their email address and full name
@app.route("/", methods=["GET","POST"])
def form():
    if request.method == "POST": #method will be post if something is entered
        name = request.form["name"]
        session["name"] = name
        flash("Thank you, " + name + " we have recieved your details")
    else:
        flash("Enter a username to login")
        return render_template("form.html")






if __name__ == "__main__":
    app.run(debug=True)
     

