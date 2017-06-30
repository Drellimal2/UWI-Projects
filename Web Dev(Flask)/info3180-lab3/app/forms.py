from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField
# other fields include PasswordField
from wtforms.validators import Required, Email

class ContactForm(Form):
    name = TextField('Username', [])
    email = TextField('Email', [Required(), Email()])
    subject = TextField('Subject', [Required()])
    msg = TextAreaField('Message', [Required()])
