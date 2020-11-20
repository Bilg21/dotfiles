#!/bin/bash

if [[ -z $1 ]]; then
	echo "missing arg: theme name"
	exit
fi

theme=$1

rm theme.conf
ln -s "./kitty-themes/themes/$theme.conf" ~/.config/kitty/theme.conf
