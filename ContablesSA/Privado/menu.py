from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class SignContractVerificationApp(App):
    """Aplicación para verificar las firmas de contratos."""

    BINDINGS = [("d", "toggle_dark", "Alternar Modo Oscuro")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Una acción para cambiar al modo oscuro."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = SignContractVerificationApp()
    app.run()