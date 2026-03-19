import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta_concesionario_2024')

    MYSQL_HOST = os.environ.get('MYSQLHOST')
    MYSQL_USER = os.environ.get('MYSQLUSER')
    MYSQL_PASSWORD = os.environ.get('MYSQLPASSWORD')
    MYSQL_DB = os.environ.get('MYSQL_DATABASE')
    MYSQL_PORT = int(os.environ.get('MYSQLPORT', 3306))

    MYSQL_CURSORCLASS = 'DictCursor'
