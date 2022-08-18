import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_moment import Moment


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysegcret'

########################   ####################

        # SQL DATABASE AND MODELS

##########################################
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/c"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://shabzy:1111@localhost:5432/flask_app"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://bgegmxlfdcscvg:d29bda716019e219967d4d9649eb7b71d07455ae1ded33113d3e1f488c73143e@ec2-44-205-112-253.compute-1.amazonaws.com:5432/df6e6097isv9hp"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

bcrypt = Bcrypt(app)

moment = Moment(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '37856c83ca7adc'
# app.config['MAIL_PASSWORD'] = 'bcaae18b457ba8'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['TESTING'] = False
app.config['MAIL_USERNAME'] = 'shabzynana@gmail.com'
app.config['MAIL_PASSWORD'] = 'mgtlzuarolxwtuhk'


mail = Mail(app)


from todo_app.core.views import core
from todo_app.users.views import users
from todo_app.todo.views import todos


# from shabzyblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(todos)


# app.register_blueprint(error_pages)
