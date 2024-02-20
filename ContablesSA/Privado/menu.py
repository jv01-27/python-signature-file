from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class ContablesSA_Contratos(App):
    """Aplicación para verificar las firmas de contratos."""

    BINDINGS = [
        ("d", "toggle_dark", "Alternar modo oscuro"),
        ("q", "quit", "Finaliza el programa")
        ]

    def compose(self) -> ComposeResult:
        """Crea widgets hijos para tu aplicación."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Una acción para cambiar al modo oscuro."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = ContablesSA_Contratos()
    app.run()