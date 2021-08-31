from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

#db variable initialization


db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    #Import a module/component using its blueprint handler variable
    from myapp.student_details.views import mod as student_module

    #Register blueprint(s)
    app.register_blueprint(student_module)
    return app