from flask import render_template,abort,redirect,url_for,request,flash
from . import main
from ..models import User, Pitch, Comment, Category
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db,photos
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch'
    categories = Category.query.all()
    return render_template('index.html', title=title, categories=categories)

@main.route('/pitches/<category_id>')
def pitches_by_category(category_id):
    '''
    View pitches page function that displays the picthes available
    '''
    pitches = Pitch.get_category_pitch(category_id)
    categories = Category.query.all()
    return render_template('categories.html', pitches = pitches, categories=categories)

@main.route('/about')
def about():
    '''
    View page function that returns the about page and its data
    '''
    title = 'About | Pitch'
    categories = Category.query.all()
    return render_template('about.html', title=title, categories=categories)

@main.route('/user/<uname>')
def profile(uname):
    categories = Category.query.all()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, categories=categories)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    categories = Category.query.all()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form, categories=categories)

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

@main.route('/new-pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    title = 'New Pitch'
    form = PitchForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        pitch = Pitch(pitch_content=form.pitch_content.data, pitcher=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been posted!', 'success')
        return redirect(url_for('main.twitter'))

    return render_template('create_pitch.html',title=title, pitch_form=form, categories=categories)

@main.route("/comment/<int:id>", methods=['GET', 'POST'])
@login_required
def new_comment(id):
    title = 'New Comment'
    form = CommentForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        comment = Comment(comment_content=form.comment_content.data, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('main.twitter', id=id))

    return render_template('add_comment.html', title=title, comment_form=form, categories=categories )

# @main.route('/categories/twitter-pitch')
# def twitter():
#     '''
#     View page function that returns the categories page and its data
#     '''
#     title = 'Categories | Twitter'
#     pitches = Pitch.query.all()
#     comments = Comment.query.all()
#     return render_template('categories/twitter.html', title=title, pitches=pitches,comments=comments)

# @main.route('/categories/elevator-pitch')
# def elevator():
#     '''
#     View page function that returns the categories page and its data
#     '''
#     title = 'Categories | Elevator'
#     return render_template('categories/elevator.html', title=title)

# @main.route('/categories/competitor-pitch')
# def competitor():
#     '''
#     View page function that returns the categories page and its data
#     '''
#     title = 'Categories | Competitor'
#     return render_template('categories/competitor.html', title=title)

# @main.route('/categories/investor-pitch')
# def investor():
#     '''
#     View page function that returns the categories page and its data
#     '''
#     title = 'Categories | Investor'
#     return render_template('categories/investor.html', title=title)

