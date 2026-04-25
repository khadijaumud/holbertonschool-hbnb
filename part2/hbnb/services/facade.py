from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = {}
        self.amenity_repo = {}
        self.place_repo = {}
        self.review_repo = {}

    # User
    def create_user(self, data):
        user = User(**data)
        self.user_repo[user.id] = user
        return user

    def get_all_users(self):
        return list(self.user_repo.values())

    # Amenity
    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenity_repo[amenity.id] = amenity
        return amenity

    def get_all_amenities(self):
        return list(self.amenity_repo.values())

    # Place
    def create_place(self, data):
        place = Place(**data)
        self.place_repo[place.id] = place
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    # Review
    def create_review(self, data):
        review = Review(**data)
        self.review_repo[review.id] = review
        place = self.get_place(data['place_id'])
        if place: place.reviews.append(review)
        return review

facade = HBnBFacade()
