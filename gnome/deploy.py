#!/usr/bin/python3
import os

if __name__ == "__main__":
    os.system("gsettings set org.gnome.mutter workspaces-only-on-primary false")
    os.system("gsettings set org.gnome.shell.app-switcher current-workspace-only true")
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-applications \"['<Super>Tab']\"")
    os.system("gsettings set org.gnome.desktop.wm.keybindings switch-windows \"['<Alt>Tab']\"")
