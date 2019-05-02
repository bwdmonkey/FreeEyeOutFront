from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config.from_object('project.config.DevelopmentConfig')

class UsersResource(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'success msg'
        }

api.add_resource(UsersResource, '/users/test')
