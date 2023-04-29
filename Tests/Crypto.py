from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
print(key)
token = f.encrypt(b'Secret message')
print(token)
token = f.decrypt(token)
print(token)
