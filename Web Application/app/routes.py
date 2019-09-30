from DES import des
from flask import render_template, redirect, flash, url_for, Flask, request, jsonify, flash
from app import app,db
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from app.models import User,Socials,Encrypt
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user

# Required for db creation ---
# TODO: Need to create validation to only create db when not already existing
db.create_all()

##--------------------- root/api/ for mobile application--------------------##
##--------------------- root/ for mobile application--------------------##

#encrpyt the user entered key
def encrpyt(data,plaintext):
	key = Encrypt.query.filter_by(userid = data["public_id"],name=data["name"]).first()
	if key is None:
		k,msg = des(key,plaintext)
		newEncrpyt = Encrypt(userid = data["public_id"],name= data["name"],key=k)
		db.session.add(newEncrpyt)
		db.session.commit()
	else:
		k,msg = des(key,plaintext)
	#copy to clipboard
	print(msg)

##----- For login page -------##
@app.route('/api/',methods = ['GET'])
def init():
	return jsonify({"message":"Welcome to Remember-me"})
@app.route('/', methods = ['GET','POST'])
def init_w():
    if current_user.is_authenticated:
        username = current_user.username
        return redirect(url_for('get_single_user_w', public_id = current_user.public_id))
    formReg = RegistrationForm(prefix='formReg')
    formLog = LoginForm(prefix='formLog')
    if formReg.validate_on_submit() and formReg.submit.data:
        public = str(uuid.uuid4())
        new_user = User(
		public_id = public,
		name = formReg.name.data,
		username = formReg.username.data,
		admin = False
		)
        new_user.set_password(formReg.password.data)
        db.session.add(new_user)
        db.session.commit()
        print('New user created')
        return redirect(url_for('get_single_user_w', public_id = public))
    if formLog.validate_on_submit() and formLog.submit.data:
        user = User.query.filter_by(username = formLog.username.data).first()
        if user is None or not user.check_password(formLog.password.data):
            flash('Invalid username or password')
            return redirect(url_for('init_w'))
        login_user(user, remember = formLog.remember_me.data)
        #print('Hello')
        print(user.public_id)
        return redirect(url_for('get_single_user_w', public_id = user.public_id))
    return render_template('login.html', form = formReg, form1 = formLog)

##----- For list of all users -------##
@app.route('/api/user',methods = ['GET'])
def get_all_user():
	data = User.query.all()
	alluserlst = list();
	print(data)
	for user in data:
		user_data = {}
		user_data['id'] = user.id
		user_data['public_id'] = user.public_id
		user_data['username'] = user.username
		user_data['name'] = user.name
		user_data['password'] = user.password
		user_data['admin'] = user.admin
		alluserlst.append(user_data)
	return jsonify({"users":alluserlst});

##----- For Home page of user -------##
@app.route('/api/user/<public_id>',methods = ['GET'])
def get_single_user(public_id):
	user = User.query.filter_by(public_id = public_id).first()
	if not user:
		return jsonify({"message":"No user found"})
	user_data = {}
	user_data['id'] = user.id
	user_data['public_id'] = user.public_id
	user_data['username'] = user.username
	user_data['name'] = user.name
	user_data['password'] = user.password
	user_data['admin'] = user.admin
	return jsonify({"user":user_data});
@app.route('/user/<public_id>',methods = ['GET','POST'])
@login_required
def get_single_user_w(public_id):
	user = User.query.filter_by(public_id = public_id).first_or_404()
	if not user:
		return jsonify({"message":"No user found"})
	user_data = {}
	user_data['id'] = user.id
	user_data['public_id'] = user.public_id
	user_data['username'] = user.username
	user_data['name'] = user.name
	user_data['password'] = user.password
	user_data['admin'] = user.admin
	social = Socials.query.filter_by(userid = public_id).all()
	websites = []
	print(social)
	for site in social:
		websites.append(str(site).split("  "))
	print(websites)
	if request.method == "POST":
		passphase = request.form.get('passphase')
		website_name = request.form.get('webname')
		#print(passphase + "hello world")
		data = dict()
		data['public_id'] = public_id;
		data['name'] = website_name
		print(website_name)
		encrpyt(data, passphase)
	return render_template('home.html', user = user_data, websites=websites)

##----- For Creating a new user for mobile -------##
@app.route('/api/user',methods = ['POST'])
def create_user():
	data = request.get_json()
	hashed_pass = generate_password_hash(data["password"],method = 'sha256')
	new_user = User(
		public_id = str(uuid.uuid4()),
		name = data["name"],
		username = data["username"],
		password =hashed_pass,
		admin = False
		)
	db.session.add(new_user)
	db.session.commit()
	return jsonify({"message":"User Created"})
##----- For user admin for testing -------##
@app.route('/api/user/<public_id>',methods = ['PUT'])
def make_admin(public_id):
	user = User.query.filter_by(public_id = public_id).first()
	if not user:
		return jsonify({"message":"user does not exist"})
	user.admin = True
	db.session.commit()
	return jsonify({"message":"user given admin rights"});


##----- For deleting a user -------##
@app.route('/api/user',methods = ['DELETE'])
def del_user():
	return '';
##----- For logouts -------##
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('init_w'))
app.run(debug = True)