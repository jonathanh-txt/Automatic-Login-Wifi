#!/bin/bash
if ping 8.8.8.8 -c 3; then
    notify-send "Network is connected"
    else
        cd ~/Automatic-Login-Wifi
        source .venv/bin/activate
        notify-send "@Wifi-SMK run Auto Login"
        python autoInput.py
fi