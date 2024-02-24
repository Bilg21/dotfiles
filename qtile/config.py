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
import config_groups
import config_widgets

_theme = config_colorthemes.CozyTheme
_dpi = config_funcs.get_primary_display_dpi()
_barheight = max(32, int(round(_dpi * 0.11, 0)))
_fontsize = 18 #_barheight - 2
_iconsize = _barheight - 2

# fake a WM-name that is on java-whitelist so java apps work properly
wmname = "LG3D"

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
terminal = "kitty"
file_manager = "kitty -e ranger"

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# GROUPS
groups = config_groups.init_groups()

# KEY/MOUSE BINDINGS
keys, mouse = config_peripherals.get_keys_and_mouse(groups)

# L A Y O U T S
layouts = [ 
    layout.Columns( margin= [10,10,10,10], 
        border_focus=_theme['focus'], #'#CAA9E0',
        border_normal=_theme['blur'],#'#1F1D2E',
        border_width=2,
    ),  

    layout.Max( 
        #border_focus=_theme['focus'],
        border_normal=_theme['blur'],
        border_focus='#4B427E',
        margin=10,
        border_width=2,
    ),  

    layout.Floating(    
        border_focus=_theme['focus'], #'#CAA9E0',
        border_normal=_theme['blur'],#'#1F1D2E',
        margin=10,
        border_width=2,
    ),  
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
#     layout.Matrix( border_focus='#1F1D2E',
#        border_normal='#1F1D2E',
#        margin=10,
#        border_width=0,
#    ),  
     layout.MonadTall(  
        border_focus=_theme['focus'], #'#CAA9E0',
        border_normal=_theme['blur'],#'#1F1D2E',
        margin=10,
        border_width=2,
    ),
#    layout.MonadWide(   border_focus='#1F1D2E',
#        border_normal='#1F1D2E',
#        margin=10,
#        border_width=0,
#    ),  
   #  layout.RatioTile(),
#     layout.Tile(   border_focus='#1F1D2E',
#        border_normal='#1F1D2E',
#    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
    layout.Zoomy(
        border_focus=_theme['focus'], #'#CAA9E0',
        border_normal=_theme['blur'],#'#1F1D2E',
        margin=10,
        columnwidth=400,
    ),
]

# floating_layout = layout.Floating(border_focus=_theme['floatfocus'], border_normal=_theme['floatblur'])
# Make certain windows to be only Float
floating_layout = layout.Floating(
    border_focus=_theme['focus'], #'#CAA9E0',
    border_normal=_theme['blur'],#'#1F1D2E',
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Calendar"),  # GPG key password entry
    ]   
)

# WIDGETS
widget_defaults = dict(font='Ubuntu mono', _fontsize=_fontsize, padding=2)

#SCREENS
screens = [ 
        Screen(top=bar.Bar(
            config_widgets.init_widgets(_theme, _fontsize, _iconsize
            ), 
            _barheight, 
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [6,15,6,15],
            background="#282738",
            spacing = 0
            )
        ),
        Screen(top=bar.Bar(
            config_widgets.init_widgets2(_theme, _fontsize, _iconsize), 
            _barheight, 
            background="#282738",
            )
        )
]

# POST START
config_funcs.exec_poststart(_theme)

@hook.subscribe.startup_once
def start_once():
    start_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([start_script])

