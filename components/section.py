from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widget import Widget
from textual.widgets import Label


class Section(VerticalGroup):
    def __init__(
        self,
        *children: Widget,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
        markup: bool = True,
        hasDate: bool = False,
        hasDescription: bool = False,
    ) -> None:
        super().__init__(
            *children,
            name=name,
            id=id,
            classes=classes,
            disabled=disabled,
            markup=markup,
        )

        self.hasDescription = hasDescription
        self.hasDate = hasDate

    def compose(self) -> ComposeResult:
        yield Label("test")

    def on_mount(self) -> None:
        self.compose_add_child(VerticalGroup(Label("test")))
