from flask import Flask
from flask import request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

dict = {'name1': 'Dawid',
        'name2': 'Dave',
        'name3': 'Dawcio'}
@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # user_agent = request.headersgit config core.autocrlf true
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/<name>')
def name(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)