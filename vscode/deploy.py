#!/usr/bin/python3
import os
import sys
import shutil

class Directory():
    def __init__(self, argv0):
        if sys.platform == 'linux':
            self.vscode_home = os.path.expanduser('~/.config/Code')
        else:
            raise RuntimeError("Platform doesn't support!")
        self.vscode_user_folder = os.path.join(self.vscode_home, 'User')
        self.vscode_snippet_folder = os.path.join(self.vscode_user_folder, 'snippets')
        self.script_folder = os.path.dirname(os.path.realpath(argv0))
        self.repo_snippets_folder = os.path.join(self.script_folder, 'snippets')

if __name__ == "__main__": 
    dirs = Directory(sys.argv[0])

    shutil.copy(os.path.join(dirs.script_folder, 'keybindings.json'), dirs.vscode_user_folder)
    for filename in os.listdir(dirs.repo_snippets_folder):
        if os.path.splitext(filename)[1] == '.json':
            shutil.copy(os.path.join(dirs.repo_snippets_folder, filename), dirs.vscode_snippet_folder)

    print('done!')

