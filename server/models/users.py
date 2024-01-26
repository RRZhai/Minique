from __init__ import db, validates, re, validates, relationship
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=False)
    profile_image_url = db.Column(db.String, nullable=True, unique=False)
    followed = relationship('User', secondary='followers', primaryjoin='User.id == Follow.follower_id', secondaryjoin='User.id == Follow.followed_id', back_populates='followers', lazy='dynamic')
    tasks = relationship('Task', back_populates='user', cascade='all, delete-orphan')
    achievements = relationship('Achievement', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>:\n' + f'\tEmail: {self.email}\n' + f'\tProfile Image URL: {self.profile_image_url}\n' + f'\tTasks: {self.tasks}\n' + f'\tAchievements: {self.achievements}\n'
    
    @property
    def password(self):
        raise AttributeError('Password is not readable.')
    
    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)
    
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            raise ValueError('Invalid email address.')
        return email
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
    
    def is_following(self, user):
        return self.followed.filter(Follow.followed_id == user.id).count() > 0