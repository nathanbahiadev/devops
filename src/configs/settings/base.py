from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
