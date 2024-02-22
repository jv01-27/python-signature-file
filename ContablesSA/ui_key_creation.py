from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static

class ActionButtons(Static):
    """Botones de accion."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        

class Creacion_Llaves(App):
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
        # yield ScrollableContainer(ActionButtons())

    def action_toggle_dark(self) -> None:
        """Una accion para cambiar al modo oscuro."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = Creacion_Llaves()
    app.run()