from wtforms import Form,StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email

class SignUpForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField()

    def __repr__(self):
        return "{}".format(self.username)