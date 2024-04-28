# api/index.py
# from flask import Flask, jsonify

# app = Flask(__name__)



from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='client/build', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')












# @app.route('/')
# def home():
#     return jsonify({'greetings': 'Hello, World!'})

# @app.route('/about')
# def about():
#     return jsonify({'message': 'About page'})
