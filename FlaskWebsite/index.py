# -*- coding: utf-8 -*-


import flask
import wtforms
import flask_bootstrap
import flask_moment
import cPickle as pickle
import conversion
from flask_wtf import FlaskForm


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'Hola'

bootstrap = flask_bootstrap.Bootstrap(app)
moment = flask_moment.Moment(app)

bookRatingsDict = pickle.load(open("../model.p","r"))

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


# TODO - handle when book is not there
@app.route('/book')
def bookPage():
    bookName = flask.request.args.get('bookName')
    isbnNumber = conversion.getIsbnFromBookName(bookName)
    isbnList = bookRatingsDict[isbnNumber]
    bookNameList = [(i[0],conversion.getBookNameFromISBN(i[1])) for i in isbnList]
    return flask.render_template('bookPage.html', bookNameList=bookNameList)

if __name__=='__main__':
    app.run(debug=True)