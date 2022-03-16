from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Jak masz na imię?', validators=[DataRequired()])
    mess = StringField('Twoja wiadomość', validators=[DataRequired()])
    pw = PasswordField('Twoje hasło')
    submit = SubmitField('Wyślij')