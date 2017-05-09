from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, DateField, FormField, FieldList
from wtforms.validators import DataRequired
from app.models import User
from config import MEASUREMENTS

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    name     = StringField('name', validators=[DataRequired()])
    age      = IntegerField('age')
    height   = DecimalField('height', places=2)
    weight   = BooleanField('weight')
    bmi      = BooleanField('bmi')
    fat      = BooleanField('fat')
    muscle   = BooleanField('muscle')
    viceral  = BooleanField('viceral')
    bmr      = BooleanField('bmr')
    bodyage  = BooleanField('bodyage')


    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please chose another one.')
            return False
        return True


class MeasurementEntry(FlaskForm):
    value = DecimalField(places=1)


class NewControlForm(FlaskForm):
    date = DateField('date', format='%Y-%m-%d')
    measurements = FieldList(FormField(MeasurementEntry))
