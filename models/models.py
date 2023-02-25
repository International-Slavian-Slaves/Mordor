from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Guitar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    brand = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Integer)
