from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class StudentForm(FlaskForm):

    fname = StringField("First Name", validators=[DataRequired(), Length(min=1, max=140)], id="fname")
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=1, max=140)], id="lname")
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=1, max=140)], id="email")
    gpa = DecimalField("GPA", validators=[DataRequired()], id="gpa")
    phone = IntegerField("Phone No", validators=[DataRequired()], id="pno")
    submit = SubmitField("Submit")
