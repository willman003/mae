import os

from mae_webapp import db, migrate, create_app
from webapp.blog.models import User, Post

env = os.environ.get('WEBAPP_ENV','dev')
app = create_app('config.%sConfig'%env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User = User, Post= Post, migrate = migrate)