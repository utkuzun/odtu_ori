
from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user

class Test(Resource):
    @jwt_required()
    def get(self):

        responseObject = {
            "username": current_user.first_name,
            "email" : current_user.last_name
        }

        return responseObject, 200











