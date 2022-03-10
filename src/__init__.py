from flask import Flask, Blueprint, url_for
from flask_restful import Api

app = Flask(__name__, static_folder='static')
app.config['RESTFUL_JSON'] = {'ensure_ascii': False, 'encoding': 'utf-8'}
api_bp = Blueprint('api', __name__, url_prefix='/api')
app_view = Api(app)
api = Api(api_bp)

import src.routes.app
import src.routes.api

app.register_blueprint(api_bp)