from .. import db



class Hospital(db.Model):
    __tablename__ = 'hospitals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    county = db.Column(db.String(64))
    description = db.Column(db.String(300))
    location = db.Column(db.String(64))# to add longitiude latitude
    """
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)  
    doctor = db.relationship('Doctor', backref=db.backref('hospitals', lazy=True))
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    medication = db.relationship('Medication', backref=db.backref('hospitals', lazy=True))
"""




    def __repr__(self):
        return '<Hospital \'%s\'>' % self.name
    

class Medication(db.Model):
	__tablename__ = 'medication'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	quantity = db.Column(db.Integer, default=0)


	def __repr__(self):
		return '<Medication \'%s\'>' % self.firstname

 
