from .. import db




class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    sirname = db.Column(db.String(64))
    location = db.Column(db.String(64))
    #qulification what kind
    

    #kind eg profestion
    #bio
    #
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'),
        nullable=False)
    hospital = db.relationship('Hostipal',
        backref=db.backref('hospitals', lazy=True))
   # hospital = db.relationship('Hostipal', backref='hospitals', lazy='dynamic')


    def __repr__(self):
        return '<Doctor \'%s\'>' % self.firstname
