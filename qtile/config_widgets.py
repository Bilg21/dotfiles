#!/usr/bin/env python3
# coding: utf-8
# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=100

import libqtile
from libqtile import widget
from qtile_extras import widget
from qtile_extras.widget.decorations import (RectDecoration, BorderDecoration, PowerLineDecoration)

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

widget_defaults = dict(
        font="sans",
        fontsize=12,
        padding=3,
        )

decoration_group = {
        "decorations": [
            RectDecoration(colour=colors[4], radius=10, filled=True, padding_y=4, group=True)
            ],
        "padding": 10,
        }

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
            text = '◀', 
            background = theme['background'], 
            foreground = color,
            #            font = "Ubuntu Mono",
            padding = 0,
            fontsize = 20)

def apply_theme(theme, widgets):
    for w in widgets:
        w.background = theme['background']
        w.foreground = theme['text']
        w.font = theme['font']
#        w.fontsize = theme['fontsize']

def init_widgets(theme, fontsize, iconsize):
    widgets = [

            widget.Image(
                filename='~/.config/qtile/Assets/launch_Icon.png',
                margin=2,
                background='#282738',
                mouse_callbacks={"Button1":config_funcs.power},
                ),

            #widget.Image(
                #    background=theme['background'],
                #    filename = "/usr/share/icons/LoginIcons/apps/64/computer.svg",
                #    scale = "True"),

            widget.Image(
                background='#282738',
                #background = '#353446',
                filename='~/.config/qtile/Assets/6.png',
                ),

            widget.StatusNotifier(**decoration_group),
            #widget.CurrentLayoutIcon(background="#00000000"),

            widget.Sep(
                linewidth=5,
                background='#353446',
                foreground='#353446',
                ),
            widget.GroupBox(
                font = 'Font Awesome 6 Pro',
                fontsize=24,
                borderwidth=3,
                highlight_method='block',
                active='#CAA9E0',
                block_highlight_text_color="#91B1F0",
                highlight_color='#4B427E',
                inactive='#282738',
                foreground='#4B427E',
                background='#353446',
                this_current_screen_border='#353446',
                this_screen_border='#353446',
                other_current_screen_border='#353446',
                other_screen_border='#353446',
                urgent_border='#353446',
                rounded=True,
                disable_drag=True,
                visible_groups=['1','2','3','4','5']
                ),

            #            widget.GroupBox(
                #                decorations=[RectDecoration(colour="#212733", radius=7, filled=True)],
                #                font="Ubuntu Mono",
                #                #background="#005588",#theme['background'],
                #                rounded=True,
                #                disable_drag=True,
                #                use_mouse_wheel=False,
                #                highlight_method=theme['highlight_method'],
                #                hide_unused=False,
                #                this_current_screen_border=theme['foreground'],
                #                this_screen_border=theme['screenblur'],
                #                other_current_screen_border=theme['foreground'],
                #                other_screen_border=theme['screenblur'],
                #                urgent_alert_method='text',
                #                fontsize=fontsize,
                #                borderwidth=2,
                #                visible_groups=['1','2','3','4','5']
                #                ),
#widget.Sep(linewidth=5, opacity=0.2, background="#00ffffff"),

            widget.Image(
                    background = '#353446',
                    filename='~/.config/qtile/Assets/1.png',
                    ),


            widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                    ),

            widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    ),


            widget.Image(
                    background = '#282738',
                    filename='~/.config/qtile/Assets/5.png',
                    ),


            widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": config_funcs.search},
                    ),

            widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#CAA9E0',
                    mouse_callbacks={"Button1": config_funcs.search},
                    ),


            widget.Image(
                    background = '#282738',
                    filename='~/.config/qtile/Assets/4.png',
                    ),

            widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font='FiraCode Bold',
                    foreground='#CAA9E0',
                    empty_group_string = 'Desktop',
                    fontsize=14,
                    ),

            widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                    ),

            widget.Systray(
                    background="#282738",
                    foreground="#CAA9E0",
                    fontsize=14,
                    ),

            widget.TextBox(
                    text=' ',
                    background='#282738',
                    ),


            widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#282738',
                    ),

            widget.Image(
                    filename='~/.config/qtile/Assets/Drop1.png',
                    ),

            widget.Net(
                    format=' {up} | {down} ',
                    background='353446',
                    foreground='CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=12,
                    prefix='k',
                    ),

            widget.Image(
                    background='#353446',
                    filename='~/.config/qtile/Assets/2.png',
                    ),

            widget.Spacer(
                    length=8,
                    background='#353446',
                    ),

            widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                    ),

            widget.Spacer(
                    length=-7,
                    background='#353446',
                    ),


            widget.Memory(
                    background='#353446',
                    #format='{MemUsed: .0f}{mm}',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                    ),

#            widget.WindowName(foreground=theme['text'], background="#00000000", #theme['background'], 
                               #                fontsize=fontsize, for_current_screen=True),

            widget.Image(
                background='#353446',
                filename='~/.config/qtile/Assets/2.png',
            ),

            widget.Spacer(
                length=8,
                background='#353446',
            ),

#widget.Net(fontsize=20, decorations=[RectDecoration(colour=colors[6], radius=7, filled=True)],),
            #            widget.GenPollText(func=config_funcs.get_dirty_mem_M, update_interval=15, foreground='#ff4400'),
            #            widget.Clock(format='%Z %H:%M', timezone="PST8PDT", foreground='#3030a0'),
            #            widget.Clock(format='%Z %H:%M', timezone="America/Los_Angeles", foreground='#805000'),
            #            widget.Clock(format='%Z %H:%M'),
            #left_arrow(theme, colors[6]),
#            widget.Sep(background=colors[1], linewidth=3, padding=0, margin_y=20, **decoration_group),
             widget.PulseVolume(
                      font='JetBrainsMono Nerd Font',
                      theme_path='~/.config/qtile/Assets/Volume/',
                      emoji=True,
                      fontsize=13,
                      background='#353446',
                      ),

            widget.PulseVolume(
               font='JetBrains Mono Bold',
               background='#353446',
                foreground='#CAA9E0',
                fontsize=13,
            ),


            widget.Image(
                filename='~/.config/qtile/Assets/5.png',
                background='#353446',
            ),
            widget.Spacer(
                 length=-5,
                 background='#353446',
                 ),
            widget.Image(
                 filename='~/.config/qtile/Assets/Misc/clock.png',
                 background='#282738',
                 margin_y=6,
                 margin_x=5,
                 ),
            widget.Clock(
                 format='%I:%M %p | %Y-%m-%d %a',
                 background='#282738',
                 foreground='#CAA9E0',
                 font="JetBrains Mono Bold",
                 fontsize=14,
                 mouse_callbacks={"Button1": config_funcs.show_calendar},
                 ),


            widget.Spacer(
             length=18,
            background='#282738',
            ),
 #widget.Clock(
         #    format='🗓%a %Y-%m-%d 🕑 %H:%M %Z', margin_y=10, 
         #    #background=colors[9]
         #    decorations=[RectDecoration(colour=colors[9], radius=7, filled=True)],
         #    ),
 #            widget.Volume(mute_command="pactl set-sink-mute 3 toggle", background=colors[0], padding = 2),
                       #widget.Systray(icon_size=34, background=colors[2], fontsize=26),
            ]
    #apply_theme(theme, widgets)
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
                active=theme['focus'],
                inactive=theme['floatblur'],
                rounded=True,
                this_current_screen_border=theme['foreground'],
                this_screen_border=theme['screenblur'],
                other_current_screen_border=theme['foreground'],
                other_screen_border=theme['screenblur'],
                urgent_alert_method='text',
                fontsize=fontsize,
                borderwidth=2,
                visible_groups=['6','7','8','9']),
            #        widget.PulseVolume(),
            #        widget.Pomodoro(),
            #        widget.SwapGraph(),
            #        widget.ThermalSensor(),
            #        widget.Volume(mute_command="pactl set-sink-mute 3 toggle"),
            #        widget.Wallpaper(),
            widget.WindowName(
                background=theme['screenblur'],
                ),
            widget.Image(
                filename='~/.config/qtile/Assets/Misc/clock.png',
                background='#282738',
                margin_y=6,
                margin_x=5,
                ),
            widget.Clock(
                format='%I:%M %p | %Y-%m-%d %a',
                background='#282738',
                foreground='#CAA9E0',
                font="JetBrains Mono Bold",
                fontsize=14,
                ),
            widget.Spacer(
                length=18,
                background='#282738',
                ),
            ]

    #apply_theme(theme, widgets)
    return widgets


