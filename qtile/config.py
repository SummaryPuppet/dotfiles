from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# My settings

import os

# from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
#from settings.screen import *

mod = "mod4"
terminal = guess_terminal()


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows 
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --togle-mute")),

    # Open Firefox
    Key([mod], "f", lazy.spawn("firefox")),

    # Rofi (Menu)
    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]



groups = [Group(i) for i in [
    "",
    "",
    "",
    "",
    "",
    "ﱘ"
]]

for i, group in enumerate(groups):
    num_desktop = str(i + 1)

    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                num_desktop,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                num_desktop,

                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

border_focus_stack1 = ["#6069db","#3f4196"]

layouts = [
    # layout.Columns(border_focus_stack=border_focus_stack1, border_width=4),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(border_focus_stack=border_focus_stack1, border_normal="#6069db"),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Caskaydia Cove Nerd Font Complete",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

bar_font_size = 26
bar_color = "#000112"

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active="#00ffff",
                    inactive="#014647",
                    padding_x=6,
                    fontsize=20,
                    rounded=False,
                    highlight_method='block',
                    block_highlight_text_color='#00ffff',
                    this_current_screen_border='#0f293b',
                    center_aligned=True,
                    disable_drag=True
                ),
                #widget.WindowName(),
                widget.Spacer(length=783),
                widget.PulseVolume(
                    foreground='#ff00ff',
                    volume_app="pavucontrol",
                ),
                widget.Systray(),
                widget.Clock(
                    format="%d/%m/%Y - %I:%M %p",
                    foreground="#0000ff"
                ),
                #widget.QuickExit(),
                widget.CurrentLayout(),
                widget.TextBox("adrian-arch", foreground="ff0000")
            ],
            bar_font_size,
            background=bar_color
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
    "feh --bg-scale /home/adrian/background/fondo.jpg",
    "picom &"
]

for x in autostart:
    os.system(x)
