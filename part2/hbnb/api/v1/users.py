from flask import request
from flask_restx import Namespace, Resource, fields
from models.user import User

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

users_db = [] 
@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.json
        new_user = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
        users_db.append(new_user)
        return new_user.to_dict(), 201

    def get(self):
        return [user.to_dict() for user in users_db], 200