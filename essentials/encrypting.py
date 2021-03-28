import simplecrypt
import libarchive.public

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)

with open('passwords.txt', 'r') as passes:
    for password in passes:
        password = password.strip()
        print(password)
        decrypt_data = simplecrypt.decrypt(password, encrypted)
        print('failed')
