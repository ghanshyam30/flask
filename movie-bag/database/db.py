#db code goes here
from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)