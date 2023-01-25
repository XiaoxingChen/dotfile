import os
import re
import subprocess
import sys

def askForRootPermission():
    if os.geteuid() == 0:
        print("run with root")
        return

    print("Permission denied")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()

def appendToConfigFile(file_path, setting_str, task=None, comment_char='#'):
    if not os.path.isfile(file_path):
        print("{} not found!", file_path)
        return

    task = file_path if task is None else task
    end_with_newline = False
    uncomment_pattern = comment_char + r'.*?(\n|$)'
    with open(file_path, 'r') as f:
        raw_str = f.read()
        end_with_newline = (len(raw_str) > 0 and raw_str[-1] == '\n')
        no_comment_file = re.sub(uncomment_pattern, '', raw_str)
        no_comment_setting = re.sub(uncomment_pattern, '', setting_str)
        if no_comment_setting in no_comment_file:
            print("skip " + task)
            return
    with open(file_path, 'a') as f:
        if not end_with_newline:
            f.write('\n')
        f.write(setting_str + '\n')