from .. import db




class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64))
    #type
    title = db.Column(db.String(64))
    date = db.Column(db.String(64))
    #doctor = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
     
#rec
#dateofbirth
#immunization
     

    def __repr__(self):
        return '<Event \'%s\'>' % self.location

 
