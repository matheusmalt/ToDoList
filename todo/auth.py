from flask import Blueprint, render_template, request, url_for, redirect, flash
from .models import User
from todo import db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/registrar", methods = ("POST", "GET"))
def registrar():
    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["senha"]

        user = User(username, password)
        error = None
        user_name = User.query.filter_by(username = username).first()

        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        
    return render_template("auth/registrar.html")