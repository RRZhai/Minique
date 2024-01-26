from __init__ import db, relationship

class List(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=False)
    title = db.Column(db.String, nullable=False, unique=False, default='Untitled List')
    tasks = relationship('Task', back_populates='list', cascade='all, delete-orphan')
    def __repr__(self):
        return f'<List {self.title}>:\n' + f'\tUser ID: {self.user_id}\n' + f'\tTasks: {self.tasks}\n'