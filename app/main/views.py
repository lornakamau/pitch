from flask import render_template,abort,redirect,url_for,request
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch'
    return render_template('index.html', title=title)

@main.route('/categories/twitter-pitch')
def twitter():
    '''
    View page function that returns the categories page and its data
    '''
    title = 'Categories | Twitter'
    return render_template('categories/twitter.html', title=title)

@main.route('/categories/elevator-pitch')
def elevator():
    '''
    View page function that returns the categories page and its data
    '''
    title = 'Categories | Elevator'
    return render_template('categories/elevator.html', title=title)

@main.route('/categories/competitor-pitch')
def competitor():
    '''
    View page function that returns the categories page and its data
    '''
    title = 'Categories | Competitor'
    return render_template('categories/competitor.html', title=title)

@main.route('/categories/investor-pitch')
def investor():
    '''
    View page function that returns the categories page and its data
    '''
    title = 'Categories | Investor'
    return render_template('categories/investor.html', title=title)

@main.route('/about')
def about():
    '''
    View page function that returns the about page and its data
    '''
    title = 'About | Pitch'
    return render_template('about.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
