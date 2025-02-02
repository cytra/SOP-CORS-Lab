from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/data')
def no_cors_data():
    return jsonify({"message": "This is a same-origin request!"})

@app.route('/cors-data')
def cors_data():
    return jsonify({"message": "This request is allowed via CORS!"})

if __name__ == '__main__':
    app.run(port=5000)
