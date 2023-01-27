#!/usr/bin/python3

import os

def readCurrentColorTheme():
    theme_name = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
    theme_name = theme_name.replace('\n', '')
    theme_name = theme_name.replace("'", '')
    return theme_name

def readDefaultTerminalProfile():
    profile_uid = os.popen('gsettings get org.gnome.Terminal.ProfilesList default').read()
    profile_uid = profile_uid.replace('\n', '')
    profile_uid = profile_uid.replace("'", '')
    return profile_uid

def setTerminalColor(target_state_dark):
    profile_uid = readDefaultTerminalProfile()
    config_head = 'gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:' + profile_uid + '/'

    print(config_head)
    while_hex = "'#FFFFFF'"
    black_hex = "'#000000'"
    if(target_state_dark):
        os.system(config_head + ' background-color ' + black_hex)
        os.system(config_head + ' foreground-color ' + while_hex)
    else:
        os.system(config_head + ' background-color ' + while_hex)
        os.system(config_head + ' foreground-color ' + black_hex)


def setColorTheme(theme_name):
    ret = os.popen('gsettings set org.gnome.desktop.interface gtk-theme ' + theme_name).read()


if __name__ == "__main__":
    is_dark_theme = {'Yaru-dark': True, 'Yaru-light': False}
    dark_theme_names = {True: 'Yaru-dark', False: 'Yaru-light'}

    theme_name = readCurrentColorTheme()
    curr_dark_state = is_dark_theme[theme_name]
    target_state = not curr_dark_state
    setColorTheme(dark_theme_names[target_state])
    setTerminalColor(target_state)