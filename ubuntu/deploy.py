#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
from config_lib import *

def setGnome():
    os.system("gsettings set org.gnome.mutter workspaces-only-on-primary false")
    os.system("gsettings set org.gnome.shell.app-switcher current-workspace-only true")
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-applications \"['<Super>Tab']\"")
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-windows \"['<Alt>Tab']\"")

def configSystem():
    appendToConfigFile(Dir.bashrc, "alias ring='paplay /usr/share/sounds/gnome/default/alerts/glass.ogg'", 'alias_ring')
    appendToConfigFile(Dir.sysctl_conf, "kernel.sysrq = 1")

    console_font_setting = """# Set font when running in console
if [ $TERM == linux ]; then
    /bin/setfont /usr/share/consolefonts/Lat2-Terminus32x16.psf.gz
fi
"""
    appendToConfigFile(Dir.bashrc, console_font_setting, 'console_font')

class Dir():
    bashrc = os.path.expanduser('~/.bashrc')
    sysctl_conf = '/etc/sysctl.d/99-sysctl.conf'

if __name__ == "__main__":
    setGnome()
    configSystem()


