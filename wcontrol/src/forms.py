from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired
from app.models import User


class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    age = IntegerField('age')
    height = DecimalField('heighti', places=2)

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
