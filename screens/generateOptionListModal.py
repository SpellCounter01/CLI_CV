from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import ModalScreen
from components.vimMotionOptionList import VimMotionOptionList


class GenerateOptionListModal(ModalScreen):
    ESCAPE_TO_MINIMIZE = True

    BINDINGS: list[Binding] = [
        Binding("j", "cursor_down", "Down", True),
        Binding("k", "cursor_up", "Up", True),
    ]

    def compose(self) -> ComposeResult:
        optionList = VimMotionOptionList(
            "Experience",
            "Award",
        )

        yield optionList

        return super().compose()
