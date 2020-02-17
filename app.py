from flask import Flask
from test2 import db,meta,connection, students

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisissecret"





if __name__ == "__main__":
    app.run()
