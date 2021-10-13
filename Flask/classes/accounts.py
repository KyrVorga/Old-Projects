from wtforms import Form, validators, TextAreaField, StringField, IntegerField

class AccountForm(Form):

    name = StringField('Name',[validators.length(max=50)])
    total = IntegerField('Total',[validators.length(max=25)])    
    percent = IntegerField('Percentage in',[validators.length(max=10)])
    flat = IntegerField('Flat amount in',[validators.length(max=25)])