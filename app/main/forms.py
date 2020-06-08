from flask_wtf import FlaskForm 
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    category = SelectField("What category are you submitting to?", choices=[("Twitter", "Twitter Pitches"), ( "Elevator", "Elevator Pitches"), ("Competitor", "Competitor Pitches"), ("Investor", "Investor Pitches")],validators=[Required()])
    pitch_content = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Add a comment',validators = [Required()] )
    submit = SubmitField('Submit')