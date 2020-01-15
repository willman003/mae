from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import DevConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login.login'
@login.user_loader
def load_user(user_id):
    return dbSession.query(Nguoi_dung).get(user_id)


def create_app(object_name):
    from mae_webapp.login import login_bp
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    from mae_webapp.main import *
    app.register_blueprint(login_bp)
    
    return app