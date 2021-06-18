#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
from config_lib import appendToConfigFile

class Dir():
    bashrc = os.path.expanduser('~/.bashrc')
    bash_profile = os.path.expanduser('~/.bash_profile')
    inputrc = os.path.expanduser('~/.inputrc')

def setBashColor():
    # Reference:
    # https://stackoverflow.com/questions/1550288/os-x-terminal-colors
    sh_func = """
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
"""
    appendToConfigFile(Dir.bashrc, sh_func, "bash color")

def setBashComplete():
    # Reference:
    # https://itnext.io/programmable-completion-for-bash-on-macos-f81a0103080b
#     sh_func = """
# export BASH_COMPLETION_COMPAT_DIR="/usr/local/etc/bash_completion.d"
# [[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"
# """
    sh_func = """
[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"
"""

    appendToConfigFile(Dir.bashrc, sh_func, "bash complete")

def setBashProfile():
    sh_func = 'source "$HOME/.bashrc"'
    appendToConfigFile(Dir.bash_profile, sh_func, "bash profile forwarding")

def setInputrc():
    contents = """
set completion-ignore-case on
set show-all-if-ambiguous on
"""
    with open(Dir.inputrc, 'w') as f:
        f.write(contents)

def setCustonPrompt():
    contents = "export PS1='$(whoami)@$(hostname):$(pwd)$ '"
    appendToConfigFile(Dir.bashrc, contents, "bash custom prompt")

if __name__ == "__main__":
    if sys.platform != 'darwin':
        print('Current OS is not macosx. Quit.')
        quit()
    setBashColor()
    setBashComplete()
    setBashProfile()
    setInputrc()
    setCustonPrompt()