import os

from flask import Flask
 
from flask_login import LoginManager
 
from flask_sqlalchemy import SQLAlchemy
 

 
app = application = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'haccdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'
db_uri = 'sqlite:////run/media/wam/aer/flask3.6/env/medical/app/test.db'
#db_uri = 'postgresql://wam:hii@127.0.0.1:5432/medical'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config['DEBUG'] = True
 
 

from app.models.user import User

 
 
 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "auth.login"

# Configure the image uploading via Flask-Uploads
#images = UploadSet('images', IMAGES)
#onfigure_uploads(app, images)

 

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
 



# Set up extensions

db.init_app(app)
 

# Register Jinja template functions
 

# Create app blueprints
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .doctor import doctor as doctor_blueprint
app.register_blueprint(doctor_blueprint, url_prefix='/doctor')


 
from .account import auth as account_blueprint
app.register_blueprint(account_blueprint, url_prefix='/account')

from app.profile.views import patient as patient_blueprint
app.register_blueprint(patient_blueprint, url_prefix='/profile')

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')


 
 
