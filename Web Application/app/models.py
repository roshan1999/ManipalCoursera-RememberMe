from app import db, login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	public_id = db.Column(db.String(50),unique = True)
	username = db.Column(db.String(50),unique = True)
	name = db.Column(db.String(50))
	password = db.Column(db.String(50))
	admin = db.Column(db.Boolean)
	email = db.Column(db.String(50))

	def __repr__(self):
		return '<User {}>'.format(self.username)
	def set_password(self,password):
		self.password = generate_password_hash(password)
	def check_password(self,password):
		return check_password_hash(self.password,password)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Socials(UserMixin,db.Model):
	userid = db.Column(db.String(50), primary_key = True)
	weburl = db.Column(db.String(200))
	name = db.Column(db.String(20), primary_key = True)
	eid = db.Column(db.Integer)
	key = db.Column(db.String(50))

	def __repr__(self):
		return '{}  {}'.format(self.name,self.weburl)

class Encrypt(UserMixin, db.Model):
	userid = db.Column(db.String(50), primary_key = True)
	name = db.Column(db.String(20), primary_key =True)
	key  = db.Column(db.BLOB(50))

	def __repr__(self):
		return self.key;
