from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Header
from screens.generateOptionListModal import GenerateOptionListModal


class TextEditor(Screen):
    TITLE = "Text Editor"
    SUB_TITLE = "New CV"

    BINDINGS: list[Binding] = [
        Binding("ctrl+n", "newSection", "New section", show=True),
        Binding("ctrl+q", "quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_newSection(self):
        self.app.push_screen(GenerateOptionListModal())
