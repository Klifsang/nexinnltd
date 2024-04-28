from flask import Flask, jsonify, send_from_directory
from databaseconfig import db
from endpoints.client_api import clients
from endpoints.tickets_api import tickets
from endpoints.admin_api import admin
from endpoints.auth_api import login, logout


app = Flask(__name__, static_folder='../client/dist', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/about')
def about():
    return jsonify({'about': 'about me info here'})



