from bottle import Bottle, debug, static_file, template

app = Bottle()
debug(True)

@app.route('/')
def index():

    info = {
        'title': 'My Main Page'
    }

    return template('index', info )


@app.route('/static/<filepath:path>')
def static(filepath):

    return static_file(filepath, root='static')


if __name__=='__main__':

    app.run()