from flask_login import login_required
from wcontrol.src.main import app
from wcontrol.src.models import db
import wcontrol.src.views as view
import sys


@app.route('/')
@app.route('/index')
@login_required
def index():
    return view.index()


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    return view.oauth_authorize(provider)


@app.route('/callback/<provider>')
def oauth_callback(provider):
    return view.oauth_callback(provider)


@app.route('/login')
def login():
    return view.login()


@app.route('/logout')
@login_required
def logout():
    return view.logout()


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    return view.user(nickname)


@app.route('/user/<nickname>/edit', methods=['GET', 'POST'])
@login_required
def edit(nickname):
    return view.edit(nickname)


@app.route('/user/<nickname>/add', methods=['GET', 'POST'])
@login_required
def add(nickname):
    return view.add(nickname)


@app.route('/user/<nickname>/controls')
@login_required
def controls(nickname):
    return view.controls(nickname)


@app.route('/controls/remove/<int:id>')
@login_required
def control_remove(id):
    return view.control_remove(id)
@app.route('/user/<nickname>/controls/remove/<int:id>')
@login_required
def control_remove(nickname, id):
    return view.control_remove(nickname, id)


if __name__ == "__main__":
    if len(sys.argv):
        if sys.argv[1] == "-c" or sys.argv[1] == "--creatredb":
            db.create_all()
