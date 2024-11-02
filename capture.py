from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/capture', methods=['POST'])
def capture_data():
    data = request.get_json()
    print("Received data:", json.dumps(data, indent=4))
    with open("captured_data.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
    return "Data received successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
