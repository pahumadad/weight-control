from flask_login import login_required
from wcontrol.src.main import app
import wcontrol.src.views as view


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
