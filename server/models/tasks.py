from __init__ import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False, unique=False)
    info = db.Column(db.String, nullable=False, unique=False)
    completed = db.Column(db.Boolean, nullable=False, unique=False)
    repeat = db.Column(db.Boolean, nullable=False, unique=False)
    repeat_interval = db.Column(db.Integer, nullable=False, unique=False)
    list = db.relationship('List', back_populates='tasks')