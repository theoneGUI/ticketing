# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, DataRequired

# login and registration

statuses = [
            ( 'in_progress', 'In Progress'),
            ( 'complete', 'Complete'),
        ]

class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    
class CreateTicketForm(FlaskForm):
    title = StringField('Title',
                    id='title_create',
                    validators=[DataRequired()])
    opener = StringField('Name Please',
                    id='opener_create',
                    validators=[DataRequired()])
    category = SelectField('Category',
                    id='category_create',
                    validators=[DataRequired()],
                    choices=[
                        ( 'help_desk', 'Tech Help Desk'),
                        ( 'printing', 'Printing Needs'),
                        ( 'broken', 'Something\'s Broken'),
                        ( 'pictures', 'Pictures Needed'),
                        ( 'presentation', 'Presentation Help'),
                        ( 'user_error', 'User Error'),
                        ( 'discord', 'Discord'),
                        ('drive', 'Google Drive'),
                        ('misc', 'Miscellaneous')
                    ])
    desc = StringField('Description',
                    id='description_create',
                    validators=[DataRequired()])
    
class EditTicketForm(FlaskForm):
    category = SelectField('Status',
        id='category_create',
        validators=[DataRequired()],
        choices=statuses)
