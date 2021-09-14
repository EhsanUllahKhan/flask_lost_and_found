from Backend.User import User as user_routes
from Backend.Models.User_model import User as UserModel
from flask import request, Response, jsonify
import json
import app
from Backend.User.schema_user import *
from Backend.validate_json import validate_json
from Backend.common.celery_app import celery

@user_routes.route('/user', methods=['GET'])
def get_all_users():
    try:
        users = app.db.session.query(UserModel).all()
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
    task_name = "create_user_task"
    task = celery.send_task(task_name, args=[data['email']])

    return dict(
            id=task.id,
            url='http://0.0.0.0:5000/task/{}'.format(task.id)
        )


@user_routes.route('/user/<email>', methods=['DELETE'])
def delete_user(email):
    try:
        _user = app.db.session.query(UserModel).filter(UserModel.email == email).first()
        app.db.session.delete(_user)
        app.db.session.commit()
        return {'status': 202}
    except:
        return {'error': "Email not found", 'status': 404}

