from secondapi.model import app, User, db
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

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

@app.route('/data', methods=['POST'])
def setdata():
    # Access the identity of the current user with get_jwt_identity
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    print(username,email)
    newuser = User(username=username, email=email)

    db.session.add(newuser)
    db.session.commit()

    return jsonify(item1 = username,item2 = email)

@app.route('/helloworld', methods=['GET'])
def helloworld():

    return "HELLO WORLD"

if __name__ == '__main__':
    app.run()