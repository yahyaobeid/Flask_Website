from flask_wtf import FlaskForm
from wtforms impirt StringField, PasswordField, SubmitField
from wtforms.validators import DateRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blog_site.models import User

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match')])
	pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	def check_email(self):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Your email is already connected to an account!')

	def check_username(self):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Your username is already connected to an account!')


class UdateUserForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('username', validators=[DataRequired()])
	picture = FileFiled('Update Profile Pricture', validators=FileAllowed(['jpg', 'png']))
	submit = SubmitField('Update')

	def check_email(self):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Your email is already connected to an account!')

	def check_username(self):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Your username is already connected to an account!')
