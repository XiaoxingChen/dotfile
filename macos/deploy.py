#!/usr/bin/python3
import os
import sys

def addBashOptions(bash_func):
    bash_profile_path = os.path.join(os.environ['HOME'], '.bash_profile')
    with open(bash_profile_path, 'r') as f:
        if bash_func in f.read():
            print('option already configured')
            return

    with open(bash_profile_path, 'a') as f:
        f.write(bash_func)

def setBashColor():
    # Reference:
    # https://stackoverflow.com/questions/1550288/os-x-terminal-colors
    sh_func = """
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
"""
    print("set bash color")
    addBashOptions(sh_func)

def setBashComplete():
    # Reference:
    # https://itnext.io/programmable-completion-for-bash-on-macos-f81a0103080b
    sh_func = """
export BASH_COMPLETION_COMPAT_DIR="/usr/local/etc/bash_completion.d"
[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"
"""

    print("set bash complete")
    addBashOptions(sh_func)

if __name__ == "__main__":
    if sys.platform != 'darwin':
        print('Current OS is not macosx. Quit.')
        quit()
    setBashColor()
    setBashComplete()