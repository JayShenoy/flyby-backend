import os
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from flask.ext.cors import CORS, cross_origin
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
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

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
@cross_origin()
def register_driver():
    driver = Driver()

    # Check if username taken
    count = Driver.objects(username=request.form['username']).count()
    if count > 0:
        return json.dumps('Username taken')
    driver.username = request.form['username']
    # Hash password
    driver.password = hashlib.sha512(request.form['password']).hexdigest()
    driver.name = request.form['name']
    driver.age = request.form['age']
    #profile_photo_img = request.files['profile_photo']
    driver.insurance = request.form['insurance']
    license = request.form['license']
    driver.vin = request.form['vin']

    # Upload profile and license images to cloud and store URLs
    '''profile_photo_json = cloudinary.uploader.upload(profile_photo_img)
    driver.profile_photo = profile_photo_json['secure_url']'''

    # Label driver as unauthorized when initially registering
    driver.authorized = False

    driver.save()

    return json.dumps('Success')

@app.route('/register-senior', methods=['POST'])
@cross_origin()
def register_senior():
    senior = Senior()

    # Check if username taken
    count = Senior.objects(username=request.form['username']).count()
    if count > 0:
        return json.dumps('Username taken')
    senior.username = request.form['username']
    # Hash password
    senior.password = hashlib.sha512(request.form['password']).hexdigest()
    senior.name = request.form['name']
    senior.age = request.form['age']
    #profile_photo_img = request.files['profile_photo']
    #id_img = request.files['license']
    senior.address = request.form['address']
    senior.hospital = request.form['hospital']

    # Check for cane and walker
    if 'has_cane' in request.form:
        senior.has_cane = True
    else:
        senior.has_cane = False
    if 'has_walker' in request.form:
        senior.has_walker = True
    else:
        senior.has_walker = False

    # Upload profile and identification images to cloud and store URLs
    '''profile_photo_json = cloudinary.uploader.upload(profile_photo_img)
    senior.profile_photo = profile_photo_json['secure_url']
    id_json = cloudinary.uploader.upload(id_img)
    senior.identification = id_json['secure_url']'''

    # Label senior as unauthorized when initially registering
    senior.authorized = False

    senior.save()

    return json.dumps('Success')

if __name__ == '__main__':
    app.run(debug=True)
