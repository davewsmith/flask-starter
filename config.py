import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', default="top sekret dev key")
    SQLALCHEMY_DATABASE_URI = "sqlite:////data/app.db"
