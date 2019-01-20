from flask import Blueprint, render_template
from app.models import Hospital#PatientPrifile
 
 

hospital = Blueprint('hospital', __name__)


@hospital.route('/hospital')
def index():
	hosp = Hospital.query.all
    return render_template('hospital/index.html', hosp=hosp)


 
@hospital.route('/hospital/<int:hospital_id>',methods=['GET'])
def hospitaldetail(hospital_id):
	hospital = Hospital.query.filter_by(id=_id).first()
	return render_template('hospital/index.html', hospital=hospital)
 


 