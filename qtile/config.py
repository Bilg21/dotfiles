#!/usr/bin/env python3
# coding: utf-8
# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=100

# default config is in qtile repo in:
#   libqtile/resources/default_config.py
# when default-config is used due to config error, type:
#   WIN+CTRL+R  to restart qtile
#   WIN+R       to execute something

import os, subprocess
from libqtile import layout, bar, hook
from libqtile.lazy import lazy
from libqtile.config import Screen, Group, Match, ScratchPad, DropDown

import config_funcs
import config_colorthemes
import config_peripherals
import config_widgets

_theme = config_colorthemes.fancyYBGtheme
_dpi = config_funcs.get_primary_display_dpi()
_barheight = max(32, int(round(_dpi * 0.11, 0)))
_fontsize = 18 #_barheight - 2
_iconsize = _barheight - 2

# fake a WM-name that is on java-whitelist so java apps work properly
wmname = "LG3D"

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
terminal = "kitty"
file_manager = "ranger"

groups = [
    Group("1", layout='max', label="www", matches=[Match(wm_class='google-chrome')], spawn="google-chrome"),
    Group("2", layout='columns'),
    Group("3", layout='columns'),
    Group("4", layout='columns'),
    Group("5", layout='columns'),
    Group("6", layout='columns'),
    Group("7", layout='columns'),
    Group("8", layout='columns'),
    Group("9", layout='columns', label="obsidian", matches=[Match(wm_class="obsidian")], spawn="obsidian"),
    # Scratchpad groups
    ScratchPad("scratchpad", [
        DropDown("term", terminal, opacity=0.80, height=0.50, width=0.60, x=0.10, y=0.02),
        DropDown("fm", file_manager, opacity=0.80, height=0.50, width=0.60, x=0.10, y=0.02),
        DropDown("fm2", "vifm", opacity=0.80, height=0.50, width=0.60, x=0.10, y=0.02)
    ])
]

keys, mouse = config_peripherals.get_keys_and_mouse(groups)

layouts = [
    layout.Columns(border_focus=_theme['focus'], border_normal=_theme['blur'], grow_amount=2, margin = 10, border_width = 3),
    layout.Max(),
    #layout.MonadTall(border_focus=_theme['focus'], border_normal=_theme['blur']),
    #layout.Tile(ratio=0.5, border_focus=_theme['focus'], border_normal=_theme['blur']),
    #layout.Floating(border_focus=_theme['floatfocus'], border_normal=_theme['floatblur']),
]

floating_layout = layout.Floating(border_focus=_theme['floatfocus'], border_normal=_theme['floatblur'])
widget_defaults = dict(font='Ubuntu mono', _fontsize=_fontsize, padding=2)

screens = [ 
        Screen(top=bar.Bar(config_widgets.init_widgets(_theme, _fontsize, _iconsize), _barheight)),
        Screen(top=bar.Bar(config_widgets.init_widgets2(_theme, _fontsize, _iconsize), _barheight))
]

config_funcs.exec_poststart(_theme)

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    start_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([start_script])

