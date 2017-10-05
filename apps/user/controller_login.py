from .models import *
import bcrypt

class LoginCtrl():
    def getUser(self, data):
        user = User.objects.get(email=data['email'])
        if user:
            return user
        else:
            return None

    def encrypt(self, data):
        password = bcrypt.hashpw(data.encode(), bcrypt.gensalt())
        return password

    def decrypt(self, data):
        errors = []
        compare = User.objects.filter(email=data['email'].lower())
        if len(compare) > 0 and bcrypt.checkpw(data['password'].encode(), compare[0].password.encode()):
            return True
        else:
            errors.append('Invalid Login')
            return errors