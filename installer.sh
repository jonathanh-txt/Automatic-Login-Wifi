#!/bin/bash
echo "=============================="
echo "Automatic-Login-Wifi Installer"
echo "=============================="
sleep 1
echo "Checking dependencies..."
echo "(1/5) checking for exist installation"
if ! ls $HOME/Automatic-Login-Wifi >/dev/null 2>&1; then
    echo "Error: cannot find package directory"
    exit 1
fi
echo "(2/5) checking for python"
if ! python --version; then
    echo "Error: cannot find python"
    exit 1
fi
echo "(3/5) checking for chrome"
if ! google-chrome-stable --version; then
    echo "Error: cannot find google-chrome-stable"
    exit 1
fi
echo "(4/5) checking for notify-send"
if ! notify-send --version; then
    echo "Error:cannot find notify-send"
    exit 1
fi
echo "(5/5) checking for pip"
if ! python -m pip -V; then
    echo "Error: cannot find pip"
    exit 1

fi
echo "installing..."
bash
sudo cp $HOME/Automatic-Login-Wifi/alwss.sh /usr/local/bin/alwss
sudo chmod +x /usr/local/bin/alwss
echo "Making virtual environment"
cd $HOME/Automatic-Login-Wifi
python -m venv $HOME/Automatic-Login-Wifi/.venv
source $HOME/Automatic-Login-Wifi/.venv/bin/activate
echo "Installing playwright"
python -m pip install playwright
alwss