from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Email, EqualTo, Required
from ..models import User
import email_validator

class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(),Email()])
    author = StringField('Enter authors name', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message= 'passwords should match')])
    password_confirm = PasswordField('Confirm passswords', validators=[Required()])
    submit = SubmitField('Signup')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('An account with that email exists')
    def validate_author(self, data_field):
        if User.query.filter_by(author=data_field.data).first():
            raise ValidationError('This name is in use, choose another')

class LoginForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(), Email()])
    password = PasswordField('Enter Your Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('SIGN IN')
