from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services import facade

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = facade.authenticate_user(email, password)
    if not user:
        return jsonify({"msg": "Wrong email or password"}), 401

    access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
    return jsonify(access_token=access_token), 200


def admin_required():
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if not claims.get("is_admin", False):
                return jsonify({"msg": "Yalnız administratorlar daxil ola bilər"}), 403
            return fn(*args, **kwargs)
        decorator.__name__ = fn.__name__
        return decorator
    return wrapper