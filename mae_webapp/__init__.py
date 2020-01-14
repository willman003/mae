from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app(object_name):
    from webapp.blog import blog_blueprint
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)
    from mae_webapp.main import *
    app.register_blueprint(blog_blueprint)
    return app