import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


class NameForm(FlaskForm):
    name = StringField('Jak masz na imię?', validators=[DataRequired()])
    mess = StringField('Twoja wiadomość', validators=[DataRequired()])
    pw = PasswordField('Twoje hasło')
    submit = SubmitField('Wyślij')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

dict = {'name1': 'Dawid',
        'name2': 'Dave',
        'name3': 'Dawcio'}


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    mess = None
    pw = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        mess = form.mess.data
        form.mess.data = ''
        pw = form.pw.data
        form.pw.data = ''
    return render_template('index.html', form=form, name=name, mess=mess, pw=pw)


if __name__ == "__main__":
    app.run(debug=True)