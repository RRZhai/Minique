from __init__ import db, re, validates, relationship

class Achievement(db.Model):
    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=False)
    name = db.Column(db.String, nullable=False, unique=False)
    description = db.Column(db.String, nullable=False, unique=False)
    user = relationship('User', back_populates='achievements')
    def __repr__(self):
        return f'<Achievement {self.name}>:\n' + f'\tUser ID: {self.user_id}\n' + f'\tDescription: {self.description}\n'