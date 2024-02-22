from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static

class ActionButtons(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("1.- Crear Llaves", id="create_keys", variant="primary", classes="box")
        yield Button("2.- Firmar Contrato", id="sign_file", variant="success", classes="box")
        yield Button("3.- Verificar Contrato", id="verify_contracts", variant="warning", classes="box")
        yield Button("4.- Mostrar registro", id="show_log", variant="error", classes="box")

class ContablesSA_Contratos(App):
    """Aplicación para verificar las firmas de contratos."""

    CSS_PATH = "menu.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Modo claro/oscuro"),
        ("q", "quit", "Finaliza el programa"),
        ("s", "save_screenshot", "Captura de pantalla")
        ]

    def compose(self) -> ComposeResult:
        """Crea widgets hijos para tu aplicación."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(ActionButtons())

    def action_toggle_dark(self) -> None:
        """Una acción para cambiar al modo oscuro."""
        self.dark = not self.dark



if __name__ == "__main__":
    app = ContablesSA_Contratos()
    app.run()