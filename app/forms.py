from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField
from wtforms.validators import DataRequired
from app.models import User

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    name     = StringField('name', validators=[DataRequired()])
    age      = IntegerField('age')
    height   = DecimalField('heighti', places=2)
    weight   = BooleanField('Weight')
    bmi      = BooleanField('BMI')
    fat      = BooleanField('Fat')
    muscle   = BooleanField('Muscle')
    viceral  = BooleanField('Viceral Fat')
    bmr      = BooleanField('Basal Metabolic Rate')
    bodyage  = BooleanField('Body Age')


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
