#!/usr/bin/python3
import os
import sys
import shutil
import platform
import json

class Directory():
    def __init__(self):
        if sys.platform == 'linux':
            if 'microsoft' in platform.uname().version.lower():
                print('Running in Windows Subsystem of Linux, please rerun this script in cmd.exe')
                quit(1)
            self.vscode_home = os.path.expanduser('~/.config/Code')
        elif sys.platform == 'win32':
            self.vscode_home = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Code')
        else:
            raise RuntimeError("Platform doesn't support!")
        self.vscode_user_folder = os.path.join(self.vscode_home, 'User')
        self.vscode_snippet_folder = os.path.join(self.vscode_user_folder, 'snippets')
        self.script_folder = os.path.dirname(os.path.realpath(__file__))
        self.repo_snippets_folder = os.path.join(self.script_folder, 'snippets')
        self.vscode_local_setting_file = os.path.join(self.script_folder, 'settings.json')
        self.vscode_system_setting_file = os.path.join(self.vscode_user_folder, 'settings.json')

if __name__ == "__main__":
    dirs = Directory()

    # overwrite keybindings.json
    shutil.copy(os.path.join(dirs.script_folder, 'keybindings.json'), dirs.vscode_user_folder)

    # incrementally modify settings.json
    with open(dirs.vscode_system_setting_file) as f:
        setting_dict = json.load(f)
    with open(dirs.vscode_local_setting_file) as f:
        setting_dict_patch = json.load(f)

    for k in setting_dict_patch:
        setting_dict[k] = setting_dict_patch[k]
    with open(dirs.vscode_system_setting_file, 'w') as f:
        json.dump(setting_dict, f, indent=2)

    # overwrite snippets folder
    for filename in os.listdir(dirs.repo_snippets_folder):
        if os.path.splitext(filename)[1] == '.json':
            shutil.copy(os.path.join(dirs.repo_snippets_folder, filename), dirs.vscode_snippet_folder)

    print('done!')

