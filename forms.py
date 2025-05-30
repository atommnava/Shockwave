from wtforms import Form, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('Full Name', [validators.Length(min=1, max=64)])
    username = StringField('Username', [validators.Length(min=2, max=32)])
    email = StringField('Email', [validators.Length(min=6, max=64)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message="Password do not match")])
    confirm = PasswordField('Confirm Password')

class SendMoneyForm(Form):
    username = StringField('Username', [validators.Length(min=2, max=32)])
    amount = StringField('Amount', [validators.Length(min=1, max=64)])

class BuyForm(Form):
    amount = StringField('Amount', [validators.Length(min=1, max=64)])

