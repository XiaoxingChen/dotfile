#!/usr/bin/python3

import os

def changeTheme():
    script_folder = os.path.abspath(os.path.dirname(__file__))
    apple_script_path = os.path.join(script_folder, 'change_theme.scpt')
    os.system('osascript ' + apple_script_path)

if __name__ == "__main__":
    changeTheme()