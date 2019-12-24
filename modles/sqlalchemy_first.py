from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sqlalchemy_first = Flask(__name__)

sqlalchemy_first.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///E:/data.db'
# sqlalchemy_first.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(sqlalchemy_first)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	users = db.relationship('User', backref='role')

	def __repr__(self):
		return '<Role %r>' % self.name


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username


