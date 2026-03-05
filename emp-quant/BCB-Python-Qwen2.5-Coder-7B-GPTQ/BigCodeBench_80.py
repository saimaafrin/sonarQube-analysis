from flask import Flask, render_template, request
import json
import logging
def task_func(template_folder):
    app = Flask(__name__, template_folder=template_folder)

    @app.route('/', methods=['POST'])
    def handle_post():
        request_data = request.get_json()
        logging.info(json.dumps(request_data))
        return render_template('index.html', data=request_data)

    return app