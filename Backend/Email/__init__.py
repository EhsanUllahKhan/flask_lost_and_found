from flask import Blueprint

Email = Blueprint('Email', __name__)

from Backend.Email import api_email