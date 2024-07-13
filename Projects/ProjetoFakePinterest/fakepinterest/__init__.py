from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database = SQLAlchemy(app)

from fakepinterest import routes  
