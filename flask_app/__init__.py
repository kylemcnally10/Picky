# __init__.py
from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhh"

DATABASE = "restaurant_picker"

bcrypt = Bcrypt(app)
