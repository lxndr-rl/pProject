import hashlib

passw = input('Frase a encriptar: ')
print(hashlib.md5(passw.encode()).hexdigest())