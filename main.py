from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from screens.landingPage import LandingPage

appName = str("CLI - CV")


class CLICV(App):
    def compose(self) -> ComposeResult:
        self.theme = "textual-dark"
        yield Header(id="Header", show_clock=True)
        self.push_screen(screen=LandingPage())
        yield Footer(id="Footer", show_command_palette=True)


if __name__ == "__main__":
    app = CLICV()
    app.run()
