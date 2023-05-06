#!/usr/bin/env python3
# coding: utf-8
# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=100

import libqtile
from libqtile import widget
#from qtile_extras.widget.decorations import BorderDecoration

import config_funcs

import socket

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


class LayoutIcon(widget.CurrentLayoutIcon):
    """Like CurrentLayoutIcon, but shows layout for *current* group, not screen of this bar. """
    def _setup_hooks(self):
        def hook_update_layout(*args, **kwargs):
            g = libqtile.qtile.current_group
            layout = g.layouts[g.current_layout]
            new_layout = layout.name
            if self.current_layout != new_layout:
                self.current_layout = new_layout
                self.bar.draw()

        libqtile.hook.subscribe.layout_change(hook_update_layout)# error here Idk why.
        libqtile.hook.subscribe.current_screen_change(hook_update_layout)

def left_arrow(theme, color):
    return widget.TextBox(
            text = '\u25C0', 
            background = theme['background'], 
            foreground = color,
#            font = "Ubuntu Mono",
            padding = 0,
            fontsize = 20)

def apply_theme(theme, widgets):
    for w in widgets:
        w.background = theme['background']

def init_widgets(theme, fontsize, iconsize):
    widgets = [
            widget.Spacer(length=6),
            widget.Image(
                background=theme['background'],
                filename = "/usr/share/icons/LoginIcons/apps/64/computer.svg",
                scale = "True"),
            widget.GroupBox(
                       background=theme['background'],
                       disable_drag=True,
                       use_mouse_wheel=False,
                       highlight_method=theme['highlight_method'],
                       hide_unused=False,
                       this_current_screen_border=theme['foreground'],
                       this_screen_border=theme['screenblur'],
                       other_current_screen_border=theme['foreground'],
                       other_screen_border=theme['screenblur'],
                       urgent_alert_method='text',
                       fontsize=fontsize,
                       borderwidth=2,
                       visible_groups=['1','2','3','4','5']
                      ),
            widget.CurrentLayoutIcon(background=theme['background']),
            widget.WindowName(foreground=theme['text'], background=theme['background'], 
                fontsize=fontsize, for_current_screen=True),
            widget.Prompt(foreground=theme['textprompt'],
                          cursor_color=theme['foreground'],
                          bell_style='visual',
                          visual_bell_time=0.1,
                          visual_bell_color='#ffffff',
                          font="DejaVu Sans Mono",
                         ),
        ]
    widgets += [
            widget.Sep(linewidth=3),
            widget.Net(background=theme['background'], padding = 2, fontsize=16),
#            widget.GenPollText(func=config_funcs.get_dirty_mem_M, update_interval=15, foreground='#ff4400'),
#            widget.Clock(format='%Z %H:%M', timezone="PST8PDT", foreground='#3030a0'),
#            widget.Clock(format='%Z %H:%M', timezone="America/Los_Angeles", foreground='#805000'),
#            widget.Clock(format='%Z %H:%M'),
            #left_arrow(theme, colors[6]),
            widget.Sep(background=colors[1], linewidth=3),
            widget.Clock(format='%a %Y-%m-%d %H:%M %Z', foreground='#ffffff', background=theme['background'], padding = 2, fontsize=20),
#            widget.Volume(mute_command="pactl set-sink-mute 3 toggle", background=colors[0], padding = 2),
            widget.Systray(icon_size=iconsize),
        ]
#    apply_theme(theme, widgets)
    return widgets

def init_widgets2(theme, fontsize, iconsize):
    widgets = [
        widget.Spacer(length=6),
        widget.Image(
            filename = "/usr/share/icons/LoginIcons/apps/64/computer.svg",
            scale = "True"),
        widget.CurrentLayoutIcon(background=theme['rootwindow'], padding = 6),
        widget.GroupBox(
            disable_drag=True,
            use_mouse_wheel=False,
            highlight_method=theme['highlight_method'],
            hide_unused=False,
            this_current_screen_border=theme['foreground'],
            this_screen_border=theme['screenblur'],
            other_current_screen_border=theme['foreground'],
            other_screen_border=theme['screenblur'],
            urgent_alert_method='text',
            fontsize=fontsize,
            borderwidth=2,
            visible_groups=['6','7','8','9']),
        widget.Sep(),
#        widget.PulseVolume(),
#        widget.Pomodoro(),
#        widget.SwapGraph(),
#        widget.ThermalSensor(),
#        widget.Volume(mute_command="pactl set-sink-mute 3 toggle"),
#        widget.Wallpaper(),
        widget.Sep(),
        widget.WindowName(),
        widget.Sep(background=colors[1], linewidth=3),
        widget.Clock(format='%a %Y-%m-%d %H:%M %Z', foreground='#ffffff', background=theme['background'], padding = 2, fontsize=20),
   ]

    apply_theme(theme, widgets)
    return widgets


