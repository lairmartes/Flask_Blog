from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'q2ep$25Swyct(H@kF9P2hrdKoXBT(Iy1MAZHFWWAM(M)9VNXiO6GY5$i443CM!SI'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flaskblog import routes
