from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
#CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

@app.route('/data', methods=['GET'])
def data():
    return jsonify(message="Data Sent")

if __name__ == '__main__':
    app.run(port=5000)
