from flask_restful import Resource
from flask import jsonify

from app.service.police import Police

police = Police()

class Data(Resource):
    def get(self):
        return jsonify(police.getInfo())