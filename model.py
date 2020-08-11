from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form


class RegForm(Form):
    name_first = StringField("Department", [validators.DataRequired()])
    name_last = StringField("Teacher Last Name", [validators.DataRequired()])
    rating = StringField("Enter Rating from 1 to 5", [validators.DataRequired(),])
    description = StringField("Elaborate On your rating... if you want")
    submit = SubmitField("Submit")
