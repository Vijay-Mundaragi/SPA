from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from forms import StudentForm
from config import Config
import connexion

conn_app = connexion.FlaskApp(__name__, specification_dir='./')

app = conn_app.app
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


conn_app.add_api('swagger.yml')


