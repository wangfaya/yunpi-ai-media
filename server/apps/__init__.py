# coding: utf-8

from flask import Flask
from flask_cors import CORS
from flask_session import Session
import settings.config
from settings.config import STATIC_URL_PATH, STATIC_FOLDER, TEMPLATE_FOLDER

from server.apps.urls import *

__all__ = ['create_app']


def init_session(app):
    sess = Session()
    sess.init_app(app)


def init_cors(app):
    CORS(app)


def init_urls(app):
    register_urls(app)


def create_app():
    app = Flask(__name__, static_url_path=STATIC_URL_PATH, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
    app.config.from_object(settings.config)
    init_session(app)
    init_cors(app)
    init_urls(app)

    return app
