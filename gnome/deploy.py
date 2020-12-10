#!/usr/bin/python3
import os

if __name__ == "__main__":
    os.system("gsettings set org.gnome.mutter workspaces-only-on-primary false")
    os.system("gsettings set org.gnome.shell.app-switcher current-workspace-only true")
