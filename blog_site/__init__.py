from flask import Flask

app = Flask(__name__)


from blog_site.core.views import core
from blog_site.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)