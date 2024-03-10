from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sign-up')
def sign_up():
    return render_template('new-sign-up.html')

@app.route('/create_account')
def create_account():
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    try:
        os.mkdir(f"static/user_data/{email}")
    except:
        return {"valid":"email_error"}
    fields = ['username', 'password', 'email']
    data = [[
        username, password, email
    ]]
    with open(f"static/user_data/{email}/basic_data.csv", 'w',newline='', encoding='utf-8') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)
    return {"valid":"True"}

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(host='0.0.0.0', port=5000,debug=True)