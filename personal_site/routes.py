from flask import render_template
from personal_site import app

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template('new_home.html')


@app.route("/resume", methods=['GET', 'POST'])
def resume():
	return render_template('new_resume.html')

@app.route("/connect", methods=['GET', 'POST'])
def connect():
	return render_template('new_connect.html')

@app.route("/projects", methods=['GET', 'POST'])
def projects():
	return render_template('new_projects.html')
