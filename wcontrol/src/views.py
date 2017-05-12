from flask import render_template, flash, redirect, url_for, g
from flask_login import login_user, logout_user, current_user
from flask_login import LoginManager
from datetime import datetime
from wcontrol.src.app import app
from wcontrol.src.models import db, User, Control
from wcontrol.src.oauth import OAuthSignIn
from wcontrol.src.forms import EditForm, NewControlForm
from wcontrol.src.results import results
from wcontrol.conf.config import MEASUREMENTS

lm = LoginManager(app)


def index():
    user = g.user
    control = user.get_last_control()
    if control is None:
        return render_template("index.html",
                               title="Home",
                               user=user)
    result = results(control)
    return render_template("index.html",
                           title="Home",
                           user=user,
                           control=control,
                           result=result)


def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    nickname, name, email = oauth.callback()
    if email is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(email=email).first()
    if not user:
        if nickname is None or nickname == "":
            nickname = email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        if name is None or name == "":
            name = nickname
        date = datetime.utcnow()
        height = 0
        age = 0
        user = User(nickname=nickname,
                    name=name,
                    email=email,
                    date=date,
                    height=height,
                    age=age)
        db.session.add(user)
        db.session.commit()
    login_user(user, remember=False)
    return redirect(url_for('index'))


def login():
    if g.user is not None and g.user.is_authenticated:
        flash('inside if g.user in login()')
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In')


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


def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if not user:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    return render_template('user.html',
                           title="User Profile",
                           user=user)


def edit(nickname):
    if g.user.nickname != nickname:
        flash('You can not edit someone else profile')
        return redirect(url_for('user', nickname=g.user.nickname))
    user = User.query.filter_by(nickname=nickname).first()
    form = EditForm(user.nickname)
    if form.validate_on_submit():
        user.nickname = form.nickname.data
        user.name = form.name.data
        user.age = form.age.data
        user.height = form.height.data
        user.weight = form.weight.data
        user.bmi = form.bmi.data
        user.fat = form.fat.data
        user.muscle = form.muscle.data
        user.visceral = form.visceral.data
        user.rmr = form.rmr.data
        user.bodyage = form.bodyage.data
        db.session.add(user)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('user', nickname=user.nickname))
    else:
        form.nickname.data = user.nickname
        form.name.data = user.name
        form.age.data = user.age
        form.height.data = user.height
        form.weight.data = user.weight
        form.bmi.data = user.bmi
        form.fat.data = user.fat
        form.muscle.data = user.muscle
        form.visceral.data = user.visceral
        form.rmr.data = user.rmr
        form.bodyage.data = user.bodyage
    return render_template('edit.html',
                           title="Edit User Profile",
                           user=user,
                           form=form)


def add(nickname):
    if g.user.nickname != nickname:
        flash('You can not add someone else controls')
        return redirect(url_for('controls', nickname=g.user.nickname))
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
        control = Control(user_id=user.id, date=form.date.data)
        for m in form.measurements:
            for x, y, z in MEASUREMENTS:
                if m.form.value.label == z:
                    control.set_attribute(y, m.form.value.data)
        db.session.add(control)
        db.session.commit()
        flash('Your control has been added')
        return redirect(url_for('index'))
    else:
        form.date.data = datetime.utcnow()
    return render_template('add.html',
                           title="Add New Control",
                           user=user,
                           form=form)


def controls(nickname):
    if g.user.nickname != nickname:
        flash('You can see someone else controls')
        return redirect(url_for('controls', nickname=g.user.nickname))
    user = User.query.filter_by(nickname=nickname).first()
    return render_template('controls.html',
                           title="User's Controls List",
                           user=user)


def control_edit(nickname, id):
    if g.user.nickname != nickname:
        flash('You can not edit someone else controls')
        return redirect(url_for('controls', nickname=g.user.nickname))
    user = User.query.filter_by(nickname=nickname).first()
    control = Control.query.filter_by(id=id).first()
    if not control:
        flash('Control does not exist')
        return redirect(url_for('controls', nickname=g.user.nickname))
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
        for m in form.measurements:
            for x, y, z in MEASUREMENTS:
                if m.form.value.label == z:
                    control.set_attribute(y, m.form.value.data)
        db.session.add(control)
        db.session.commit()
        flash('Your control has been edited')
        return redirect(url_for('controls', nickname=g.user.nickname))
    else:
        form.date.data = control.date
        for m in form.measurements:
            for x, y, z in MEASUREMENTS:
                if m.form.value.label == z:
                    m.form.value.data = control[x][1]
    return render_template('edit_control.html',
                           title="Edit Control",
                           form=form)


def control_remove(nickname, id):
    if g.user.nickname != nickname:
        flash('You can not remove someone else controls')
        return redirect(url_for('controls', nickname=g.user.nickname))
    control = Control.query.filter_by(id=id).first()
    if not control:
        flash('Control does not exist')
        return redirect(url_for('controls', nickname=g.user.nickname))
    db.session.delete(control)
    db.session.commit()
    flash('The control has been deleted')
    return redirect(url_for('controls', nickname=g.user.nickname))
