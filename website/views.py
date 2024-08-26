from flask import Blueprint, render_template, redirect, url_for, flash

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")


@views.route("/about")
def about():
    return render_template('about.html')