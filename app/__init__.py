from flask import Flask
from datetime import datetime
from app.routes import main  
# from .routes import main
'''El import from .routes import main solo funciona si app es tratado como un paquete Python (por ejemplo, cuando Flask ejecuta create_app() desde run.py).'''

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)

    @app.context_processor
    def inject_year():
        return {'year': datetime.now().year}

    return app