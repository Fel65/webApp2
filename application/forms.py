from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import Chore

class ChoreForm(FlaskForm):
    
    #id = db.Column(db.Integer, primary_key=True)
    charge = StringField('Enter the charge')
    job_done = StringField('Is it complete')
    house_id = StringField('House details(*)', validators=[DataRequired()])
    chore_description = StringField("Chore Description", validators=[DataRequired()])
    submit = SubmitField("Add Chore")
    #CRUD Functionality is excuted here
    def validate_task(self, chore):
        chore = Chore.query.all()
        for chore in chores:
            if chore.task == chore.data:
                raise ValidationError('You already added this chore')

job_status =[
            ("complete", "Completed"),
            ("id", "Recent"),
            ("old", "Old"),
            ('incomplete', "Incomplete")
        ]

#

