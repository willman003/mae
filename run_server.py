import os
from mae_webapp import create_app

env = os.environ.get('WEBAPP_ENV','dev')
app = create_app('config.%sConfig' % env.capitalize())

if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST','localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.debug = True
    app.run(HOST, PORT)