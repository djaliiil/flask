from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField,SubmitField


class UserSignUp(Form):
    username = StringField('username',[validators.Length(min=3, max=35)])
    password = PasswordField('password',[validators.Length(min=3, max=35)])
    email = StringField('email',[validators.Length(min=3, max=35)])
    phone = StringField('phone',[validators.Length(min=3, max=35)])
    fullname = StringField('fullname',[validators.Length(min=3, max=35)])
    submit = SubmitField('userSignUp')


class LoginForm(Form):
    username = StringField('username', [validators.Length(min=3, max=35)])
    password = PasswordField('password', [validators.Length(min=3, max=35)])
    remember = BooleanField('remember me')