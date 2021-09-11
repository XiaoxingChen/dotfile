#!/usr/bin/python3
import os
import sys

def setGlobalIgnore():
    global_ignore_path = None
    if sys.platform in {'darwin', 'linux'}:
        global_ignore_path = os.path.join(os.environ['HOME'], '.gitignore_global')
    elif sys.platform == 'win32':
        global_ignore_path = os.path.join(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'], '.gitignore_global')
    with open(global_ignore_path, 'w') as f:
        f.write('/.vscode/\n')

    os.system('git config --global core.excludesfile {}'.format(global_ignore_path))

def setGitAutoComplete():
    if sys.platform != 'darwin':
        return

    sh_func = """
if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash ]; then
  . `brew --prefix`/etc/bash_completion.d/git-completion.bash
fi
"""
    bash_profile_path = os.path.join(os.environ['HOME'], '.bash_profile')
    with open(bash_profile_path, 'r') as f:
        if sh_func in f.read():
            print('git auto complete already configured')
            return

    os.system('brew install git bash-completion')
    with open(bash_profile_path, 'a') as f:
        f.write(sh_func)

if __name__ == "__main__":
    os.system("git config --global core.whitespace cr-at-eol")
    os.system("git config --global core.editor vim")
    setGlobalIgnore()
    setGitAutoComplete()
