from wtforms import Form, validators, StringField, PasswordField, TextAreaField, SelectField, SelectMultipleField, RadioField
from classes.cat import Cat


class RegisterForm(Form):

    username = StringField("Username",[validators.Length(min=4,max=25)])
    email = StringField("Email",[validators.Length(min=6,max=25)])
    password = PasswordField("Password",[
        validators.DataRequired(),
        validators.Length(min=6,max=25),
        validators.EqualTo("confirm", message="Passwords do not match.")
    ])
    confirm = PasswordField("Confirm password", [validators.DataRequired()])




class LoginForm(Form):

    username = StringField("Username",[validators.Length(min=4,max=25),validators.DataRequired()])

    password = PasswordField("Password",[validators.DataRequired()])


class NewCatForm(Form):


    # cat = Cat()
    # owners = cat.getOwners()

    catName = StringField("Cat's Name",[validators.DataRequired(),validators.Length(min=3,max=50)])
    catOwner = SelectField("Owner's Name", coerce=int) # choices=owners,
    catMedication = RadioField("Needs   Medication:", choices=[('no', 'No'), ('yes', 'Yes')], default='no')
    catMedicationDetails = TextAreaField("Medication Details",[validators.Length(min=0,max=255)])
    catDiet = TextAreaField("Diet",[validators.Length(min=0,max=255)])
    catLikesDislikes = TextAreaField("Likes/Dislikes",[validators.Length(min=0,max=255)])
    catBehaviour =  RadioField("Has behavioural issues:", choices=[('no', 'No'), ('yes', 'Yes')], default='no')
    catBehaviourDetails = TextAreaField("Behaviour Details",[validators.Length(min=0,max=255)])
    catOther = TextAreaField("Other",[validators.Length(min=0,max=255)])
    catDepatureDate = StringField("Depature Date",[validators.Length(min=0,max=40)])


class NewOwnerForm(Form):
    
    ownerName = StringField("Owner's Name",[validators.Length(min=3,max=55),validators.DataRequired()])
    ownerAddress = StringField("Owner's Address",[validators.Length(min=3,max=80)])
    ownerPhoneNumber = StringField("Owner's Phone Number",[validators.Length(min=3,max=25)])
    ownerEmail = StringField("Owner's Email",[validators.Length(min=3,max=80)])

