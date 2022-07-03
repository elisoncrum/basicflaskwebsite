import os
from flask import Flask
import requests
from app import config
from sqlmodel import SQLModel
from sqlmodel import create_engine

APP_SETTINGS = os.getenv("APP_SETTINGS", "Testing")

def drop_database(config):
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy import MetaData
    from sqlalchemy import inspect
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base

    engine = create_engine(config["DATABASE_URI"])
    meta = MetaData()
    meta.reflect(bind=engine)
    meta.drop_all(engine, checkfirst=False)

def create_app():
    app = Flask(__name__, template_folder="app/templates/", static_folder="app/static/")
    app.count_requests = 0

    app.config.from_object(f"app.config.{APP_SETTINGS}")
    app.secret_key = os.urandom(256)
    app.url_map.strict_slashes = False

    return app

app = create_app()
with app.app_context():
    from app.database import engine

    app.engine = engine

if os.getenv("DROP_DATABASE", False):
    drop_database(app.config)

SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))