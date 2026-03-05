from flask import Flask
from flask_restful import Resource, Api
import requests
def task_func(api_url, template_folder):
    app = Flask(__name__, template_folder=template_folder)
    api = Api(app)

    class ExternalAPIData(Resource):
        def get(self):
            response = requests.get(api_url)
            return response.json()

    api.add_resource(ExternalAPIData, '/data')

    return app