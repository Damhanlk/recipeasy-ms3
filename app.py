import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Routing 

@app.route("/")
def home():
    """
    This method loads the recipes in MongoDB into a list
    for pagination and display on he index page
    """
    per_page = 6

    page = request.args.get(get_page_parameter(), type=int, default=1)

    games = list(mongo.db.recipes.find())

    pagination = Pagination(page=page, per_page=per_page, total=len(games))

    return render_template("homepage.html",
                           recipes=display_recipes(recipes, page, per_page),
                           pagination=pagination,
                           username=get_user(),
                           acc_type=get_acc_type())


# Log In function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
       
        if existing_user:
            # Check if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Password is invalid
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Remove session to log user out
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    session.pop("acc_type")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Checks if passwords match
        if request.form.get(
             'password') != request.form.get('password-confirm'):
            # If passwords don't match, flash the message below to the user and return to form
            flash("Passwords do not match")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Profile Page function to display recipes submitted by user 

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Adapted Code from the Flask task project
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    users = list(mongo.db.users.find())

    if session["user"] and get_acc_type() == "user":
        recipes = list(mongo.db.reviews.find({"created_by": username}))
        return render_template("profile.html",
                               username=username,
                               recipes=recipes)
    else:
        return redirect(url_for("login"))
