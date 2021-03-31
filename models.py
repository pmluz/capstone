import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = "postgres://localhost:5432/casting_agency"
if not database_path:
    database_name = "casting_agency"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)
db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    print("db dropped successfully!")
    db.create_all()
    print("db created successfully!")


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    age = Column(Integer(), nullable=False)
    gender = Column(String(20), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True)
    release_date = Column(String(180), nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }
