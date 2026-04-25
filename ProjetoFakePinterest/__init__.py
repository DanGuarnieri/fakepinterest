from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# ---------------- APP ---------------- #
app = Flask(__name__, instance_relative_config=True)

app.config['SECRET_KEY'] = '123fda61553c986fae5f8ceee79c1bcd'
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

# 📁 Garante que a pasta instance existe
os.makedirs(app.instance_path, exist_ok=True)

# 🗄️ Banco dentro da instance
db_path = os.path.join(app.instance_path, "pinterestfake.db")

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# ---------------- EXTENSIONS ---------------- #
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'homepage'
login_manager.login_message = 'Faça o login para acessar a página'
login_manager.login_message_category = 'alert-info'


# ---------------- LOGIN ---------------- #
from ProjetoFakePinterest.models import Usuario

@login_manager.user_loader
def load_usuario(user_id):
    return Usuario.query.get(int(user_id))


# ---------------- IMPORTS ---------------- #
from ProjetoFakePinterest import models
from ProjetoFakePinterest import routes