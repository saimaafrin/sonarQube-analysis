from flask import Flask, render_template, request
import json
import logging
def task_func(template_folder):
    app = Flask(__name__)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["TEMPLATES_FOLDER"] = template_folder

    @app.route("/", methods=["POST"])
    def index():
        data = request.get_json()
        logging.info(json.dumps(data))
        return render_template("index.html", data=data)

    return app