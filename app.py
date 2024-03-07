from flask import Flask, flash, request, redirect, url_for, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

app.run(host='0.0.0.0', port=5000,debug=True)