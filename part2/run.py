import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'hbnb')))

from flask import Flask
from flask_restx import Api
from api.v1.users import api as users_ns
from api.v1.amenities import api as amenities_ns
from api.v1.places import api as places_ns

app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API', description='Full HBnB Backend')

api.add_namespace(users_ns, path='/api/v1/users')
api.add_namespace(amenities_ns, path='/api/v1/amenities')
api.add_namespace(places_ns, path='/api/v1/places')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)