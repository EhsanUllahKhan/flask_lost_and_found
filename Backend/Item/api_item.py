import datetime

from Backend.Item import Item as item_routes
from Backend.Models.Item_model import Item as ItemModel
from flask import request, Response, jsonify
import json
from datetime import datetime
# from Backend import db
import app


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
def new_item():
    data = request.get_json(force=True)
    try:
        item = ItemModel(
            name = data['name'],
            is_found = False,
            lost_date = datetime.today().date(),
            lost_by_user_id = data['lost_by_user_id'],
            found_by_user_id = None
        )
        app.db.session.add(item)
        app.db.session.commit()
        return {'status': 201}
    except:
        return {'error': "Something went wrong", 'status': 404}

@item_routes.route('/item/<lost_item_id>', methods=['DELETE'])
def delete_item(lost_item_id):
    try:
        _item = app.db.session.query(ItemModel).filter(ItemModel.lost_item_id == lost_item_id).first()
        if not _item:
            return Response(status=400)
        app.db.session.delete(_item)
        app.db.session.commit()
        return {'status': 202}
    except:
        return {'error': "Item not found", 'status': 404}

@item_routes.route('/item/found/<lost_item_id>/<found_by_user_id>', methods=['PATCH'])
def found_item(lost_item_id, found_by_user_id):
    try:
        _item = app.db.session.query(ItemModel).filter(ItemModel.lost_item_id == lost_item_id).first()
        if not _item:
            return Response(status=400)

        _item.is_found = True
        _item.found_by_user_id = found_by_user_id
        app.db.session.commit()
        return {'status': 203}
    except:
        return {'error': "Something went wrong", 'status': 404}

