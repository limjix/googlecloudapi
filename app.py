from model import app, User
from flask import Flask,jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/data', methods=['GET'])
def getdata():
    # Access the identity of the current user with get_jwt_identity
    data = User.query.all()

    for item in data:
        output= {}
        output["id"] = item.id
        output["username"] = item.username
        output["email"] = item.email
        print(output)
    return jsonify(data = output), 200

if __name__ == "__main__":
    app.run()