from flask import render_template
from personal_site import app

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route("/resume", methods=['GET', 'POST'])
def resume():
	return render_template('full_resume.html')

@app.route("/connect", methods=['GET', 'POST'])
def connect():
	return render_template('connect.html')

@app.route("/apps", methods=['GET', 'POST'])
def apps():
	return render_template('apps.html')

@app.route("/interests", methods=['GET', 'POST'])
def interests():
	return render_template('interests.html')
