from flask import Blueprint, render_template
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')  

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/skills')
def skills():
    return render_template('skills.html')

@main.route('/experience')
def experience():
    return render_template('experience.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

