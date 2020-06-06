from flask import render_template,abort
from . import main
from ..models import User

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch'
    return render_template('index.html', title=title)

@main.route('/categories')
def categories():
    '''
    View page function that returns the categories page and its data
    '''
    title = 'Categories'
    return render_template('categories.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
