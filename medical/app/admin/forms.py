from flask_wtf import Form
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
    SelectField
)
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField,SubmitField

#from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,

)

from app import db
from app.models.user import Role, User


class ChangeUserEmailForm(Form):
    email = EmailField(
        'New email', validators=[InputRequired(),
                                 Length(1, 64),
                                 Email()])
    submit = SubmitField('Update email')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


class ChangeAccountTypeForm(Form):
    role = SelectField('select role', coerce=int)
    submit = SubmitField('Update role')


    def __init__(self, *args, **kwargs):
        super(ChangeAccountTypeForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                 for role in Role.query.order_by(Role.name).all()]



class InviteUserForm(Form):
    role = SelectField('select role', coerce=int)
    username = StringField(
        'username', validators=[InputRequired(),
                                  Length(1, 64)])
    phone = StringField(
        'phone', validators=[InputRequired(),
                                  Length(1, 64)])
    fullname = StringField(
        'fullname', validators=[InputRequired(),
                                 Length(1, 64)])
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    submit = SubmitField('Invite')


    def __init__(self, *args, **kwargs):
        super(InviteUserForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                 for role in Role.query.order_by(Role.name).all()]


    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
 





class NewUserForm(InviteUserForm):
    password = PasswordField('password',[validators.Length(min=3, max=35)])

    submit = SubmitField('Create')





class AddDoctorForm(Form):
    role = SelectField('select role', coerce=int)
    submit = SubmitField('Update role')





    def __init__(self, *args, **kwargs):
        super(AddDoctorForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                 for role in Role.query.order_by(Role.name).all()]

