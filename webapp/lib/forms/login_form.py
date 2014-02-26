from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, ValidationError
from webapp.lib.db import User

invalid_message = "Invalid email or password."


class LoginForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember Me', default=False)

    def validate_email(self, field):
        user = User.query.filter_by(email=self.email.data).first()

        if user is None:
            raise ValidationError(invalid_message)

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()

        if user is None:
            raise ValidationError(invalid_message)

        if user.check_password(self.password.data) is False:
            raise ValidationError(invalid_message)
