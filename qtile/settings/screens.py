from libqtile import bar, widget
from libqtile.config import Screen

from .widgets import widget_defaults

colorBar = "#7434eb"

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def status_bar(widgets):
    return bar.Bar(widgets, 28, background=colorBar)

screens = [
    Screen(
        bottom=status_bar(
            widget_defaults
        )),
]