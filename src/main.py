import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.core.blacklist import blacklist

from src.models import init_app_models

from src.routes import auth_bp

ORIGIN = os.getenv('ORIGIN', 'http://localhost:5173')
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está definido en el entorno")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no está definido en el entorno")

print("DATABASE_URL:", DATABASE_URL)  # debug
print("SECRET_KEY:", SECRET_KEY)  # debug

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in blacklist

CORS(app,
     resources={r"/api/*": {"origins": ORIGIN}},
     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
     allow_headers=['Content-Type', 'Authorization'],
     supports_credentials=True)

init_app_models(app)

# Registrar blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
