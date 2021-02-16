from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content="Testing")

@app.route('/blogs')
def getblog():
    return render_template("first-post.html", content="Testing")

if __name__ == "__main__":
    app.run(debug=True)