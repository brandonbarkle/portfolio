import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        db.execute("INSERT INTO 'birthdays' ('name', 'month', 'day') VALUES(%s, %s, %s)", name, month, day)
        return redirect("/")

    else:
        entries = db.execute('SELECT name, month, day FROM birthdays')
        return render_template("index.html", entries=entries)


