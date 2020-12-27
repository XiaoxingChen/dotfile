#!/usr/bin/python3
import os
import sys
import shutil

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
from config_lib import *

class Dir():
    vimrc = os.path.expanduser('~/.vimrc')

def configVim():
    if not os.path.isfile(Dir.vimrc):
        os.system("> " + Dir.vimrc)

    appendToConfigFile(Dir.vimrc, "set tabstop=4")
    appendToConfigFile(Dir.vimrc, "set shiftwidth=4")
    appendToConfigFile(Dir.vimrc, "set nu")
    appendToConfigFile(Dir.vimrc, "set expandtab")

if __name__ == "__main__":
    configVim()