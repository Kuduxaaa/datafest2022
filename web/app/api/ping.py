from flask_restful import Resource
from flask import jsonify

class Ping(Resource):
    def get(self):
        return jsonify({
            'message': 'pong'
        })