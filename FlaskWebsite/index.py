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
        return flask.redirect(flask.url_for("bookPage",bookName=form.name.data))
    return flask.render_template('index.html',form=form)
    
@app.route('/book')
def bookPage():
    bookName = flask.request.args.get('bookName')
    similarityDict = {'Hi':0.9, 'Hello': 0.1}
    return flask.render_template('bookPage.html', similarityDict=similarityDict)

if __name__=='__main__':
    app.run(debug=True)