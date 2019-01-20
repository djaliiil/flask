from .. import db




class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64))
    blood_type = db.Column(db.String(64))
    dateofbirth = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('profiles', lazy=True))

#rec
#dateofbirth
#immunization
     

    def __repr__(self):
        return '<Profile \'%s\'>' % self.firstname

 
