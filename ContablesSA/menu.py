import rsa
import hashlib
import os

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Input, Label

# Import necessary modules for screen navigation and screenshot
from textual.screen import Screen, ModalScreen

ALERT_TEXT = """
Antes de continuar:

Está a punto de crear llaves nuevas.
Esto sustituirá las llaves existentes.

Esto hará inválido cualquier contrato firmado con las llaves anteriores.
"""

class ActionButtons(Static):
    """Botones de accion."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Controlador para cuando se presiona un botón."""
        button_id = event.button.id
        if button_id == "btn_create_keys":
            self.app.push_screen("ui_create_keys")  # Navigate to the specified screen
        elif button_id == "btn_sign_file":
            self.app.push_screen("ui_sign_contract")
        elif button_id == "btn_verify_contracts":
            self.app.push_screen("ui_verify_contract")
        elif button_id == "btn_show_log":
            self.app.push_screen("ui_log")

    def compose(self) -> ComposeResult:
        """Interfaz principal."""
        yield Button("1.- Crear Llaves", id="btn_create_keys", variant="primary", classes="box")
        yield Button("2.- Firmar Contrato", id="btn_sign_file", variant="success", classes="box")
        yield Button("3.- Verificar Contrato", id="btn_verify_contracts", variant="warning", classes="box")
        yield Button("4.- Mostrar registro", id="btn_show_log", variant="error", classes="box")       

class KeySuccessDialog(ModalScreen):
    """Pantalla de dialogo.""" 

    BINDINGS = [
        ("escape", "app.pop_screen", "Regresar")        
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Static("¡Llaves generadas correctamente!\nPresione ESC para volver", id="question")
            ,id="dialog"
        )    

class QuitScreen(ModalScreen[bool]):  
    """Pantalla de confirmacion."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("¿Desea finalizar el programa?", id="question"),
            Button("Finalizar", variant="error", id="quit", classes="full_btn"),
            Button("Cancelar", variant="primary", id="cancel", classes="full_btn"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.dismiss(True)
        else:
            self.dismiss(False)

class SignErrorDialog(ModalScreen):
    """Pantalla de dialogo.""" 

    BINDINGS = [
        ("escape", "app.pop_screen", "Regresar")        
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Static("Se ha ingresado una ruta no valida, intente de nuevo\nPresione ESC para volver", id="question")
            ,id="dialog"
        )

class SignSuccessDialog(ModalScreen):
    """Pantalla de dialogo.""" 

    BINDINGS = [
        ("escape", "app.pop_screen", "Regresar")        
    ]

    def compose(self) -> ComposeResult:
        yield Grid(
            Static("¡Contrato firmado correctamente!\nPresione ESC para volver", id="question")
            ,id="dialog"
        ) 

class UI_Key_Creation(Screen):
    BINDINGS = [
        ("escape", "app.pop_screen", "Regresar")        
    ]  

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "btn_create_keys":
            self.action_create_keys()

    def compose(self) -> ComposeResult:
        yield Static(" Creación de Llaves ", id="title")
        yield Static(ALERT_TEXT)
        yield Button("Generar Llaves", id="btn_create_keys", variant="error")

    def action_create_keys(self) -> None:
        (pubkey, privkey) = rsa.newkeys(2048)

        with open('Privado/publickey.pem', 'wb') as key_file:
            key_file.write(pubkey.save_pkcs1('PEM'))
    
        with open('Privado/privatekey.pem','wb')as key_file:
            key_file.write(privkey.save_pkcs1('PEM'))

        self.app.pop_screen()
        self.action_show_message()

    def action_show_message(self) -> None:        
        self.app.push_screen(KeySuccessDialog())
        
class UI_Contract_Sign(Screen):
    BINDINGS = [
        ("escape", "app.pop_screen", "Regresar")        
    ]

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "btn_sign":
            self.action_sign_contract()

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Ruta del archivo a firmar", type="text")
        yield Button("Firmar Contrato", id="btn_sign", variant="primary", classes="box")

    def action_sign_contract(self) -> None:
        document_path = self.query("document_path_input", type="str")  # Get input via query instead of direct access

        # Validar si el archivo existe
        if os.path.exists(document_path):
            sign_document(document_path, private_key)
        else:            
            self.error_show_message()
            def error_show_message(self) -> None:        
                self.app.push_screen(SignErrorDialog())

        
        
        private_key_file = "ContablesSA/Privado/privatekey.pem"
        private_key = import_private_key(private_key_file)
        
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

        self.app.pop_screen()
        self.action_show_message()

    def action_show_message(self) -> None:        
        self.app.push_screen(SignSuccessDialog())

class ContablesSA_Contratos(App):
    """Aplicacion para verificar las firmas de contratos."""

    CSS_PATH = "menu.tcss"
    SCREENS = {"ui_create_keys": UI_Key_Creation(),
               "ui_sign_contract" : UI_Contract_Sign(),
               }

    BINDINGS = [
        ("d", "toggle_dark", "Modo claro/oscuro"),
        ("q", "request_quit", "Finalizar programa"),        
        ("b", "push_screen('ui_create_keys')", "Generar LLaves"),        
    ]

    def compose(self) -> ComposeResult:
        """Crea widgets hijos para tu aplicacion."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(ActionButtons())

    def action_toggle_dark(self) -> None:
        """Una accion para cambiar al modo oscuro."""
        self.dark = not self.dark

    def action_request_quit(self) -> None:
        """Accion que activa el dialogo de cierre."""

        def check_quit(quit: bool) -> None:
            """Se llama cuando QuitScreen es descartado."""
            if quit:
                self.exit()
        
        self.push_screen(QuitScreen(), check_quit)

if __name__ == "__main__":
    app = ContablesSA_Contratos()
    app.run()
