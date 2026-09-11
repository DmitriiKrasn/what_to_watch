from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты модулей приложения — САМЫМИ ПОСЛЕДНИМИ!
from . import views, models  # noqa: E402, F401
from . import error_handlers, cli_commands  # noqa: E402, F401
