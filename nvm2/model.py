from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# GCP
CLOUDSQL_USER = 'postgres'
CLOUDSQL_PASSWORD = '123456'
CLOUDSQL_DATABASE = 'test2'
CLOUDSQL_CONNECTION_NAME = 'tunnel-insight:asia-southeast1:tbm-instance'

LOCAL_SQLALCHEMY_DATABASE_URI = (
    'postgres+psycopg2://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

SQLALCHEMY_DATABASE_URI = (
    'postgres+psycopg2://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

'''
admin = User(username='admin4', email='admin4@example.com')
guest = User(username='guest4', email='guest4@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
'''

data = User.query.all()
print(data[1].username)