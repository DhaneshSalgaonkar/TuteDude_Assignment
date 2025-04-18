from flask import Flask, request, render_template, redirect, url_for
import pymongo
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Get the MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = pymongo.MongoClient(mongo_uri)
db = client["database_names"]
collection = db["names"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_data():
    try:
        name = request.form["name"]
        collection.insert_one({"name": name})
        return redirect(url_for("success"))
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template("index.html", error=error_message)

@app.route("/success")
def success():
    return "<h1>Data submitted successfully</h1>"


if __name__ == "__main__":
    app.run(debug=True)