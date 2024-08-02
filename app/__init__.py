from flask import Flask
from routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    return app
