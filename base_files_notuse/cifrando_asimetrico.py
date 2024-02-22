import rsa

def import_public_key(file_path):
    with open(file_path, 'rb') as key_file:
        public_key = rsa.PublicKey.load_pkc1(key_file.read())
    return public_key
    
    
def import_private_key(file_path):
    with open(file_path, 'rb') as key_file:
        private_key=rsa.PrivateKey.load_pkcs1(key_file.read())
    return private_key   
    
def cifrado(mensaje,public_key):
    msj_cifrado= rsa.encrypt(mensaje.encode(),public_key) 
    return msj_cifrado

def desifrar(mensaje_cifrado,private_key):
    mensaje= rsa.decrypt(mensaje_cifrado ,private_key)
    return mensaje
    
def main():
    public_key =import_public_key('publickey.pem')
    private_key=import_private_key('privatekey.pem')
    mensaje="Asinatura de Ciberseguridad para conocer el encriptado."
    mensaje_cifrado= cifrado(mensaje,public_key)
    print("Mensaje cifrado ",mensaje_cifrado)
    mensaje_desifrado=desifrar(mensaje_cifrado,private_key)
    print("Mensaje descifrado", mensaje_desifrado)  
    
    if __name__ == "__main__":
       main()     