from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),nullable=False,unique=True)
    email=db.Column(db.String(50))
    password_hash=db.Column(db.String)
    contact=db.Column(db.String)
    address=db.Column(db.String)
    profile_pic_path=db.Column(db.String,default='profile.png')
    bio=db.Column(db.String)
    post=db.relationship('Post',backref='user',lazy='dynamic')
    comment=db.relationship('Comment',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot access password!')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    post=db.Column(db.String,nullable=False)
    picture=db.Column(db.String)
    posted_date=db.Column(db.DateTime,default=time_zone)
    upvotes=db.Column(db.Integer)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.relationship('Comment',backref='post',lazy='dynamic')

    def __repr__(self):
        return f'Post {self.post}'

class Comment(db.Model):
    __tablename__="comments"
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        return Comment.query.filter_by(post_id=id).all()