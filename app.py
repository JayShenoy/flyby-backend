import os
from flask import Flask, render_template, request, redirect, url_for, make_response
import json

from config import *
from mongoengine import connect
from models import *

import cloudinary
import cloudinary.uploader
import cloudinary.api

connect(MONGODB_NAME, host=MONGODB_URI)

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

cloudinary.config(
    cloud_name = 'jayshenoy',
    api_key = '288719545538119',
    api_secret = 'sRhVjoVT5TmWk-IfgEFGyzRUVY4'
)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
