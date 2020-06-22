# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class query_form(FlaskForm):
    query = StringField('Search for a value in column a:', validators=[DataRequired()])
    submit = SubmitField('Search')


