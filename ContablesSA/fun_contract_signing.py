import rsa
import hashlib

def import_private_key(filepath):
    with open (filepath,"rb") as key_file:
        private_key  = rsa.PrivateKey.load_pkcs1(key_file.read())
        return private_key
    
def calculate_hash(document_path):
    sha256_hash = hashlib.sha256()
    with open (document_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    print (f"El hash del documento es: {sha256_hash.hexdigest}")
    return sha256_hash.digest()

def sign_document(document_path, private_key):
    document_hash = calculate_hash(document_path)
    signature = rsa.sign(document_hash, private_key, 'SHA-256')
    with open ("document_sign.sign", "wb") as file:
        file.write(signature)
    print ("El documento ha sido firmado")

def main():
    private_key_file =  "ContablesSA/Privado/privatekey.pem"
    private_key = import_private_key (private_key_file)
    document_path = "ContablesSA/Historico/contract1.txt"
    sign_document (document_path, private_key)

if __name__ == "__main__":
    main()