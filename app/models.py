from . import db

class User(db.Model): #db.Model helps connect our class to our database
    __tablename__ = 'users' #gives tables in our database proper names
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='author',lazy="dynamic")

    def __repr__(self): #defines how the user object will be constructed when the class is called
        return f'USER {self.username}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment_wording = db.Column(db.String(255))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'COMMENT {self.comment_wording}'

