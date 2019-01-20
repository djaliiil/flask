from app import application
 
from flask_login import LoginManager


login_manager = LoginManager(application)

login_manager.login_view = "account.login"

 

from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()





 



# Set up extensions

 
login_manager.init_app(application)

#
# run the app.
 
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.run(host='192.168.43.216', port=5000, debug=True)




if __name__ == '__main__': 
     application.run(host='0.0.0.0', port=8080)
  

