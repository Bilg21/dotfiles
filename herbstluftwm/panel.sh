#!/bin/bash

hc() { "${herbstclient_command[@]:-herbstclient}" "$@" ;}
monitor=${1:-0}
geometry=( $(herbstclient monitor_rect "$monitor") )
if [ -z "$geometry" ] ;then
    echo "Invalid monitor $monitor"
    exit 1
fi
# geometry has the format W H X Y
x_offset=42
y_offset=4
x=$(echo "${geometry[0]} + $x_offset" | bc)
y=$(echo "${geometry[1]} + $y_offset" | bc)
panel_width=$(echo "${geometry[2]} - (2 * $x_offset + 1)" | bc)
monitor_width=${geometry[2]}
fn="$HOME/.config/herbstluftwm/monitor.d/${monitor_width}x${geometry[3]}.sh"
[ -f "${fn}" ] && source "${fn}"
panel_height=${pad_up}
font="-*-Migu 1M-medium-*-*-*-16-*-*-*-*-*-*-*"
# bgcolor=$(hc get frame_border_normal_color)
bgcolor='#000000'
selbg='#ff005f'
selfg='#000000'

####
# Try to find textwidth binary.
# In e.g. Ubuntu, this is named dzen2-textwidth.
# if which textwidth &> /dev/null ; then
#     textwidth="textwidth";
# elif which dzen2-textwidth &> /dev/null ; then
#     textwidth="dzen2-textwidth";
# else
#     echo "This script requires the textwidth tool of the dzen2 project."
#     exit 1
# fi
####
# true if we are using the svn version of dzen2
# depending on version/distribution, this seems to have version strings like
# "dzen-" or "dzen-x.x.x-svn"
if dzen2 -v 2>&1 | head -n 1 | grep -q '^dzen-\([^,]*-svn\|\),'; then
    dzen2_svn="true"
else
    dzen2_svn=""
fi

if awk -Wv 2>/dev/null | head -1 | grep -q '^mawk'; then
    # mawk needs "-W interactive" to line-buffer stdout correctly
    # http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=593504
    uniq_linebuffered() {
      awk -W interactive '$0 != l { print ; l=$0 ; fflush(); }' "$@"
    }
else
    # other awk versions (e.g. gawk) issue a warning with "-W interactive", so
    # we don't want to use it there.
    uniq_linebuffered() {
      awk '$0 != l { print ; l=$0 ; fflush(); }' "$@"
    }
fi

# hc pad $monitor $panel_height

{
    ### Event generator ###
    # based on different input data (mpc, date, hlwm hooks, ...) this generates events, formed like this:
    #   <eventname>\t<data> [...]
    # e.g.
    #   date    ^fg(#efefef)18:33^fg(#909090), 2013-10-^fg(#efefef)29

    #mpc idleloop player &
    while true ; do
        # "date" output is checked once a second, but an event is only
        # generated if the output changed compared to the previous run.
        # date +$'date\t^fg(#ece391)%a %m/%d %H:%M'
        date +$'date\t^fg(#909090)%a %m/%d %H:%M%p %Z'
        sleep 1 || break
    done > >(uniq_linebuffered) &
    childpid=$!
    hc --idle
    kill $childpid
} 2> /dev/null | {
    IFS=$'\t' read -ra tags <<< "$(hc tag_status $monitor)"
    visible=true
    date=""
    windowtitle=""
    while true ; do

        ### Output ###
        # This part prints dzen data based on the _previous_ data handling run,
        # and then waits for the next event to happen.

        # bordercolor="#26221C"
        bordercolor="#000000"
        separator="^bg()^fg(#666666) :"
        titlecolor="#666666"
        # draw tags
        for i in "${tags[@]}" ; do
            tag_char=""
            case ${i:0:1} in
                '#')  # the tag is viewed on the specified monitor and it is focused
                    echo -n "^bg()^fg($selbg)"
                    tag_char="●"
                    titlecolor="${selbg}"
                    ;;
                '+')  # the tag is viewed on the specified monitor but the monitor is not focused
                    echo -n "^bg()^fg(#A8B6B8)"
                    tag_char="●"
                    ;;
                ':')  # the tag is not empty
                    echo -n "^bg()^fg(#666666)"
                    tag_char="●"
                    ;;
                '!')  # the tag contains an urgent window
                    echo -n "^bg(#FF0675)^fg(#141414)"
                    tag_char="*"
                    ;;
                '%')  # the tag is viewed on a different monitor and this monitor is not focused
                    echo -n "^bg()^fg($selbg)"
                    tag_char="⦿"
                    ;;
                '-')  # the tag is viewed on a different monitor and this monitor is not focused
                    echo -n "^bg()^fg(#A8B6B8)"
                    tag_char="⦿"
                    ;;
                *)
                    echo -n "^bg()^fg(#666666)"
                    tag_char="○"
                    ;;
            esac
            if [ ! -z "$dzen2_svn" ] ; then
                # clickable tags if using SVN dzen
                echo -n "^ca(1,\"${herbstclient_command[@]:-herbstclient}\" "
                echo -n "focus_monitor \"$monitor\" && "
                echo -n "\"${herbstclient_command[@]:-herbstclient}\" "
                # echo -n "use \"${i:1}\") ${i:1} ^ca()"
                echo -n "use \"${i:1}\") ${tag_char}^ca()"
            else
                # non-clickable tags if using older dzen
                echo -n " ${i:1} "
            fi
        done
        echo -n "$separator"
        echo -n "^bg()^fg(${titlecolor}) ${windowtitle//^/^^}"
        # small adjustments
        right="^bg() $date"
        right_text_only=$(echo -n "$right" | sed 's.\^[^(]*([^)]*)..g')
        # get width of right aligned text.. and add some space..
        # width=$($textwidth "$font" "$right_text_only    ")
        width=200
        echo -n "^pa($(($panel_width - $width)))$right"
        echo

        ### Data handling ###
        # This part handles the events generated in the event loop, and sets
        # internal variables based on them. The event and its arguments are
        # read into the array cmd, then action is taken depending on the event
        # name.
        # "Special" events (quit_panel/togglehidepanel/reload) are also handled
        # here.

        # wait for next event
        IFS=$'\t' read -ra cmd || break
        # find out event origin
        case "${cmd[0]}" in
            tag*)
                #echo "resetting tags" >&2
                IFS=$'\t' read -ra tags <<< "$(hc tag_status $monitor)"
                ;;
            date)
                #echo "resetting date" >&2
                date="${cmd[@]:1}"
                ;;
            quit_panel)
                exit
                ;;
            togglehidepanel)
                currentmonidx=$(hc list_monitors | sed -n '/\[FOCUS\]$/s/:.*//p')
                if [ "${cmd[1]}" -ne "$monitor" ] ; then
                    continue
                fi
                if [ "${cmd[1]}" = "current" ] && [ "$currentmonidx" -ne "$monitor" ] ; then
                    continue
                fi
                echo "^togglehide()"
                if $visible ; then
                    visible=false
                    hc pad $monitor $(($(hc list_padding $monitor | cut -d' ' -f1) - 19))
                else
                    visible=true
                    hc pad $monitor $pad_up
                fi
                ;;
            reload)
                exit
                ;;
            focus_changed|window_title_changed)
                windowtitle="${cmd[@]:2}"
                ;;
            #player)
            #    ;;
        esac
    done

    ### dzen2 ###
    # After the data is gathered and processed, the output of the previous block
    # gets piped to dzen2.

} 2> /dev/null | dzen2 -w $panel_width -x $x -y $y -fn "$font" -h $panel_height \
    -e 'button3=' \
    -ta l -bg "$bgcolor" -fg '#efefef'
