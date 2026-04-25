from flask_restx import Namespace, Resource, fields
from services.facade import facade

api = Namespace('places', description='Place operations')
model = api.model('Place', {
    'title': fields.String(required=True),
    'price': fields.Float(required=True),
    'owner_id': fields.String(required=True)
})

@api.route('/')
class PlaceList(Resource):
    def get(self): return [{'id': p.id, 'title': p.title} for p in list(facade.place_repo.values())]
    @api.expect(model)
    def post(self):
        p = facade.create_place(api.payload)
        return {'id': p.id, 'title': p.title}, 201