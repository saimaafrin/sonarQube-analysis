
from flask import Flask, render_template, request
import json
import logging

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    logging.info(request.data)
    return render_template('index.html', data=request.data)

@app.route('/')
def root():
    return render_template('index.html')