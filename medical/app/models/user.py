from .. import db 
#from app import db 
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
 

class Permission:
    VIEW = 0x01
    WRITE_DIAGNOSIS = 0x02
    ADMINISTER = 0x04
    #ADMINISTER = 0x08
  

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    # relationship
    users = db.relationship('User', backref='role', lazy='dynamic')

    @classmethod
    def insert_roles(cls):
        roles = {
            'User': (Permission.VIEW ,True),
            'Doctor': (Permission.WRITE_DIAGNOSIS,False),
            'Administrator': (0xff, False)
        }
        for role_name in roles.keys():
            role = cls.query.filter_by(name=role_name).first()
            if role is None:
                print('Role: add %s' % role_name)
                role = cls(name=role_name)
            role.permissions = roles[role_name][0]
            role.default = roles[role_name][1]
            db.session.add(role)
        db.session.commit()
        print('Insert roles is done.')

    def __repr__(self):
        return '<Role %r>' % self.name




class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=False)
    password=db.Column(db.String(80))
    email=db.Column(db.String(80),unique=False)
    phone=db.Column(db.String(20),unique=False)
    active = db.Column(db.Boolean, default=True)
    fullname=db.Column(db.String(80))
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_ip = db.Column(db.String(45))
    authenticated = db.Column(db.Boolean, default=False)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    current_logged_in = db.Column(db.DateTime, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))



    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions


  
 




    @property 
    def is_administrator(self): 
        return self.can(Permission.ADMINISTER)


        def __repr__(self):
            return '<User %r - %s>' % (self.username, self.role.name)





    