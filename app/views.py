from flask import render_template, flash, redirect, url_for, session, request, g
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app import app, db, lm
from .models import User
from .oauth import OAuthSignIn
from .forms import EditForm, NewControlForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template("index.html",
                           title="Home",
                           user=user)

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    nickname, name, email = oauth.callback()
    if email is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user=User.query.filter_by(email=email).first()
    if not user:
        if nickname is None or nickname == "":
            nickname = email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        if name is None or name == "":
            name = nickname
        date = datetime.utcnow()
        height = 0
        age = 0
        user=User(nickname=nickname,
                  name=name,
                  email=email,
                  date=date,
                  height=height,
                  age=age)
        db.session.add(user)
        db.session.commit()
    login_user(user, remember=False)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    if g.user is not None and g.user.is_authenticated:
        flash('inside if g.user in login()')
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    return render_template('user.html',
                            title="User Profile",
                            user=user)


@app.route('/user/<nickname>/edit', methods=['GET', 'POST'])
@login_required
def edit(nickname):
    if g.user.nickname != nickname:
        flash('You can not edit someone else profile')
        return redirect(url_for('user', nickname=g.user.nickname))
    user = User.query.filter_by(nickname=nickname).first()
    form = EditForm(user.nickname)
    if form.validate_on_submit():
        user.nickname = form.nickname.data
        user.name     = form.name.data
        user.age      = form.age.data
        user.height   = form.height.data
        user.weight   = form.weight.data
        user.bmi      = form.bmi.data
        user.fat      = form.fat.data
        user.muscle   = form.muscle.data
        user.viceral  = form.viceral.data
        user.bmr      = form.bmr.data
        user.bodyage  = form.bodyage.data
        db.session.add(user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', nickname=user.nickname))
    else:
        form.nickname.data = user.nickname
        form.name.data     = user.name
        form.age.data      = user.age
        form.height.data   = user.height
        form.weight.data   = user.weight
        form.bmi.data      = user.bmi
        form.fat.data      = user.fat
        form.muscle.data   = user.muscle
        form.viceral.data  = user.viceral
        form.bmr.data      = user.bmr
        form.bodyage.data  = user.bodyage
    return render_template('edit.html',
                            title="Edit User Profile",
                            user=user,
                            form=form)


@app.route('/<nickname>/add', methods=['GET', 'POST'])
@login_required
def add(nickname):
    if g.user.nickname != nickname:
        flash('You can not add someone else controls')
        return redirect(url_for('user', nickname=g.user.nickname))
    user = User.query.filter_by(nickname=nickname).first()
    user_measurements = user.get_measurements_dict()
    form = NewControlForm(measurements=user_measurements)
    i = 0
    for m in form.measurements:
        m.form.value.label = list(user_measurements.values())[i]
        i += 1
    if i == 0:
        flash('You have to select your measurements')
        return redirect(url_for('user', nickname=user.nickname))
    if form.validate_on_submit():
        pass
    else:
        form.date.data = datetime.utcnow()
    return render_template('add.html',
                            title="Add New Control",
                            form=form)
