from flask import render_template, make_response
from flask_restful import Resource

class HomeController(Resource):

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def get(cls):

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)