import sqlalchemy as db
import os

SECRET_KEY = os.urandom (256)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# GCP
CLOUDSQL_USER = 'postgres'
CLOUDSQL_PASSWORD = '123456'
CLOUDSQL_DATABASE = 'test'
CLOUDSQL_CONNECTION_NAME = 'tunnel-insight:asia-southeast1:tbm-instance'

LOCAL_SQLALCHEMY_DATABASE_URI = (
    'postgres+psycopg2://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

# Step 1: Create the Engine
engine = db.create_engine(LOCAL_SQLALCHEMY_DATABASE_URI, echo = True)

# Step 2: Connect
connection = engine.connect()

# Step 3: Create Metadata
meta = db.MetaData()

# Step 4: Set the Schema
students = db.Table(
   'students', meta,
   db.Column('id', db.Integer, primary_key = True),
   db.Column('name', db.String),
   db.Column('lastname', db.String),
)

# Optional: Create engine if engine hasn't existed. Once schema created, it can't be recreated
meta.create_all(engine)




