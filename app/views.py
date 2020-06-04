from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch'
    return render_template('base.html', title=title)