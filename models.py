import hashlib
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.String(100), nullable=True)
    task_status = db.Column(db.Boolean, default=False)

class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password



