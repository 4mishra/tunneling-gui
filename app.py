import os
import shelve
import subprocess
from flask import Flask, render_template, redirect, url_for, request, session

from forms import StaticIpForm, PasswordForm, TunnelForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'really-long-string')

# db = shelve.open

@app.route('/', methods=['GET', 'POST'])
def index():
    """ This renders IP Address template
    """
    form = StaticIpForm(meta={'csrf': False})
    return render_template('index.html', form=form)


@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    form = PasswordForm(meta={'csrf': False})
    if form.is_valid():
        # TODO 1:shelve.sync
    return render_template('change-password.html', form=form)

@app.route('/tunnel', methods=['GET', 'POST'])
def tunnel():
    form = TunnelForm()
    return render_template('tunnel.html', form=form)

@app.route('/diagnostics', methods=['GET', 'POST'])
def diagnostics():
    return render_template('diagnostics.html')

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
