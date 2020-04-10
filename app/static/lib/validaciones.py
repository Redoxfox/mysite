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