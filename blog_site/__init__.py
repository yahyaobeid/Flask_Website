from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
from flask_login import LoginManager

app = Flask(__name__)



########
#DataBase Setup#
########

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.joing(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

####
#Login Configurations
####

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


from blog_site.core.views import core
from blog_site.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)