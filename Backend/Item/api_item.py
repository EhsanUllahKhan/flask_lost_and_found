from Backend.Item.schema_item import *
from Backend.validate_json import validate_json

from Backend.Item import Item as item_routes
from Backend.Models.Item_model import Item as ItemModel
from flask import request, Response, jsonify
import json
import app
from Backend.common.celery_app import celery


@item_routes.route('/item', methods=['GET'])
def get_all_items():
    try:
        items = app.db.session.query(ItemModel).all()
        if not items:
            return Response(status=204)

        items_list = list()
        for item in items:
            items_list.append(item.to_json())
        return Response(json.dumps(items_list, indent=4, sort_keys=True, default=str), mimetype='application/json')
    except:
        return {'error': "Something went wrong", 'status': 404}

@item_routes.route('/item', methods=['POST'])
@validate_json(lost_item_create_schema)
def new_item():
    data = request.get_json(force=True)
    task_name = "create_item_task"
    task = celery.send_task(task_name, args=[data['name'], data['lost_by_user_id']])

    return dict(
        id=task.id,
        url='http://0.0.0.0:5000/task/{}'.format(task.id)
    )

@item_routes.route('/item/<lost_item_id>', methods=['DELETE'])
def delete_item(lost_item_id):
    task_name = "delete_item_task"
    task = celery.send_task(task_name, args=[lost_item_id])

    return dict(
        id=task.id,
        url='http://0.0.0.0:5000/task/{}'.format(task.id)
    )

@item_routes.route('/item/found/<lost_item_id>/<found_by_user_id>', methods=['PATCH'])
def found_item(lost_item_id, found_by_user_id):
    task_name = "found_item_task"
    task = celery.send_task(task_name, args=[lost_item_id, found_by_user_id])

    return dict(
        id=task.id,
        url='http://0.0.0.0:5000/task/{}'.format(task.id)
    )


