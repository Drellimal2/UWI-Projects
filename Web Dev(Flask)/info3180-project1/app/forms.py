from flask.ext.wtf import Form
from wtforms.fields import TextField, FileField, SelectField, IntegerField
# other fields include PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms.validators import Required

class ProfileForm(Form):
    image = FileField('image', validators=[])
    firstname = TextField('firstname', [Required()])
    lastname = TextField('lastname', [Required()])
    age = TextField('age', [Required()])
    sex = SelectField('sex', choices=[('M', 'Male'), ('F', 'Female')],validators=[Required()])