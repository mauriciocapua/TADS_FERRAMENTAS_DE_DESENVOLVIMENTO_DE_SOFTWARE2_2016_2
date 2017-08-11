import os

from flask import *
from werkzeug.utils import secure_filename
from flask_sqlalchemy import *

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import *
from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__,
            static_folder='modulo1/static')

limiter = Limiter(
    app,
    key_func=get_remote_address,
    global_limits=["200 per day", "50 per hour"]
)
admin = Admin(app, name='GOOGLE KEEP POBRE EDITION', template_mode='bootstrap3')

UPLOAD_FOLDER = 'modulo1/static/imagens/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = True
