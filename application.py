import os
import io
import requests
import time
import random

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, Response
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.jinja_env.filters["usd"] = usd
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///recipes.db")


@app.route("/")
@login_required
def home():
    return render_template("home.html", alert="")


@app.route("/viewpost", methods=["GET", "POST"])
@login_required
def viewpost():
    if request.method == "POST":

        form = request.form.get("form")

        if form == "random":
            meal = request.form.get("meal")
            recipes = db.execute(f"SELECT * FROM recipes WHERE meal = '{meal}';")
            chosen = random.choice(recipes)

        else:
            code = request.form.get("code")
            returned = db.execute(f"SELECT * FROM recipes WHERE url = '{code}'")

            if returned == []:
                return apology("Please enter a valid code")

            chosen = returned[0]

        chosen["meal"] = chosen["meal"][0].upper() + chosen["meal"][1::]
        chosen["text"] = chosen["text"].split("<br>")
        chosen["introduction"] = chosen["introduction"].split("<br>")

        url = chosen["url"]
        reviews = db.execute(f"SELECT * FROM reviews WHERE recipe_code = '{url}';")

        if reviews == []:
            rating = "N/A"
            color = "black"

        else:
            scores = []

            for review in reviews:
                score = review["stars"]
                scores.append(score)

            rating = round(sum(scores)/len(scores), 1)

            if rating > 8:
                color = "green"
            elif rating > 4:
                color = "yellow"
            else:
                color = "red"


        return render_template("viewpost.html", recipe=chosen, rating=rating, color=color)

    else:
        return redirect("/")


@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    if request.method == "POST":

        term = request.form.get("term")

        if not term:
            return apology("Missing search phrase")

        recipes = db.execute(f"SELECT * FROM recipes WHERE title LIKE '%{term}%' OR text LIKE '%{term}%'")

        for i in range(len(recipes)):
            recipe = recipes[i]
            recipe["introduction"] = recipe["introduction"].split("<br>")
            recipes[i] = recipe

        return render_template("search_results.html", recipes=recipes, query=term)

    else:
        return render_template("search.html")


@app.route("/post", methods=["GET", "POST"])
@login_required
def post():

    if request.method == "POST":

        title = request.form.get("title")
        introduction = request.form.get("introduction")
        recipe = request.form.get("recipe")
        imageURL = str(request.form.get("image"))
        meal = request.form.get("meal")

        if not title:
            return apology("Missing title")
        elif not recipe or not introduction:
            return apology("Missing introduction or recipe")
        elif not imageURL:
            return apology("Missing image URL")

        user = session['user_id']

        characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        url = ""

        for i in range(10):
            url += characters[random.randint(0, len(characters) - 1)]

        while (db.execute(f"SELECT * FROM recipes WHERE url = '{url}';")) != []:
            url = ""

            for i in range(10):
                url += characters[random.randint(0, len(characters) - 1)]

        introduction = introduction.replace("\n", "<br>")
        recipe = recipe.replace("\n", "<br>")

        username = db.execute(f"SELECT * FROM users WHERE id = {user};")[0]["username"]

        db.execute(f"INSERT INTO recipes (id, username, title, text, url, image, meal, introduction) VALUES ({user}, '{username}', '{title}', '{recipe}', '{url}', '{imageURL}', '{meal}', '{introduction}');")
        return render_template("home.html", alert=f"post {url} successfully submitted")
    else:
        return render_template("post.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("All fields must be filled in")

        if password != confirmation:
            return apology("Password and confirmation do not match")

        existing = db.execute(f"SELECT * FROM users WHERE username = '{username}';")

        if existing != []:
            return apology("An account with this username already exists")

        passwordhash = generate_password_hash(password)
        db.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{passwordhash}');")
        user_id = db.execute(f"SELECT * FROM users WHERE username = '{username}';")[0]["id"]

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/review", methods=["GET", "POST"])
@login_required
def review():
    if request.method == "POST":
        rating = request.form.get("rating")
        code = request.form.get("code")
        user = session["user_id"]

        returned = db.execute(f"SELECT * FROM reviews WHERE user_id = '{user}' AND recipe_code = '{code}';")

        if returned == []:
            db.execute(f"INSERT INTO reviews (user_id, recipe_code, stars) VALUES ('{user}', '{code}', '{rating}');")
        else:
            db.execute(f"UPDATE reviews SET stars = '{rating}' WHERE user_id = '{user}' AND recipe_code = '{code}';")

        return render_template("home.html", alert=f"rating for recipe {code} successfully added")

    else:
        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return apology("Please enter a valid username and password")

        rows = db.execute(f"SELECT * FROM users WHERE username = '{username}'")

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], password):
            return apology("Invalid username and/or password")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)