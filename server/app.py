# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from server.models.users import User
from server.models.lists import List
from server.models.tasks import Task
from server.models.achievements import Achievement
from server.models.follows import Follow

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'



if __name__ == '__main__':
    app.run(port=5555, debug=True)

