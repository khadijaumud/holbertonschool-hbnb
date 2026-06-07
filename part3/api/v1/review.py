@reviews_bp.route('/', methods=['POST'])
@jwt_required()
def create_review():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    place_id = data.get('place_id')
    
    place = facade.get_place(place_id)
    if place.owner_id == current_user_id:
        return jsonify({"msg": "You cannot review your own location"}), 400
        
    # Dublikat yoxlanışı
    existing_review = facade.get_review_by_user_and_place(current_user_id, place_id)
    if existing_review:
        return jsonify({"msg": "You have already reviewed this location"}), 400
        
    new_review = facade.create_review(data, user_id=current_user_id)
    return jsonify({"id": new_review.id, "message": "Review added successfully"}), 201