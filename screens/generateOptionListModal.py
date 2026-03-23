from textual.app import ComposeResult
from textual.screen import ModalScreen
from components.vimMotionOptionList import VimMotionOptionList


class GenerateOptionListModal(ModalScreen):
    ESCAPE_TO_MINIMIZE = True

    def compose(self) -> ComposeResult:
        optionList = VimMotionOptionList(
            "Experience",
            "Award",
        )

        yield optionList

        return super().compose()
