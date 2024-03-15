from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    task_description = db.Column(db.String(100), nullable=True)
    task_status = db.Column(db.Boolean, default=False)


