class Validar:
    import uuid
    import hashlib

    def hash_password(self, password):
        # uuid is used to generate a random number
        salt = self.uuid.uuid4().hex
        password_encrip=self.hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        datos_password = []
        datos_password.append(salt)
        datos_password.append(password_encrip)
        return datos_password
    
    def check_password(self, hashed_password, user_password, salt_user):
        password, salt = hashed_password.split(':')
        if salt.encode() == salt_user.encode() and password == self.hashlib.sha256(salt.encode() + user_password.encode()).hexdigest():
            val_password = True
        else:
            val_password = False

        return val_password
 
#new_pass = input('Please enter a password: ')
#hashed_password = hash_password(new_pass)
#print('The string to store in the db is: ' + hashed_password)
#old_pass = input('Now please enter the password again to check: ')
#if check_password(hashed_password, old_pass):
#    print('You entered the right password')
#else:
#    print('I am sorry but the password does not match')