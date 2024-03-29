#!/usr/bin/env python3
# coding: utf-8
# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=100

# default config is in qtile repo in:
#   libqtile/resources/default_config.py
# when default-config is used due to config error, type:
#   WIN+CTRL+R  to restart qtile
#   WIN+R       to execute something

from libqtile.lazy import lazy
from libqtile.config import Key, Drag, Click, ScratchPad
from libqtile.log_utils import logger

import config_funcs

import copy


@lazy.function
def log_function(qtile, msg):
    logger.warning(msg)


def get_keys_and_mouse(groups):
    terminal = "kitty"
    mod = ["mod4"]
    shft = ["shift"]
    ctrl = ["control"]
    alt = ["mod1"]
    mswitch = ["mod5"]  # (modeswitch)

    keys = [

        # Layout

        # Toggle between different layouts as defined below
        Key(mod, "space",              lazy.next_layout()),
        Key(mod+shft, "space",         lazy.layout.flip()),
        # Swap panes of split stack
        Key(mod+shft, "n",             lazy.layout.rotate()),
        # Split := increase one window to full screen height, stack overlapped below
        Key(mod+shft, "Return",        lazy.layout.toggle_split()),

        Key(mod, "y",                  lazy.layout.shrink()),
        Key(mod, "u",                  lazy.layout.grow()),
        Key(mod, "i",                  lazy.layout.normalize()),
        Key(mod, "o",                  lazy.layout.maximize()),

        Key(mod, "h",                  lazy.layout.left()),
        Key(mod, "j",                  lazy.layout.down()),
        Key(mod, "k",                  lazy.layout.up()),
        Key(mod, "l",                  lazy.layout.right()),

        Key(mod, "n",                  lazy.layout.next()),
        Key(mod, "p",                  lazy.layout.previous()),

        Key(mod+shft, "h",             lazy.layout.shuffle_left()),
        Key(mod+shft, "j",             lazy.layout.shuffle_down()),
        Key(mod+shft, "k",             lazy.layout.shuffle_up()),
        Key(mod+shft, "l",             lazy.layout.shuffle_right()),

        Key(mod+ctrl, "h",             lazy.layout.grow_left()),
        Key(mod+ctrl, "j",             lazy.layout.grow_down()),
        Key(mod+ctrl, "k",             lazy.layout.grow_up()),
        Key(mod+ctrl, "l",             lazy.layout.grow_right()),

        Key(mod+ctrl+shft, "h",        lazy.layout.swap_left()),
        Key(mod+ctrl+shft, "j",        lazy.layout.swap_down()),
        Key(mod+ctrl+shft, "k",        lazy.layout.swap_up()),
        Key(mod+ctrl+shft, "l",        lazy.layout.swap_right()),

        # Screen
        Key(mod, "Left",               lazy.screen.prev_group(
            skip_empty=True, skip_managed=True)),
        Key(mod, "Right",              lazy.screen.next_group(
            skip_empty=True, skip_managed=True)),
        Key(mod+shft, "Left",          lazy.screen.prev_group(skip_managed=True)),
        Key(mod+shft, "Right",         lazy.screen.next_group(skip_managed=True)),
    ]
    _screenkeys = "wert"
    keys += [Key(mod, key,             lazy.to_screen(screen))
             for screen, key in enumerate(_screenkeys)]
    keys += [Key(mod+shft, key,        lazy.function(config_funcs.move_window_to_screen(screen)))
             for screen, key in enumerate(_screenkeys)]
    keys += [

        # Group
        Key(mod, "Tab",                lazy.function(
            config_funcs.next_window_to_front_if_float)),
        Key(mod+shft, "Tab",           lazy.group.next_window()),
    ]

    for i in groups:
        if i.name == "0":
            logger.warning("hotkeys are initialized")
            keys.append(
                Key(mod+ctrl, "f", lazy.group[i.name].dropdown_toggle("fm")))
            keys.append(
                Key(mod+ctrl, "comma", lazy.group[i.name].dropdown_toggle("fm2")))
            keys.append(
                Key(mod+ctrl, "period", lazy.group[i.name].dropdown_toggle("term")))
            keys.append(
                Key(mod+ctrl, "slash", lazy.group[i.name].dropdown_toggle("calc")))
        else:
            keys.append(
                Key(mod, i.name, lazy.group[i.name].toscreen(toggle=False)))
            keys.append(Key(mod+shft, i.name, lazy.window.togroup(i.name)))

    keys += [

        # Window

        Key(mod, "g",                  lazy.window.toggle_floating()),
        Key(mod, "q",                  lazy.window.kill()),
        Key(mod+shft, "m",             lazy.function(config_funcs.window_audio("mute"))),
        Key(mod+shft, "comma",
            lazy.function(config_funcs.window_audio("down"))),
        Key(mod+shft, "period",        lazy.function(config_funcs.window_audio("up"))),
        Key(mod+shft, "slash",
            lazy.function(config_funcs.window_audio("reset"))),

        # Other

        Key(mod+ctrl+shft, "r",             lazy.restart()),
        Key(mod+ctrl+shft, "q",        lazy.shutdown()),
        Key(mod, "Up",                 lazy.hide_show_bar()),
        Key(mod, "f",             lazy.window.toggle_fullscreen()),

        Key(mod, "BackSpace",          lazy.spawncmd()),
        Key(mod+shft, "r",
            lazy.spawn("/usr/bin/dmenu_run -l 10 -i -fn 'Monospace'")),
        Key(mod, "r",                  lazy.spawn(
            "rofi -show drun -show-icons"), "Nice Rofi Menu"),
        Key(mod, "Return",             lazy.spawn(terminal)),
        Key(mod, "Escape",             lazy.spawn("xautolock-force")),
        Key(mod+mswitch, "Escape",     lazy.spawn("xautolock -toggle")),
        Key([], "Print",               lazy.spawn(
            "/usr/bin/gnome-screenshot -i")),
        Key(mod, "s",                  lazy.spawn("/usr/bin/gnome-screenshot")),
        Key(mod+shft, "s",             lazy.spawn("/usr/bin/gnome-screenshot --window")),
        Key(mod+alt, "l",              lazy.spawn(
            "i3lock -i /home/bilg/Pictures/Wallpapers/wallpaper_mikael_gustafsson.png -e -f -t")),

        Key(mod, "v",                  lazy.spawn("paste_to_qrcode")),

        Key([], "XF86Display",         lazy.spawn("displace -af")),
        Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
        Key([], "XF86AudioMute",       lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    ]

    # Map function keys to special_keys script

    for _modifier in (("", "NONE"), (shft, "SHIFT"), (ctrl, "CTRL"), (alt, "ALT"), (mswitch, "MODESWITCH")
                      ):
        for _fkey in range(1, 13):
            _fkey_name = "F{}".format(_fkey)
            _mod = copy.copy(mod)
            if ("" != _modifier[0]):
                _mod += _modifier[0]
            keys.append(Key(_mod, _fkey_name, lazy.spawn(
                "special_keys {} {}".format(_fkey_name, _modifier[1]))))
    for _fkey in ("XF86MonBrightnessDown", "XF86MonBrightnessUp", "XF86LaunchA", "XF86LaunchB", "XF86KbdBrightnessDown", "XF86KbdBrightnessUp", "XF86AudioPrev", "XF86AudioNext", "XF86AudioPlay", "XF86AudioStop"  # , "XF86AudioMute"
                  , "XF86AudioMicMute"  # , "XF86AudioLowerVolume"
                  #                 , "XF86AudioRaiseVolume"
                  , "XF86Favorites", "XF86Eject"
                  ):
        keys.append(Key([], _fkey, lazy.spawn(
            "special_keys {} NONE".format(_fkey))))

    # Mouse config
    mouse = [
        Drag(mod, "Button1",           lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag(mod+shft, "Button1",      lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Drag(mod, "Button3",           lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
    ]

    return keys, mouse
