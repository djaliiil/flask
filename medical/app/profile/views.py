from flask import Blueprint, render_template
from app.models.profile import Profile 
from flask import (request, redirect, url_for, render_template,
                   flash, current_app)
from app.models.user import Role, User
from flask_login import current_user, login_required
from app.decorators import patient_required
from app.models.user import User#PatientPrifile
from app.models.diaganosis import Diaganosis,Appointment 
from .. import db 
from sqlalchemy.orm import joinedload

patient = Blueprint('patient', __name__)


#test to add to admin
@patient.route('/')
def list():
	allp = Profile.query.all()
	print('12')
	print(allp)
	return render_template('patient/all.html')



#patient home page
@patient.route('/<username>',methods=['GET'])

def index(username): 
	digs = User.query.options(joinedload('diaganosis'))
	apo = User.query.options(joinedload('appointments'))
	profile = User.query.options(joinedload('profiles'))
	for dig in digs:
		for apo in apo:
			for profile in profile:
				return render_template('patient/profile.html', profile=profile, apos=apo,digs=dig)


#edit location to addmore

@patient.route('/rec')
def recomedation():
	rec=Diaganosis.query.filter_by(id=_id).first() 
	#apo=Appointment.query.filter_by(id=_id).first() 

	return render_template('patient/index.html',rec=rec)

#edit location to addmore phone
#@patient.route('/rec')
def edit(username):
    form = EditProfileForm(request.form)
    user = User.query.filter_by(username=username).first()
    if request.method == 'POST' and form.validate():
        profile = Profile(location=form.location.data)
        db.session.add(profile)
        db.session.commit() 
    return render_template('patient/edit.html', users=user,form=form  )

