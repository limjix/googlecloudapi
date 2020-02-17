from model import app
from flask import Flask,jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()