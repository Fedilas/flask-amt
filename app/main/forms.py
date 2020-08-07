from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length, Optional
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)], description='write to your teammate',
                            render_kw={'id': 'message', 'width': '50%', 'placeholder': 'write to your teammate'})
    submit = SubmitField(render_kw={'id': 'next', "type": "submit", "value": "Send"})


class CodeForm(FlaskForm):
    code = TextAreaField(_l('Insert your code here to get paid for your bonuses'), validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={'id': 'code'})
    gender = SelectField('Which one of these genders do you identify with?',
                         choices=[(None, '---'), ('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),
                                  ('Prefer not to say', 'Prefer not to say')], coerce=str)
    age = SelectField('Which one of these age groups do you belong to?',
                      choices=[(None, '---'), ('15-19', '15-19'), ('20-29', '20-29'), ('30-39', '30-39'),
                               ('40-49', '40-49'), ('50+', '50+')], coerce=str)
    nationality = TextAreaField(_l('Your Nationality'), validators=[
        DataRequired(), Length(min=1, max=30)], render_kw={'id': 'nationality'})
    education = SelectField('Your educational background',
                            choices=[(None, '---'), ('Less than High School', 'Less than High School'),
                                     ('High School', 'High School'),
                                     ('Some College', 'Some College'),
                                     ('College Degree', 'College Degree'),
                                     ('Postgraduate Education', 'Postgraduate Education')], coerce=str)
    experience = SelectField('Have you played similar games before?',
                             choices=[(None, '---'), ('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], coerce=str)
    answers = [(None, '---'), ('Very poorly', 'Very poorly'), ('Poorly', 'Poorly'), ('Moderately', 'Moderately'),
               ('Well', 'Well'),
               ('Very well', 'Very well')]

    performance = SelectField('How well did the team perform?',
                              choices=answers, coerce=str)
    cohesion = SelectField('How cohesive was the team?',
                           choices=answers, coerce=str)
    communication = SelectField('How well did the team communicate?',
                                choices=answers, coerce=str)
    balance = SelectField('Was the teamwork well balanced between the two players?',
                          choices=answers, coerce=str)
    satisfaction = SelectField('Would you play with the same teammate again?',
                               choices=[(None, '---'), ('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], coerce=str)

    submit = SubmitField(render_kw={'id': 'code', "type": "submit", "value": "Submit"})


class ChatForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[
        Optional()])
    room = StringField('Room', validators=[
        Optional()])
    submit = SubmitField('Enter the Maze')


class TextForm(FlaskForm):
    text_area = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=10, max=60)], render_kw={'id': 'explore', 'class': 'form-control', 'rows': 7,
                                                            'placeholder': 'the conversation is displayed here'})

    text = TextAreaField(_l('<strong>Enter your message here</strong>'), validators=[
        DataRequired(), Length(min=1, max=30)], render_kw={'id': 'text', 'placeholder': 'write to your teammate here'})
    submit = SubmitField(render_kw={"style": "display: none"})
