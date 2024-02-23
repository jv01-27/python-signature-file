import rsa
import hashlib
import os

def import_private_key(filepath):
    with open(filepath, "rb") as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
        return private_key

def calculate_hash(document_path):
    sha256_hash = hashlib.sha256()
    with open(document_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    print(f"El hash del documento es: {sha256_hash.hexdigest()}")
    return sha256_hash.digest()

def sign_document(document_path, private_key):
    document_hash = calculate_hash(document_path)
    signature = rsa.sign(document_hash, private_key, 'SHA-256')
    
    # Obtener el nombre del archivo sin la ruta
    filename = os.path.basename(document_path)
    
    # Generar el nombre del archivo .sign con el mismo nombre que el documento
    sign_file_path = f"{filename}.sign"
    
    with open(sign_file_path, "wb") as file:
        file.write(signature)
    print("El documento ha sido firmado")

def main():
    private_key_file = "ContablesSA/Privado/privatekey.pem"
    private_key = import_private_key(private_key_file)
    
    # Obtener la ruta del documento desde la entrada del usuario
    document_path = input("Ingrese la ruta del documento: ")
    
    # Validar si el archivo existe
    if os.path.exists(document_path):
        sign_document(document_path, private_key)
    else:
        print("El archivo no existe. Verifique la ruta proporcionada.")

if __name__ == "__main__":
    main()
