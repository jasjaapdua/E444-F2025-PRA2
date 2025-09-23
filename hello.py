from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = "efbae2b6ea473d2e8d65eec7dfdd7937c0881f23d9ce0a1d3ea0b99f39f7f3eb"


def validate_utoronto_email(form, field):
    if "utoronto" not in field.data.lower():
        raise ValidationError("Email must be a valid UofT email address (contain 'utoronto').")


class NameForm(FlaskForm):
    name = StringField(
        'What is your name?', 
        validators=[DataRequired()]
    )
    email = EmailField(
        label="What is your UofT email address?", 
        validators=[DataRequired(), validate_utoronto_email]
    )
    submit = SubmitField(
        'Submit'
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
    return render_template('index.html', form=form, name=name, email=email)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
