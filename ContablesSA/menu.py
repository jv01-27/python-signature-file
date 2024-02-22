from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static

class ActionButtons(Static):
    """Botones de accion."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Controlador para cuando se presiona un botón."""
        button_id = event.button.id
        if button_id == "create_keys":
            action_push_screen()
        elif button_id == "sign_file":
            self.remove_class("started")
        elif button_id == "verify_contracts":
            self.remove_class("started")
        elif button_id == "show_log":
            self.remo

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("1.- Crear Llaves", id="create_keys", variant="primary", classes="box")
        yield Button("2.- Firmar Contrato", id="sign_file", variant="success", classes="box")
        yield Button("3.- Verificar Contrato", id="verify_contracts", variant="warning", classes="box")
        yield Button("4.- Mostrar registro", id="show_log", variant="error", classes="box")

    def action_push_screen(self, screen) -> None:
        """Cambiar de pantalla."""

class ContablesSA_Contratos(App):
    """Aplicacion para verificar las firmas de contratos."""

    CSS_PATH = "menu.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Modo claro/oscuro"),
        ("q", "quit", "Finaliza el programa"),
        # ("s", "save_screenshot", "Captura de pantalla")
        ]

    def compose(self) -> ComposeResult:
        """Crea widgets hijos para tu aplicacion."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(ActionButtons())

    def action_toggle_dark(self) -> None:
        """Una accion para cambiar al modo oscuro."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = ContablesSA_Contratos()
    app.run()