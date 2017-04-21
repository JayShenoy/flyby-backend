from mongoengine import *

class Driver(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    profile_photo = StringField(required=True)
    insurance = StringField(required=True)
    license = StringField(required=True)
    vin = StringField(required=True)
    authorized = BooleanField(required=True)

class Senior(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    profile_photo = StringField(required=True)
    identification = StringField(required=True)
    address = StringField(required=True)
    hospital = StringField(required=True)
    has_cane = BooleanField(required=True)
    has_walker = BooleanField(required=True)
    authorized = BooleanField(required=True)