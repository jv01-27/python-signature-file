import rsa

(pubkey, privkey) = rsa.newkeys(2048)

with open('Privado/publickey.pem', 'wb') as key_file:
    key_file.write(pubkey.save_pkcs1('PEM'))
    
with open('Privado/privatekey.pem','wb')as key_file:
    key_file.write(privkey.save_pkcs1('PEM'))