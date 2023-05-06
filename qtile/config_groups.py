#!/usr/bin/env python
# coding=utf-8
from libqtile.config import Group, ScratchPad, DropDown

from platforms import num_screens, hostname

terminal="kitty"

if num_screens[hostname] == 2:
    # 2 Screens (Desktop)
    groups = []
    groups.extend([
        Group("term", spawn=terminal, layout="columns", persist=True),
        Group("code", spawn="", layout="max", persist=True),
        Group("web", spawn="google-chrome", layout="max", persist=True),
        Group("files", spawn=["pcmanfm", "kitty -e vifm"], layout="columns", persist=True),
        Group("docs", spawn="", layout="max", persist=True),
        Group("media", spawn="", layout="max", persist=True),
        Group("server", spawn="kitty", layout="max", persist=True),
        Group("local", spawn="kitty", layout="max", persist=True),
        Group("tor", spawn="", layout="max", persist=True),
        Group("books", spawn="", layout="max", persist=True)
    ])
else:
    # 1 Screen (Laptop)
    groups = [Group(i) for i in ["web", "chat", "code", "term"]]

# Scratchpad
groups.append(
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "kitty", opacity=0.8),
    ]),
)

