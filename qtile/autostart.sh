#!/bin/bash

. ~/.screenlayout/awesome-monitor-orientation.sh
numlockx
compton &
nitrogen --restore &
pactl set-default-sink alsa_output.pci-0000_00_1f.3.analog-stereo
