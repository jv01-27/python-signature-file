import rsa
import ast

def generar_llave():
    (pubkey, privkey) = rsa.newkeys(2048)

    with open('publickey.pem', 'wb') as key_file:
        key_file.write(pubkey.save_pkcs1('PEM'))

    with open('privatekey.pem', 'wb') as key_file:
        key_file.write(privkey.save_pkcs1('PEM'))

    print("Llave generada y guardada correctamente.")

def importar_llave_publica(file_path):
    with open(file_path, 'rb') as key_file:
        public_key = rsa.PublicKey.load_pkcs1(key_file.read())
    return public_key

def importar_llave_privada(file_path):
    with open(file_path, 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    return private_key

def encriptar(mensaje, public_key):
    mensaje_encriptado = rsa.encrypt(mensaje.encode('utf-8'), public_key)
    return mensaje_encriptado

def desencriptar(mensaje_encriptado, private_key):
   
    mensaje = rsa.decrypt(mensaje_encriptado, private_key)
    return mensaje

# Menú principal
while True:
    print("\n1. Generar llave")
    print("2. Encriptar")
    print("3. Desencriptar")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        generar_llave()

    elif opcion == '2':
        public_key_path = input("Ingresa la ruta del archivo de llave pública (publickey.pem): ")
        public_key = importar_llave_publica(public_key_path)
        mensaje = input("Ingresa el mensaje a encriptar: ")
        mensaje_encriptado = encriptar(mensaje, public_key)
        print(f"Mensaje encriptado: {mensaje_encriptado}")

    elif opcion == '3':
        private_key_path = input("Ingresa la ruta del archivo de llave privada (privatekey.pem): ")
        private_key = importar_llave_privada(private_key_path)
        mensaje_encriptado = input("Ingresa el mensaje encriptado: ")
        mensaje_desencriptado = desencriptar(ast.literal_eval(mensaje_encriptado), private_key)
        print(f"Mensaje desencriptado: {mensaje_desencriptado}")

    elif opcion == '4':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
