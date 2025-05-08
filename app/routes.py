from flask import Blueprint, render_template, request, redirect, flash, url_for
from datetime import datetime
from app.extensions import mail
from flask_mail import Message

main = Blueprint('main', __name__)

@main.route('/', strict_slashes=False)
def home():
    return render_template('home.html')  

@main.route('/projects', strict_slashes=False)
def projects():
    return render_template('projects.html')

@main.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


@main.route('/skills', strict_slashes=False)
def skills():
    return render_template('skills.html')

@main.route('/experience', strict_slashes=False)
def experience():
    return render_template('experience.html')

@main.route('/message', strict_slashes=False)
def message():
    return render_template('message_email.html')


@main.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        msg = Message(
            subject=f"Nuevo mensaje de {nombre}",
            sender=correo,
            recipients=['leanvarela6@gmail.com'],
            body=f"Nombre: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"
        )

        try:
            mail.send(msg)
            flash("¡Mensaje enviado exitosamente!")
        except Exception as e:
            flash(f"Error al enviar mensaje: {str(e)}")

        return redirect(url_for('main.message'))

    return render_template("contact.html")


