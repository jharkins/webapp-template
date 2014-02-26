from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, ValidationError
from webapp.lib.db import User


class RegistrationForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])

    def validate_email(self, field):
        user = User.query.filter(User.email == self.email.data).first()

        if user is not None:
            raise ValidationError("This email address is already registered.")
