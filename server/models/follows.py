from __init__ import db, validates, re, validates, relationship

class Follow(db.Model):
    __tablename__ = 'followers'
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())

    follower = relationship('User', foreign_keys=[follower_id], back_populates='followed_users', lazy='joined')
    followed = relationship('User', foreign_keys=[followed_id], back_populates='followers', lazy='joined')

