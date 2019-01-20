from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField,SubmitField
from wtforms.validators import DataRequired, NumberRange


class AddDiagosisForm(Form):
    symptoms = StringField('symptoms', [validators.Length(min=6, max=35)])
    recomendations = StringField('recomendations',[validators.Length(min=6, max=35)])

    submit = SubmitField('update history')

 
class SearchForm(Form):
    q = StringField('Search terms', validators=[DataRequired()])
    submit = SubmitField('Search plant')


class DoctorDetail(Form):
	"""
	qulification
	hospital_id
	bio
	"""

pass    



