#!/usr/bin/python3
import re

from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()

for line in c.display_kb().splitlines():
    trimmed = re.sub(r"\s{2,}", ";", line.strip())
    columns = trimmed.split(';')
    if len(columns) < 4:
        columns.insert(2, '')
    if len(columns) < 5:
        columns.append('')
#    trimmed = re.sub(r"\s+", " ", line)
#    print(line)
#    print(trimmed)
#    print(len(columns))
    mod = "[]" if len(columns[2]) == 0 else "[{}] + ".format(columns[2])
    print("{0: <25}{1: <25}{2: <50}{3}".format(mod, columns[1], columns[3], columns[4], width=200))



