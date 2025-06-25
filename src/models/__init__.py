from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa modelos principales
from .company import Company
from .user import User

# Función opcional para futuras expansiones o uso en factory
def init_app_models(app):
    db.init_app(app)
