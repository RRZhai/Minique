# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from server.models.users import db

# Import models here
from server.models.users import User
from server.models.lists import List
from server.models.tasks import Task
from server.models.achievements import Achievement
from server.models.follows import Follow

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
