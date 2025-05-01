from flask import Blueprint, render_template
from datetime import datetime

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

@main.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')

