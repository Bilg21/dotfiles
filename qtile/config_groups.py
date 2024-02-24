#!/usr/bin/env python3
# coding=utf-8
from libqtile.config import Group, ScratchPad, DropDown, Match

# from platforms import num_screens, hostname

terminal = "kitty"


def init_groups():
    groups = [
        # Scratchpad groups
        ScratchPad("0", [
            DropDown("term", terminal),
            DropDown("fm", "kitty -e ranger", opacity=0.80,
                     height=0.50, width=0.60, x=0.10, y=0.02),
            DropDown("fm2", "kitty -e vifm", opacity=0.80,
                     height=0.50, width=0.60, x=0.10, y=0.02),
            DropDown("calc", "gnome-calculator", opacity=0.98,
                     height=0.50, width=0.30, x=0.10, y=0.02)
        ]),

        # regular groups
        Group("1", layout='max', label="1.www", matches=[
            Match(wm_class='google-chrome')], spawn="google-chrome"),
        Group("2", layout='columns', label="2"),
        Group("3", layout='columns'),
        Group("4", layout='columns'),
        Group("5", layout='columns', label="5.AI"),
        Group("6", layout='columns'),
        Group("7", layout='columns'),
        Group("8", layout='columns', label="8.music"),
        Group("9", layout='columns', label="9.obsidian", matches=[
            Match(wm_class="obsidian")], spawn="obsidian"),
    ]
    for g in groups:
        g.label = "◉"
    return groups
#
# if num_screens[hostname] == 2:
#    # 2 Screens (Desktop)
#    groups = []
#    groups.extend([
#        Group("term", spawn=terminal, layout="columns", persist=True),
#        Group("code", spawn="", layout="max", persist=True),
#        Group("web", spawn="google-chrome", layout="max", persist=True),
#        Group("files", spawn=["pcmanfm", "kitty -e vifm"], layout="columns", persist=True),
#        Group("docs", spawn="", layout="max", persist=True),
#        Group("media", spawn="", layout="max", persist=True),
#        Group("server", spawn="kitty", layout="max", persist=True),
#        Group("local", spawn="kitty", layout="max", persist=True),
#        Group("tor", spawn="", layout="max", persist=True),
#        Group("books", spawn="", layout="max", persist=True)
#    ])
# else:
#    # 1 Screen (Laptop)
#    groups = [Group(i) for i in ["web", "chat", "code", "term"]]
#
# Scratchpad
# groups.append(
#    ScratchPad("scratchpad", [
#        # define a drop down terminal.
#        # it is placed in the upper third of screen by default.
#        DropDown("term", "kitty", opacity=0.8),
#    ]),
# )
#
