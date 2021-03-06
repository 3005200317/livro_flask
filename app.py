# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config import

from config import app_config, app_active

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route("/")
    def index():
        return "Hello julia!"

    @app.route("/login/")
    def login():
        return "Aqui entrará a tela de login"

    @app.route("/recovery-password/")
    def recovery_password():
        return "Aqui entrará a tela de recuperar senha"

    return app

