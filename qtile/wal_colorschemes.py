#!/usr/bin/env python3
# coding: utf-8
# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=100

with open(home + '/.cache/wal/colors.json') as wal_import:
  data = json.load(wal_import)
  wallpaper = data['wallpaper']
  colors = data['colors']
  val_colors = list(colors.values())
  def getList(val_colors):
    return [*val_colors]
    
  def init_colors():
    return [*val_colors]

color = init_colors()

