from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from app.models.user import User 

 

class UserRegister(Resource):

    userparse = reqparse.RequestParser()
    userparse.add_argument('email',type=str, required=True, help="This field cannot be blank." )
    userparse.add_argument('phone', type=str,  required=True, help="This field cannot be blank.")
    userparse.add_argument('password', type=str,  required=True, help="This field cannot be blank.")

    def post(self):
        data = self.userparse.parse_args()

        if User.find_by_emails(data['email']):
            return "0", 400

        if User.find_by_phonenu(data['phone']):
            return "0", 400    

        #user = User(data['email'], data['password'], data['phone'])
        print(data)
        user=User(**data)
        user.save_to_db()

        return {}, 201


class UserLogin(Resource):
    login1= reqparse.RequestParser()
    login1.add_argument('email',type=str, required=True, help="This field cannot be blank." )
    login1.add_argument('password', type=str,  required=True, help="This field cannot be blank.")
    def post(self):
        data = self.login1.parse_args()
        print(data['email'])
        print(data['password'])

        user = User.find_by_emails(data['email'])
        print(user)

        if user and (user.password, data['password']):
            return  {}, 200

        return {"0"}, 401


 

class User(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """
    @classmethod
    def get(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200


