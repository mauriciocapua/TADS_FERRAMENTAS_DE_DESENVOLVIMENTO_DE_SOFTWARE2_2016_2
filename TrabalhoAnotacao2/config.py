import os
from flask import *
from werkzeug.utils import secure_filename
from flask_sqlalchemy import *

from sqlalchemy import *

app = Flask(__name__,
            static_folder='modulo1/static')

UPLOAD_FOLDER = 'modulo1/static/imagens/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.debug = True
