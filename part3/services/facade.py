from app.models.user import User
from app.persistence.user_repository import UserRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        
    def create_user(self, user_data):
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            password=user_data['password']
        )
        return self.user_repo.add(user)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)