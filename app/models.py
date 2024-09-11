from flask import  url_for
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    image = db.Column(db.String(250))
    creator_id = db.Column(db.Integer, db.ForeignKey('creators.id'), nullable=True)
    # date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __str__(self):
        return self.title

    # @property
    # def image_url(self):
    # return url_for('static', filename=f"images/{self.image}")

    @property
    def image_url(self):
        return url_for('static', filename=f"/images/{self.image}")

    @property
    def show_url(self):
        return url_for('posts.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('posts.delete', id=self.id)


class Creator(db.Model):
    __tablename__ = 'creators'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # define relation in model
    posts= db.relationship('Post', backref='creator')
    
    def __str__(self):
        return self.title

    @property
    def show_url(self):
        return url_for('creators.show', id=self.id)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)