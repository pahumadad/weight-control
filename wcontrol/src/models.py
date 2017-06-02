from wcontrol.src.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from collections import OrderedDict
from wcontrol.conf.config import MEASUREMENTS

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.DateTime)
    height = db.Column(db.Float(Precision=2))
    age = db.Column(db.Integer)
    weight = db.Column(db.Boolean, default=False)
    bmi = db.Column(db.Boolean, default=False)
    fat = db.Column(db.Boolean, default=False)
    muscle = db.Column(db.Boolean, default=False)
    visceral = db.Column(db.Boolean, default=False)
    rmr = db.Column(db.Boolean, default=False)
    bodyage = db.Column(db.Boolean, default=False)
    control_user = db.relationship('Control', backref='user', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def get_id(self):
        return str(self.id)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

    def __getitem__(self, index):
        if index == 0:
            return self.weight
        if index == 1:
            return self.bmi
        if index == 2:
            return self.fat
        if index == 3:
            return self.muscle
        if index == 4:
            return self.visceral
        if index == 5:
            return self.rmr
        if index == 6:
            return self.bodyage

    def get_measurements(self):
        measures = []
        for x, y, z in MEASUREMENTS:
            if self[x] is True:
                measures.append(z)
        return measures

    def get_measurements_dict(self):
        measures = OrderedDict()
        for x, y, z in MEASUREMENTS:
            if self[x] is True:
                measures.update({y: z})
        return measures

    def get_measurements_index(self):
        measures = []
        for x, y, z in MEASUREMENTS:
            if self[x] is True:
                measures.append(x)
        return measures

    def get_controls(self):
        return Control.query.filter(Control.user_id == self.id)\
                      .order_by(Control.date.desc(), Control.id.desc())

    def get_controls_dict(self):
        controls = Control.query.filter(Control.user_id == self.id)\
                          .order_by(Control.date.asc(), Control.id.asc())
        controls_dict = OrderedDict()
        aux = 0
        for control in controls:
            controls_dict.update({aux: OrderedDict()})
            for j in range(7):
                controls_dict[aux].update({j: control[j][0]})
            aux += 1
        return controls_dict

    def get_controls_date_dict(self):
        controls = Control.query.filter(Control.user_id == self.id)\
                          .order_by(Control.date.asc(), Control.id.asc())
        dates_dict = OrderedDict()
        aux = 0
        for control in controls:
            dates_dict.update({aux: control[7][0]})
            aux += 1
        return dates_dict

    def get_last_control(self):
        return Control.query.filter(Control.user_id == self.id)\
                      .order_by(Control.date.desc(), Control.id.desc()).first()


class Control(db.Model):
    __tablename__ = 'controls'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.DateTime)
    weight = db.Column(db.Float(Precision=2), default=0)
    bmi = db.Column(db.Float(Precision=2), default=0)
    fat = db.Column(db.Float(Precision=2), default=0)
    muscle = db.Column(db.Float(Precision=2), default=0)
    visceral = db.Column(db.Float(Precision=2), default=0)
    rmr = db.Column(db.Float(Precision=2), default=0)
    bodyage = db.Column(db.Float(Precision=2), default=0)

    def __repr__(self):
        return '<Control %r>' % (self.id)

    def __getitem__(self, index):
        if index == 0:
            return [self.weight, MEASUREMENTS[0][1], MEASUREMENTS[0][2]]
        if index == 1:
            return [self.bmi, MEASUREMENTS[1][1], MEASUREMENTS[1][2]]
        if index == 2:
            return [self.fat, MEASUREMENTS[2][1], MEASUREMENTS[2][2]]
        if index == 3:
            return [self.muscle, MEASUREMENTS[3][1], MEASUREMENTS[3][2]]
        if index == 4:
            return [self.visceral, MEASUREMENTS[4][1], MEASUREMENTS[4][2]]
        if index == 5:
            return [self.rmr, MEASUREMENTS[5][1], MEASUREMENTS[5][2]]
        if index == 6:
            return [self.bodyage, MEASUREMENTS[6][1], MEASUREMENTS[6][2]]
        if index == 7:
            return [self.date, '', '']

    def set_attribute(self, attr, value):
        self.__setattr__(attr, value)
