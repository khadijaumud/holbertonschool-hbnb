from flask_restx import Namespace, Resource, fields
from services.facade import facade

api = Namespace('amenities', description='Amenity operations')
model = api.model('Amenity', {'name': fields.String(required=True)})

@api.route('/')
class AmenityList(Resource):
    def get(self): return [{'id': a.id, 'name': a.name} for a in facade.get_all_amenities()]
    @api.expect(model)
    def post(self):
        new_obj = facade.create_amenity(api.payload)
        return {'id': new_obj.id, 'name': new_obj.name}, 201