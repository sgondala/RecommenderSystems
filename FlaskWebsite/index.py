# -*- coding: utf-8 -*-


import flask
import wtforms
import flask_bootstrap
import flask_moment
from flask_wtf import FlaskForm


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'Hola'

bootstrap = flask_bootstrap.Bootstrap(app)
moment = flask_moment.Moment(app)

class BookForm(FlaskForm):
    name = wtforms.StringField("Enter the book name:",
                               validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")


@app.route('/', methods=['GET','POST'])
def homePage():
    form = BookForm()
    if form.validate_on_submit():
        flask.session['name'] = form.name.data
        return flask.redirect('http://www.google.com')
    return flask.render_template('index.html',name=flask.session.get('name'),form=form)

if __name__=='__main__':
    app.run()