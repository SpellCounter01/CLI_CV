from textual.binding import Binding
from textual.widgets import OptionList


class VimMotionOptionList(OptionList):
    BINDINGS = [
        Binding("j", "cursor_down", "Down", True),
        Binding("k", "cursor_up", "Up", True),
    ]
