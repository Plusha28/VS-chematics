"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from VS_schematics import app

@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='VS-schematics',
        year=datetime.now().year,
        message='Главная'
    )

@app.route('/category')
def category():
    """Renders the category page."""
    return render_template(
        'category.html',
        title='Category',
        year=datetime.now().year,
        message='Категории'
    )

@app.route('/rules')
def rules():
    """Renders the rules page."""
    return render_template(
        'rules.html',
        title='Rules',
        year=datetime.now().year,
        message='Правила'
    )

@app.route('/creators')
def creators():
    """Renders the creators page."""
    return render_template(
        'creators.html',
        title='Creators',
        year=datetime.now().year,
        message='Авторам'
    )

@app.route('/contacts')
def contacts():
    """Renders the contacts page."""
    return render_template(
        'contacts.html',
        title='Contacts',
        year=datetime.now().year,
        message='Контакты'
    )

@app.route('/register')
def register():
    """Renders the contacts page."""
    return render_template(
        'register.html',
        title='Регистрация',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the contacts page."""
    return render_template(
        'login.html',
        title='Вход',
        year=datetime.now().year,
    )