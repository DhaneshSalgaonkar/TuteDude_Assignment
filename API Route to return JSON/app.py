from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from a file
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

@app.route("/api")
def api_route():
    data = load_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)