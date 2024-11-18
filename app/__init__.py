import os
from flask import Flask

def create_app():
    
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../templates"))
    app = Flask(__name__, template_folder=template_dir)

    
    from .routes import app_routes
    app.register_blueprint(app_routes)
    return app

