from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='../client/dist', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')
@app.route('/api/')
def index():
    return jsonify({'greetings': 'Hello, World!'})

@app.route('/api/about')
def about():
    return jsonify({'message': 'About page'})
