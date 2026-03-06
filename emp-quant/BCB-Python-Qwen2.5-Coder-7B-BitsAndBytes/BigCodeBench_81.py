
from flask import Flask
from flask_restful import Resource, Api
import requests

def task_func(api_url, template_folder):
    # Create a Flask application instance
    app = Flask(__name__, template_folder=template_folder)
    
    # Create an API instance
    api = Api(app)
    
    # Define a resource class for the API endpoint
    class ExternalData(Resource):
        def get(self):
            try:
                # Fetch data from the external API
                response = requests.get(api_url)
                response.raise_for_status()  # Raise an exception for HTTP errors
                return response.json()
            except requests.exceptions.RequestException as e:
                return {'error': str(e)}, 500
    
    # Add the resource to the API
    api.add_resource(ExternalData, '/data')
    
    return app