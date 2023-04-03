from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from personal_site.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from personal_site import routes
