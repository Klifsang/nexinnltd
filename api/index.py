# api/index.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'greetings': 'Hello, World!'})

@app.route('/about')
def about():
    return jsonify({'message': 'About page'})
