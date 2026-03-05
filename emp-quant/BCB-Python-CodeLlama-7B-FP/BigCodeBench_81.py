from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests
def task_func(api_url, template_folder):
    app = Flask(__name__)
    api = Api(app)

    class MyResource(Resource):
        def get(self):
            response = requests.get(api_url)
            return jsonify(response.json())

    api.add_resource(MyResource, '/')
    return app