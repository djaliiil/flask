from .. import db



class Diaganosis(db.Model):
    __tablename__ = 'diaganosis'
    id = db.Column(db.Integer, primary_key=True)
    symptoms = db.Column(db.String(300))
    recomendations = db.Column(db.String(300))
    #medication
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('diaganosis', lazy=True))



    def __repr__(self):
        return '<Diaganosis %r>' % self.symptoms

 
#
class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    #recomendations = db.Column(db.String(300))
    #medication
    #Datetime
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('appointments', lazy=True))

    def __repr__(self):
        return '<Appointment %r>' % self.name

