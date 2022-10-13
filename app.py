import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'really-long-string')

@app.route('/', methods=['GET', 'POST'])
def index():
    """ This renders IP Address template
    """
    return render_template('index.html')


@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    return render_template('change-password.html')

@app.route('/tunnel', methods=['GET', 'POST'])
def tunnel():
    return render_template('tunnel.html')

@app.route('/diagnostics', methods=['GET', 'POST'])
def diagnostics():
    return render_template('diagnostics.html')
