from flask import Blueprint

Item = Blueprint('Item', __name__)

from Backend.Item import api_item