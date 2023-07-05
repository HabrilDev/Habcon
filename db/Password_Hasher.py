import bcrypt

passwd = b'TingTong'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
print(hashed)