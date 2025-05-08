from flask import Flask
from datetime import datetime
from app.routes import main  
from flask_mail import Mail, Message
from .extensions import mail  
# from .routes import main
'''El import from .routes import main solo funciona si app es tratado como un paquete Python (por ejemplo, cuando Flask ejecuta create_app() desde run.py).'''

def create_app():
    app = Flask(__name__)

    app.secret_key = '7b6cba071352bf3d85de263b736b5f171e877dae66082bf19489b4715bae9f01'
    # Configuración del correo (ejemplo con Gmail)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'leanvarela6@gmail.com'  # Tu correo
    app.config['MAIL_PASSWORD'] = 'lruabarhfquhqxsf'  # Tu contraseña de aplicación
    app.config['MAIL_DEFAULT_SENDER'] = 'leanvarela6@gmail.com'

    app.register_blueprint(main)

    
    mail.init_app(app)

    @app.context_processor
    def inject_year():
        return {'year': datetime.now().year}

    return app