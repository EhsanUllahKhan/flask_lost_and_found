from flask import Blueprint

User = Blueprint('User', __name__)

from Backend.User import api_user