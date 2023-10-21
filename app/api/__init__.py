from flask import Blueprint,jsonify

api = Blueprint('api',__name__,url_prefix='/api')

from .resources import (
    usuario_resources,
    alumno_resources,
    colegio_resources
)

#from .models.colegio_models import Colegio

@api.route('/')
def index():
    context ={
        'message':'blueprint api'
    }
    return jsonify(context)