from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/create_account')
def create_account():
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    try:
        os.mkdir(f"static/data/{email}")
    except:
        print("Already exists")

app.run(host='0.0.0.0', port=5000,debug=True)