from flask import render_template

from . import main

@main.errorhandler(404)
def fourOfour(error):

    return render_template('fourOfour.html')(virtual) root@Kali:~/PythonProjects/the-neighbourhood/app/main# cat forms.py 
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, SelectField,TextAreaField
from wtforms.validators import Required

class InForm(FlaskForm):
    speak_out = TextAreaField('Is it Happening: What?')
    title = StringField('Title')
    category = SelectField(u'info category', choices=[('Covid', 'Covid'), ('Empowerment', 'Empowerment'), ('Community Gatherings', 'Community Gatherings'), ('Adventures', 'Adventures'), ('Our Youth', 'Our Youth'), ('Safety', 'Safety')])
    submit = SubmitField('Submit')

 
class Commentform(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What is interesting about you', validators=[Required()])
    submit = SubmitField('submit')
