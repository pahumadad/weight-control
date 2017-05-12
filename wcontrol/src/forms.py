from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField,\
                    DateField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired
from wcontrol.src.models import User


GENDER = [('Female', 'Female'), ('Male', 'Male')]


class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    gender = SelectField('gender', choices=GENDER)
    age = IntegerField('age')
    height = DecimalField('height', places=2)
    weight = BooleanField('weight')
    bmi = BooleanField('bmi')
    fat = BooleanField('fat')
    muscle = BooleanField('muscle')
    visceral = BooleanField('visceral')
    rmr = BooleanField('rmr')
    bodyage = BooleanField('bodyage')

    def __init__(self, original_nickname, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user:
            msg = 'This nickname is already in use. Please chose another one.'
            self.nickname.errors.append(msg)
            return False
        return True


class MeasurementEntry(FlaskForm):
    value = DecimalField(validators=[DataRequired()])

    def __init__(self, csrf_enabled=False, *args, **kwargs):
        super(MeasurementEntry, self).__init__(csrf_enabled=csrf_enabled,
                                               *args, **kwargs)


class NewControlForm(FlaskForm):
    date = DateField('date')
    measurements = FieldList(FormField(MeasurementEntry))
