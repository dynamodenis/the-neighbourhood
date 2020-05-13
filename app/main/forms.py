from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, SelectField,TextAreaField
from wtforms.validators import Required,Email,ValidationError
from flask_wtf.file import FileField,FileAllowed
from ..models import User
from flask_login import current_user

class PostForm(FlaskForm):
    post = TextAreaField('Is it Happening: What?')
    title = StringField('Title')
    submit = SubmitField('Submit')

 
class Commentform(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What is interesting about you', validators=[Required()])
    username=StringField('Type Your Username:')
    email=StringField('Enter Your Email Address:', validators=[Email()])
    picture=FileField('Choose a Profile Picture:', validators=[FileAllowed(['jpeg','jpg','png'])])
    submit=SubmitField('Create Account')

    def validate_username(self,data):
        if data.data != current_user.username:
            if User.query.filter_by(username=data.data).first():
                raise ValidationError('This username is taken! Choose another username.')

    def validate_email(self,data):
        if data.data != current_user.email:
            if User.query.filter_by(email=data.data).first():
                raise ValidationError('This email is taken! Choose another email.')
        
