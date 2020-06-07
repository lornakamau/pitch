from flask_wtf import FlaskForm 
from wtforms import SubmitField,TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_content = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')