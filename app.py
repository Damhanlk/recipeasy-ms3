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

