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
    appendToConfigFile(Dir.bashrc, "alias toggle_theme='python3 {}'".format(Dir.toggle_theme_script), 'theme_toggle')

    console_font_setting = """# Set font when running in console
if [ $TERM == linux ]; then
    /bin/setfont /usr/share/consolefonts/Lat2-Terminus32x16.psf.gz
fi
"""
    appendToConfigFile(Dir.bashrc, console_font_setting, 'console_font')

def rootConfigSystem():
    appendToConfigFile(Dir.sysctl_conf, "kernel.sysrq = 1")
class Dir():
    bashrc = os.path.expanduser('~/.bashrc')
    sysctl_conf = '/etc/sysctl.d/99-sysctl.conf'
    script_folder = os.path.abspath(os.path.dirname(__file__))
    toggle_theme_script = os.path.join(script_folder, 'toggle_theme.py')

if __name__ == "__main__":
    if os.geteuid() == 0:
        rootConfigSystem()
    else:
        setGnome()
        configSystem()
        subprocess.call(['sudo', 'python3', *sys.argv])



