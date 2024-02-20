import rsa
import hashlib

def import_public_key(filepath):
    with open (filepath, "rb") as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())
    return public_key

def calcula_hash(document_path):
    sha256_h = hashlib.sha256()
    with open (document_path, "rb") as file:
        for byte_block in iter (lambda: file.read(4096), b""):
            sha256_h.update(byte_block)
    return sha256_h.digest()

def verificacion_document (document_path, signature_path, public_key):
    document_hash = calcula_hash(document_path)

    with open (signature_path, "rb") as signature_file:
        signature = signature_file.read()

    try:
        rsa.verify(document_hash, signature, public_key)
        print("La firma es válida")
    except rsa.VerificationError:
        print("Firma no válida")

def main():
    public_key_path = "publickey.pem"
    signature_path = "document_sign.sign"
    public_key = import_public_key(public_key_path)
    document_path = "cat.jpg"
    verificacion_document(document_path, signature_path, public_key)

if __name__ == "__main__":
    main()