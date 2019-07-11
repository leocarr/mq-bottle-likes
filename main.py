from bottle import template, Bottle, debug, redirect, request, static_file
import database
import sqlite3


app = Bottle()
debug(True)

@app.route('/')
def index(db):
    """Home page"""

    info = {
        'title': 'Welcome Home!',
        'likes': database.get_likes(db)
    }

    return template('index', info)


@app.post('/likes')
def like(db):
    """Process like form post request"""

    # get the form field
    likes = request.forms.get('likes')

    if likes:
        database.store_like(db, likes)

    return redirect('/')


@app.route('/static/<filepath:path>')
def static(filepath):

    return static_file(filepath, root='static')


if __name__ == "__main__":
    # code to connect to the database and create the tables
    from bottle.ext import sqlite

    DATABASE_NAME = 'test.db'
    db = sqlite3.connect(DATABASE_NAME)
    database.create_tables(db)

    # code to run our web application
    plugin = sqlite.Plugin(dbfile=DATABASE_NAME)
    app.install(plugin)

    # run the application
    app.run()

