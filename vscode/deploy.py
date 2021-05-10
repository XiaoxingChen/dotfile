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

extension_list = [
    'eamodio.gitlens',
    'hediet.vscode-drawio',
    'LeetCode.vscode-leetcode',
    'ms-python.python',
    'ms-vscode-remote.remote-ssh',
    'ms-vscode-remote.remote-ssh-edit',
    'ms-vscode.cpptools',
    'redhat.java',
    'ritwickdey.LiveServer',
    'streetsidesoftware.code-spell-checker',
    'twxs.cmake']

def installExtensions(ext_list):
    for extension in ext_list:
        os.system('code --install-extension ' + extension)

def updateSettingFile(dirs):
    setting_dict = dict()
    # incrementally modify settings.json
    if os.path.isfile(dirs.vscode_system_setting_file):
        with open(dirs.vscode_system_setting_file) as f:
            setting_dict = json.load(f)

    os.makedirs(dirs.vscode_user_folder, exist_ok=True)

    with open(dirs.vscode_local_setting_file) as f:
        setting_dict_patch = json.load(f)

    for k in setting_dict_patch:
        setting_dict[k] = setting_dict_patch[k]
    with open(dirs.vscode_system_setting_file, 'w') as f:
        json.dump(setting_dict, f, indent=2)

def updateKeyBindings(dirs):
    # overwrite keybindings.json
    if not os.path.isdir(dirs.vscode_user_folder):
        os.makedirs(dirs.vscode_user_folder, exist_ok=True)
    shutil.copy(os.path.join(dirs.script_folder, 'keybindings.json'), dirs.vscode_user_folder)

def updateSnippets(dirs):
    # overwrite snippets folder
    os.makedirs(dirs.repo_snippets_folder, exist_ok=True)
    for filename in os.listdir(dirs.repo_snippets_folder):
        if os.path.splitext(filename)[1] == '.json':
            shutil.copy(os.path.join(dirs.repo_snippets_folder, filename), dirs.vscode_snippet_folder)

if __name__ == "__main__":
    dirs = Directory()
    updateSettingFile(dirs)
    updateKeyBindings(dirs)
    updateSnippets(dirs)
    installExtensions(extension_list)

    print('done!')

