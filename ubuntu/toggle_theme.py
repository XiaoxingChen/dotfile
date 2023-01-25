#!/usr/bin/python3

import os

def readCurrentColorTheme():
    theme_name = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
    theme_name = theme_name.replace('\n', '')
    theme_name = theme_name.replace("'", '')
    return theme_name

def setColorTheme(theme_name):
    ret = os.popen('gsettings set org.gnome.desktop.interface gtk-theme ' + theme_name).read()


if __name__ == "__main__":
    revert = {'Yaru-dark': 'Yaru-light', 'Yaru-light': 'Yaru-dark'}
    theme_name = readCurrentColorTheme()
    setColorTheme(revert[theme_name])