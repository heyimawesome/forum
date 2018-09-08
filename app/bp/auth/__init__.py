from flask import Blueprint

bp = Blueprint('u', __name__)

from app.bp.auth import routes
