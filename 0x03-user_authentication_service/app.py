#!/usr/bin/env python3

from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """
    Route to return a JSON payload
    """

    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def register_user():
    """
    Endpoint to register a user
    """
    email = request.form.get("email")
    password = request.form.get("password")


    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message" : "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
