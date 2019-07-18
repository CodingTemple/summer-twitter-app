from flask import render_template,redirect
from twitterapp import app
from twitterapp.forms import SignUpForm

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def createUser():
    form = SignUpForm()
    if form.validate():
        redirect("/")
        print(form.username.data)
    else:
        print("Not valid")
        print(form.errors)
    return render_template("register.html",form=form)