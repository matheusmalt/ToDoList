from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = "dev",
        SQLALCHEMY_DATABASE_URI = "sqlite:///projeto.db"
    )

    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template("index.html")
    
    return app