from app import db
from flask_login import UserMixin
from config import MEASUREMENTS

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id       = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    name     = db.Column(db.String(64), index=True)
    email    = db.Column(db.String(64), index=True, unique=True)
    date     = db.Column(db.DateTime)
    height   = db.Column(db.Float(Precision=2))
    age      = db.Column(db.Integer)
    weight   = db.Column(db.Boolean, default=False)
    bmi      = db.Column(db.Boolean, default=False)
    fat      = db.Column(db.Boolean, default=False)
    muscle   = db.Column(db.Boolean, default=False)
    viceral  = db.Column(db.Boolean, default=False)
    bmr      = db.Column(db.Boolean, default=False)
    bodyage  = db.Column(db.Boolean, default=False)

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
        try:
            return unicode(self.id) # python2
        except NameError:
            return str(self.id) # python3

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
            return self.viceral
        if index == 5:
            return self.bmr
        if index == 6:
            return self.bodyage

    def get_measurements(self):
        measures = []
        for x, y, z in MEASUREMENTS:
            if self[x] is True:
                measures.append(z)
        return measures
