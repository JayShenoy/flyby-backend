from mongoengine import *

class Driver(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    name = StringField(required=True)
    age = StringField(required=True)
    #profile_photo = StringField(required=True)
    insurance = StringField(required=True)
    license = StringField(required=True)
    vin = StringField(required=True)
    authorized = BooleanField(required=True)

class Senior(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    name = StringField(required=True)
    age = StringField(required=True)
    #profile_photo = StringField(required=True)
    #identification = StringField(required=True)
    address = StringField(required=True)
    hospital = StringField(required=True)
    has_cane = BooleanField(required=True)
    has_walker = BooleanField(required=True)
    authorized = BooleanField(required=True)