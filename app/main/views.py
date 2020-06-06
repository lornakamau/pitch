from flask import render_template
from . import main

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