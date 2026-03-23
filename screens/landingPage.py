from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import VerticalGroup
from textual.screen import Screen
from textual.widgets import Label
from screens.textEditor import TextEditor


class LandingPage(Screen):
    CSS_PATH = "../tcss/landingPage.tcss"
    TITLE = "CLI CV"
    SUB_TITLE = "A CV editor on your terminal"

    BINDINGS: list[Binding] = [
        Binding("n", "new", "Create new", show=True, priority=True),
        Binding("e", "edit", "Edit CV", show=True, priority=True),
        Binding("ctrl+q", "quit", "Quit", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        welcomeString = Label(
            content="Welcome CLI - CV choose an operation",
            classes="welcomeString",
        )

        self.styles.align = (
            "center",
            "middle",
        )

        options = []

        for keybind in self.BINDINGS:
            if keybind.description:
                tempLabel = Label(
                    f"[bold underline]{keybind.key}[/] [dim]{keybind.description}[/]"
                )
                options.append(tempLabel)

        yield VerticalGroup(welcomeString, VerticalGroup(*options, classes="optionDiv"))

    def action_new(self):
        self.app.switch_screen(screen=TextEditor())
