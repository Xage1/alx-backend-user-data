#!/usr/bin/env python3

from flask import Flask, request, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome() -> str:
    """
    Route to return a JSON payload
    """

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """Endpoint to register a user"""

    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError as error:
        if "already exists" in str(error):
            return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({"message": str(error)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
