import os
SECRET_KEY = os.urandom (256)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# GCP
CLOUDSQL_USER = 'postgres'
CLOUDSQL_PASSWORD = '123456'
CLOUDSQL_DATABASE = ''
CLOUDSQL_CONNECTION_NAME = ''

SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)
