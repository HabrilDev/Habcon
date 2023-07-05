import bcrypt

passwd = b'TingTong'
hashed = b'$2b$12$s1sfKqaSKJbj627qSMTlOuiNqA5wsMbDzLnTEVe.By1XbMNGXO1uK'


if bcrypt.checkpw(passwd, hashed):
    print("match")
else:
    print("does not match")