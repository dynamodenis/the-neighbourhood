from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, SelectField,TextAreaField
from wtforms.validators import Required

class InForm(FlaskForm):
    speak_out = TextAreaField('Is it Happening: What?')
    title = StringField('Title')
    submit = SubmitField('Submit')

 
class Commentform(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What is interesting about you', validators=[Required()])
    submit = SubmitField('submit')
