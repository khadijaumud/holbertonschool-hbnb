import uuid
from datetime import datetime

class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()