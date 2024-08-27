from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional

# form for adding control
class ControlForm(FlaskForm):
    name = StringField('Control Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    status = SelectField('Status', choices=[('active', 'Active'), ('inactive', 'Inactive')], validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', default=datetime.today, validators=[DataRequired()])
    submit = SubmitField('Add Control')

# form for visualization
class FilterForm(FlaskForm):
    criteria = SelectField('Select Criteria', choices=[('rating', 'Rating'), ('status', 'Status'), ('date', 'Date')], validators=[DataRequired()])
    # fields in case user wants to filter by date range
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[Optional()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Generate')