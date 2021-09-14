from flask import Blueprint

Task = Blueprint('Task', __name__)

from Backend.tasks import api_task