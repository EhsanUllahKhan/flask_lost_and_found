from Backend.User import User as user_routes
from Backend.Models.User_model import User as UserModel
from flask import request, Response, jsonify
import json
# from Backend import db
from app import db
from Backend.User.schema_user import *
from Backend.validate_json import validate_json

@user_routes.route('/user', methods=['GET'])
def get_all_users():
    try:
        users = db.session.query(UserModel).all()
        if not users:
            return Response(status=204)

        users_list = list()
        for user in users:
            users_list.append(user.to_json())
        return Response(json.dumps(users_list), mimetype='application/json')
    except:
        return {'error': "Something went wrong", 'status': 404}

@user_routes.route('/user', methods=['POST'])
@validate_json(user_create_schema)
def new_user():
    data = request.get_json(force=True)
    try:
        _user = db.session.query(UserModel).filter(UserModel.email == data['email']).first()
        if _user:
            return {'status': 400}

        user = UserModel(
            email = data['email']
        )
        db.session.add(user)
        db.session.commit()
        return {'status': 201}
    except:
        return {'error': "Something went wrong", 'status': 404}

@user_routes.route('/user/<email>', methods=['DELETE'])
def delete_user(email):
    try:
        _user = db.session.query(UserModel).filter(UserModel.email == email).first()
        db.session.delete(_user)
        db.session.commit()
        return {'status': 202}
    except:
        return {'error': "Email not found", 'status': 404}

