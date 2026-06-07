from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

places_bp = Blueprint('places', __name__, url_prefix='/api/v1/places')

@places_bp.route('/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    current_user_id = get_jwt_identity()
    place = facade.get_place(place_id)
    
    if not place:
        return jsonify({"msg": "Location not found"}), 404
        
    if place.owner_id != current_user_id:
        return jsonify({"msg": "Operation not permitted"}), 403
        
    data = request.get_json()
    updated_place = facade.update_place(place_id, data)
    return jsonify({"msg": "Location updated successfully"}), 200