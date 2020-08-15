from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField
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
    code = TextAreaField(_l('<h3><strong>End of task UNIQUE CODE</strong></h3>Insert your code here to get paid for your bonuses'), validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={'id': 'code'})

    experience = SelectField('<h3>About the game</h3> Have you played similar games before?',
                             choices=[(None, '---'),('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], coerce=str)
    answers = [(None, '---'), ('Very poorly', 'Very poorly'), ('Poorly', 'Poorly'), ('Moderately', 'Moderately'),
               ('Well', 'Well'),
               ('Very well', 'Very well')]

    performance = SelectField('<h3>About the teamwork</h3>How well, in your opinion, did your team perform?',
                              choices=answers, coerce=str)
    cohesion = SelectField('How cohesive was your team?',
                           choices=answers, coerce=str)
    communication = SelectField('How well did your team communicate?',
                                choices=answers, coerce=str)
    balance = SelectField('Did both members of your team contribute equally in your opinion?',
                          choices=[(None, '---'), ('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], coerce=str)
    balance_extra = SelectField(_l('If not, who contributed more?'), choices=[(None, '---'), ('Myself', 'Myself'), ('Teammate', 'My teammate')], coerce=str)

    satisfaction = SelectField('Would you play with the same teammate again?',
                               choices=[(None, '---'), ('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], coerce=str)
    comments = TextAreaField(_l('Any comments about the game?'), validators=[
        Optional(), Length(min=1, max=30)])
    likert_scale = [(None, '---'), ('Very Low', '1. Disagree Strongly'), ('Low', '2. Disagree a Little'), \
                    ('Moderate', '3. Neither Agree nor Disagree'), ('Good', '4. Agree a Little'), \
                    ('High', '5. Agree Strongly')]
    reversed_likert_scale =[(None, '---'), ('High', '1. Disagree Strongly'), ('Good', '2. Disagree a Little'), \
                 ('Moderate', '3. Neither Agree nor Disagree'), ('Low', '4. Agree a Little'), \
                 ('Very Low', '5. Agree Strongly')]

    enthusiasm = SelectField('<h3>How do you see yourself as: </h3>Extraverted, enthusiastic', choices=likert_scale, coerce=str)
    critical = SelectField('Critical, quarrelsome', choices=reversed_likert_scale,
                             coerce=str)
    dependable = SelectField('Dependable, self-disciplined', choices=likert_scale,
                             coerce=str)
    anxious = SelectField('Anxious, easily upset', choices=reversed_likert_scale,
                           coerce=str)
    complex = SelectField('Open to new experiences, complex', choices=likert_scale,
                             coerce=str)
    reserved = SelectField('Reserved, quiet', choices=reversed_likert_scale,
                          coerce=str)

    warm = SelectField('Sympathetic, warm', choices=likert_scale,
                          coerce=str)
    careless = SelectField('Disorganised, careless', choices=reversed_likert_scale,
                           coerce=str)
    calm = SelectField('Calm, emotionally stable', choices=likert_scale,
                       coerce=str)
    uncreative = SelectField('Conventional, uncreative', choices=reversed_likert_scale,
                           coerce=str)
    improve = TextAreaField(_l('<h3>About the task</h3>What would you improve about the game?'), validators=[
        Optional(), Length(min=1, max=30)])

    keep = TextAreaField(_l('What would you keep the same?'), validators=[
        Optional(), Length(min=1, max=30)])

    other = TextAreaField(_l('Any other comments?'), validators=[
        Optional(), Length(min=1, max=30)])

    submit = SubmitField(render_kw={'id': 'code', "type": "submit", "value": "Submit"})


class ChatForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[
        Optional()])
    room = StringField('Room', validators=[
        Optional()])
    submit = SubmitField('Enter the Maze', render_kw={'id' :'maze'})





class TextForm(FlaskForm):
    text_area = TextAreaField(_l('<p>chat history (do not type here) </p>'), validators=[
        DataRequired(), Length(min=10, max=60)], render_kw={'id': 'explore', 'class': 'form-control', 'rows': 7,
                                                            'placeholder': ''})

    text = TextAreaField(_l('<h4 style="color: blue;"><strong>Enter your message below:</strong></h4>'), validators=[
        DataRequired(), Length(min=1, max=30)], render_kw={'id': 'text', 'placeholder': 'write to your teammate here'})
    submit = SubmitField(render_kw={"style": "display: none"})
