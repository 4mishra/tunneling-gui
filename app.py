import os
from flask import Flask, render_template, redirect, url_for, request, session

from .forms import StaticIpForm, PasswordForm, TunnelForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'really-long-string')

@app.route('/', methods=['GET', 'POST'])
def index():
    """ This renders IP Address template
    """
    form = StaticIpForm(meta={'csrf': False})
    print(form)
    return render_template('index.html', form=form)


@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    form = PasswordForm(meta={'csrf': False})
    return render_template('change-password.html', form=form)

@app.route('/tunnel', methods=['GET', 'POST'])
def tunnel():
    form = TunnelForm()
    return render_template('tunnel.html', form=form)

@app.route('/diagnostics', methods=['GET', 'POST'])
def diagnostics():
    return render_template('diagnostics.html')
