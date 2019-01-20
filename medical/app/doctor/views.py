from flask import Blueprint, render_template, request,redirect,url_for
from app.models.user import User#PatientPrifile
from app.models.diaganosis import Diaganosis
from .forms import AddDiagosisForm, SearchForm
from app.decorators import permission_required, doctor_required
from .. import db 
from sqlalchemy.orm import joinedload

doctor = Blueprint('doctor', __name__)




@doctor.route('/',methods=['GET','POST'])
@doctor_required
def index():
    #event=Event.query.all()
    #doctor=Doctor.query.filter_by(username=username).first()
    search_form = SearchForm(request.form)
    if request.method == 'POST' and search_form.validate():
        search_query = '%'+(search_form.q.data)+'%' 
        search = User.query.filter(User.username.ilike(search_query)) 
        return render_template('doctor/doctor.html', search=search,form=search_form)
    return render_template('doctor/doctor.html',form=search_form)

@doctor.route('/<username>',methods=['GET'])
@doctor_required
def detail(username):
    profile = User.query.options(joinedload('profiles'))

    digs = User.query.options(joinedload('diaganosis'))
    for dig in digs:
        for profile in profile:
            return render_template('doctor/detail.html',  digs=dig, profile=profile)


 
 
 
@doctor.route('add/<username>',methods=['POST','GET'])
@doctor_required
def adddig(username):
    form = AddDiagosisForm(request.form)
    user = User.query.filter_by(username=username).first()
    if request.method == 'POST' and form.validate():
        dignosis = Diaganosis(symptoms=form.symptoms.data,recomendations=form.recomendations.data,user_id=user.id)
        #doctors field
        print(dignosis.recomendations)
        db.session.add(dignosis)
        db.session.commit()
        return redirect(url_for('doctor.index')) 

    return render_template('doctor/adddignosis.html', users=user,form=form)


 