from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()], render_kw={'placeholder': 'Username'})
    email = StringField(_l('Email'), validators=[DataRequired(), Email()], render_kw={'placeholder': 'email'})

    password = PasswordField(_l('Password'), validators=[DataRequired()], render_kw={'placeholder': 'password'})
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')], render_kw={'placeholder': 'repeat password'})

    likert_scale = [(None, '---'), ('Very Low', '1. Disagree Strongly'), ('Low', '2. Disagree a Little'), \
                    ('Moderate', '3. Neither Agree nor Disagree'), ('Good', '4. Agree a Little'), \
                    ('High', '5. Agree Strongly')]

    extra = SelectField(
        '<h3>Personality Traits</h3> I am reserved',
        choices=[(None, '---'), ('High', '1. Disagree Strongly'), ('Good', '2. Disagree a Little'), \
                 ('Moderate', '3. Neither Agree nor Disagree'), ('Low', '4. Agree a Little'), \
                 ('Very Low', '5. Agree Strongly')], coerce=str)
    trust = SelectField('I am generally trusting', choices=likert_scale, coerce=str)
    lazy = SelectField('I tend to be lazy',
                       choices=[(None, '---'), ('High', '1. Disagree Strongly'), ('Good', '2. Disagree a Little'), \
                                ('Moderate', '3. Neither Agree nor Disagree'),
                                ('Low', '4. Agree a Little'), \
                                ('Very Low', '5. Agree Strongly')], coerce=str)
    relax = SelectField('I am relaxed and can handle stress very well',
                        choices=[(None, '---'), ('High', '1. Disagree Strongly'), ('Good', '2. Disagree a Little'), \
                                 ('Moderate', '3. Neither Agree nor Disagree'), ('Low', '4. Agree a Little'), \
                                 ('Very Low', '5. Agree Strongly')], coerce=str)
    art = SelectField('I have few artistic interests', choices=likert_scale, coerce=str)
    social = SelectField('I am outgoing and sociable', choices=likert_scale, coerce=str)
    fault = SelectField('I tend to find faults in others', choices=likert_scale, coerce=str)
    job = SelectField('I do a thorough job', choices=likert_scale, coerce=str)
    nervous = SelectField('I get nervous easily', choices=likert_scale, coerce=str)
    imagination = SelectField('I have an active imagination', choices=likert_scale, coerce=str)
    ability = SelectField(
        'I see myself as someone whose abilities needed for team work are..',
        choices=[(None, '---'), ('Very Low', 'Very Low'), ('Low', 'Low'), \
                 ('Moderate', 'Moderate'), ('Good', 'Good'), \
                 ('High', 'High')], coerce=str)

    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
