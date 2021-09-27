import os 
import datetime
basedir = os.path.abspath(os.path.dirname(__file__))

database_name = os.getenv("DATABASE_NAME")
user_name=os.getenv("ROOT")
password=os.getenv("PASSWORD")


mysql_local_name = f"mysql://{user_name}:{password}@localhost/" + database_name


class BaseConfig():
    """ Base configiration """
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(hours=2)


class DevelopmentConfig(BaseConfig):
    """ Development configiration """
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = mysql_local_name




