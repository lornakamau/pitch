from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model): #db.Model helps connect our class to our database
    __tablename__ = 'users' #gives tables in our database proper names
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    comments = db.relationship('Comment', backref='author',lazy="dynamic")
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute') #raises an attribute error when we try to access the password

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self): #defines how the user object will be constructed when the class is called
        return f'USER {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment_wording = db.Column(db.String(255))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'COMMENT {self.comment_wording}'

