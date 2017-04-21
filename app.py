import os
from flask import Flask, render_template, request, redirect, url_for, make_response
import json
import hashlib

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

@app.route('/register-driver', methods=['POST'])
def register_driver():
    driver = Driver()

    # Check if username taken
    count = Driver.objects(username=request.form['username'])
    if count > 0:
        return 'Username taken'
    driver.username = request.form['username']
    # Hash password
    driver.password = hashlib.sha512(request.form['password']).hexdigest()
    driver.name = request.form['name']
    driver.age = int(request.form['age'])
    profile_photo_img = request.files['profile_photo']
    driver.insurance = request.form['insurance']
    license_img = request.files['license']
    driver.vin = request.form['vin']

    # Upload profile and license images to cloud and store URLs
    profile_photo_json = cloudinary.uploader.upload(profile_photo_img)
    driver.profile_photo = profile_photo_json['secure_url']
    license_json = cloudinary.uploader.upload(license_img)
    driver.license = license_json['secure_url']

    # Label driver as unauthorized when initially registering
    driver.authorized = False

    driver.save()

    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)
