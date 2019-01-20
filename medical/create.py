from app import  db
from app.models.user import Role, User
from app.models.event import Event
 
 

wam="austin"
 
   
db.drop_all()
db.create_all()
db.session.commit()
 
Role.insert_roles()

user = User(username='Admin', fullname='Account', password="123456",email='austinwam',  role_id=3)
user1 = User(username='admin1', fullname='Account', password="123456",email='austinwam3',  role_id=3)
user2 = User(username='Admin2', fullname='Account', password="123456",email='austinwam4',  role_id=3)
user3 = User(username='doc', fullname='Account', password="123456",email='austinwam1',  role_id=2)
user4 = User(username='doc1', fullname='Account', password="123456",email='austinwam2',  role_id=2)
event = Event(location='othaya',title='immunatioztion', date='1241993',)
db.session.add(user)
db.session.add(user1)
db.session.add(user2)
db.session.add(user4)
db.session.add(user3)
db.session.add(event)


db.session.commit()
print('Added administrator')
print('Added administrator')
print('Added doc')


 
